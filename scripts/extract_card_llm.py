import argparse
import csv
import json
import os
from pathlib import Path
from tempfile import NamedTemporaryFile
from datetime import datetime, timezone

import yaml
from openai import OpenAI
from dotenv import load_dotenv

from chunk_split import select_doc_ids

# 加载环境变量
load_dotenv()

def load_config(path: Path):
    with path.open('r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_prompt(system_prompt_file: Path):
    with system_prompt_file.open('r', encoding='utf-8') as f:
        return f.read()

def load_schema(schema_file: Path):
    with schema_file.open('r', encoding='utf-8') as f:
        return f.read()


def read_manifest_rows(manifest_path: Path):
    with manifest_path.open('r', encoding='utf-8-sig', newline='') as f:
        reader = csv.DictReader(f)
        rows = list(reader)
        return rows, list(reader.fieldnames or [])


def write_manifest_rows(manifest_path: Path, rows, fieldnames):
    with NamedTemporaryFile('w', encoding='utf-8', newline='', dir=manifest_path.parent, delete=False) as tmp:
        writer = csv.DictWriter(tmp, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)
        temp_path = Path(tmp.name)
    temp_path.replace(manifest_path)


def ensure_manifest_fields(fieldnames):
    extra_fields = [
        'extract_status',
        'extract_model_version',
        'extract_prompt_version',
        'extract_updated_at',
        'extract_output_path',
        'extract_error',
    ]
    merged = list(fieldnames)
    for field in extra_fields:
        if field not in merged:
            merged.append(field)
    return merged


def utc_timestamp():
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace('+00:00', 'Z')


def relative_to_root(path: Path, root: Path) -> str:
    try:
        return str(path.relative_to(root))
    except ValueError:
        return str(path)


def update_manifest_entry(row, *, status, model_name, prompt_version, output_path=None, error=''):
    row['extract_status'] = status
    row['extract_model_version'] = model_name
    row['extract_prompt_version'] = prompt_version
    row['extract_updated_at'] = utc_timestamp()
    row['extract_output_path'] = output_path or row.get('extract_output_path', '')
    row['extract_error'] = error


def atomic_write_json(path: Path, payload):
    with NamedTemporaryFile('w', encoding='utf-8', dir=path.parent, delete=False) as tmp:
        json.dump(payload, tmp, ensure_ascii=False, indent=2)
        temp_path = Path(tmp.name)
    temp_path.replace(path)

def extract_information(md_content, doc_id, config, system_prompt, schema_text):
    model_config = config['model']
    api_key_env = model_config.get('api_key_env', 'BAILIAN_API_KEY')
    api_key = os.getenv(api_key_env)
    base_url = model_config.get('base_url')
    model_name = model_config.get('model_name')
    
    if not api_key:
        raise ValueError(f"未找到 API Key，请检查环境变量: {api_key_env}")
        
    client = OpenAI(api_key=api_key, base_url=base_url)
    
    user_prompt = f"""
以下是一篇文献的 Markdown 内容。请根据系统提示词的要求，并严格遵循以下 extraction schema 进行提取：

## JSON Schema:
{schema_text}

## 文献内容:
{md_content}

请直接返回 JSON 数据，不要包含任何额外的说明文字或 markdown 代码块标记。
"""

    response = client.chat.completions.create(
        model=model_name,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.1 # 降低随机性
    )
    
    result_text = response.choices[0].message.content.strip()
    # 简单的清理，以防大模型还是输出了 markdown 标记
    if result_text.startswith("```json"):
        result_text = result_text[7:]
    if result_text.startswith("```"):
        result_text = result_text[3:]
    if result_text.endswith("```"):
        result_text = result_text[:-3]
        
    result_text = result_text.strip()
    
    try:
        # 尝试解析，如果失败会抛出异常
        parsed_json = json.loads(result_text)
        # 强制更新 doc_id
        parsed_json["doc_id"] = doc_id
        return parsed_json
    except json.JSONDecodeError as e:
        print(f"[{doc_id}] JSON 解析失败。大模型原始输出:\n{result_text}")
        raise e

def main():
    parser = argparse.ArgumentParser(description="Extract structured literature cards with LLM.")
    parser.add_argument("--config", default="config.yaml", type=Path)
    parser.add_argument("--doc-id", action="append", default=[])
    parser.add_argument("--batch", help="A, B, C, or a manifest batch prefix")
    parser.add_argument("--force", action="store_true", help="Overwrite existing extracted JSON files")
    args = parser.parse_args()

    config = load_config(args.config)
    root = args.config.resolve().parent
    system_prompt = load_prompt(root / config['model']['system_prompt_file'])
    schema_text = load_schema(root / config['paths']['extraction_schema'])
    model_name = config['model']['model_name']
    prompt_version = config['model'].get('prompt_version', '')

    parsed_dir = root / config['paths']['parsed']
    cards_dir = root / config['paths']['cards']
    manifest_path = root / config['paths']['manifest']

    cards_dir.mkdir(parents=True, exist_ok=True)

    manifest_rows, fieldnames = read_manifest_rows(manifest_path)
    fieldnames = ensure_manifest_fields(fieldnames)
    row_by_doc_id = {row['doc_id']: row for row in manifest_rows if row.get('doc_id')}

    selected_doc_ids = select_doc_ids(manifest_path, args.doc_id, args.batch)
    if not selected_doc_ids:
        print("No documents selected.")
        return

    if not args.doc_id and not args.batch and not args.force:
        doc_ids = [
            doc_id for doc_id in selected_doc_ids
            if row_by_doc_id.get(doc_id, {}).get('extract_status', '').strip().lower() != 'done'
        ]
    else:
        doc_ids = selected_doc_ids

    if not doc_ids:
        print("No documents selected.")
        return

    manifest_dirty = False

    for doc_id in doc_ids:
        row = row_by_doc_id.get(doc_id)
        md_file = parsed_dir / f"{doc_id}.md"
        output_file = cards_dir / f"{doc_id}.json"
        output_rel_path = relative_to_root(output_file, root)

        if not md_file.exists():
            print(f"[missing] {md_file}")
            if row is not None:
                update_manifest_entry(
                    row,
                    status='missing_input',
                    model_name=model_name,
                    prompt_version=prompt_version,
                    output_path=output_rel_path,
                    error=f'missing parsed markdown: {relative_to_root(md_file, root)}',
                )
                manifest_dirty = True
            continue
        if output_file.exists() and not args.force:
            print(f"[{doc_id}] 已存在，跳过提取。")
            if row is not None and row.get('extract_status', '').strip().lower() != 'done':
                update_manifest_entry(
                    row,
                    status='done',
                    model_name=model_name,
                    prompt_version=prompt_version,
                    output_path=output_rel_path,
                )
                manifest_dirty = True
            continue

        print(f"开始提取: {doc_id} ...")
        with md_file.open('r', encoding='utf-8') as f:
            md_content = f.read()

        try:
            extracted_json = extract_information(md_content, doc_id, config, system_prompt, schema_text)
            atomic_write_json(output_file, extracted_json)
            if row is not None:
                update_manifest_entry(
                    row,
                    status='done',
                    model_name=model_name,
                    prompt_version=prompt_version,
                    output_path=output_rel_path,
                )
                manifest_dirty = True
            print(f"[{doc_id}] 提取成功，已保存至 {output_file}")
        except Exception as e:
            if row is not None:
                update_manifest_entry(
                    row,
                    status='failed',
                    model_name=model_name,
                    prompt_version=prompt_version,
                    output_path=output_rel_path,
                    error=str(e),
                )
                manifest_dirty = True
            print(f"[{doc_id}] 提取过程中发生错误: {e}")

    if manifest_dirty:
        write_manifest_rows(manifest_path, manifest_rows, fieldnames)

if __name__ == "__main__":
    main()
