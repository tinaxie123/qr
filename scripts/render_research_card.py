import os
import json
import glob
import yaml

def load_config():
    with open('config.yaml', 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def render_markdown(card_data):
    doc_id = card_data.get('doc_id', 'Unknown')
    metadata = card_data.get('metadata', {})
    
    md_lines = []
    md_lines.append(f"# {metadata.get('title', 'Unknown Title')}")
    md_lines.append(f"**Doc ID:** {doc_id}")
    authors = ", ".join(metadata.get('authors', []))
    md_lines.append(f"**Authors:** {authors}")
    md_lines.append(f"**Year:** {metadata.get('publication_year', 'Unknown')}")
    md_lines.append("")
    
    md_lines.append("## 1. 原文事实 (Original)")
    original = card_data.get('original', {})
    
    def render_original_section(title, data):
        md_lines.append(f"### {title}")
        desc = data.get('description', '缺失')
        locators = data.get('source_locators', [])
        md_lines.append(f"{desc}")
        if locators:
            md_lines.append(f"*Sources: {', '.join(locators)}*")
        else:
            md_lines.append("*Sources: [] (未提供)*")
        md_lines.append("")

    render_original_section("研究场景 (Research Scenario)", original.get('research_scenario', {}))
    render_original_section("经济机制 (Economic Mechanism)", original.get('economic_mechanism', {}))
    
    md_lines.append("### 特征公式 (Feature Formulas)")
    formulas = original.get('feature_formulas', [])
    if not formulas:
        md_lines.append("原文未提及公式。")
    else:
        for f in formulas:
            md_lines.append(f"**{f.get('name', 'Unnamed Formula')}**")
            md_lines.append(f"$$ {f.get('formula', '')} $$")
            locators = f.get('source_locators', [])
            if locators:
                md_lines.append(f"*Sources: {', '.join(locators)}*")
            variables = f.get('variables', [])
            if variables:
                md_lines.append("- 变量说明：")
                for v in variables:
                    md_lines.append(f"  - `{v.get('symbol', '')}`: {v.get('meaning', '')}")
            md_lines.append("")
            
    render_original_section("数据处理 (Data Processing)", original.get('data_processing', {}))
    render_original_section("检验方法 (Testing Methods)", original.get('testing_methods', {}))
    render_original_section("稳健性与失败 (Robustness & Failures)", original.get('robustness_and_failures', {}))
    render_original_section("交易可实现性 (Tradability)", original.get('tradability', {}))

    md_lines.append("## 2. 项目适配 (Adaptation)")
    adaptation = card_data.get('adaptation', {})
    md_lines.append("### 与项目契合度")
    md_lines.append(adaptation.get('project_fit', '未提供'))
    md_lines.append("### 调整建议")
    md_lines.append(adaptation.get('adjustments_needed', '未提供'))
    md_lines.append(f"### 数据充分性\n{adaptation.get('data_sufficiency', '未提供')}")
    md_lines.append(f"### 复现模式\n{adaptation.get('replication_mode', '未提供')}")
    missing_fields = adaptation.get('missing_fields', [])
    md_lines.append(f"### 缺失字段\n{', '.join(missing_fields) if missing_fields else '无'}")
    md_lines.append("")

    md_lines.append("## 3. 扩展假设 (Extensions)")
    extensions = card_data.get('extensions', [])
    if not extensions:
        md_lines.append("无扩展假设。")
    else:
        for i, ext in enumerate(extensions, 1):
            md_lines.append(f"### 假设 {i}")
            md_lines.append(f"**内容:** {ext.get('hypothesis', '')}")
            rationale = ext.get('rationale')
            if rationale:
                md_lines.append(f"**推导理由:** {rationale}")
            source_locators = ext.get('source_locators', [])
            md_lines.append(f"**本文证据:** {', '.join(source_locators) if source_locators else '无'}")
            basis = ext.get('basis_evidence_ids', [])
            md_lines.append(f"**跨文献证据ID:** {', '.join(basis) if basis else 'L2 暂空，待 L3 回填'}")
            md_lines.append("")
            
    return "\n".join(md_lines)

def main():
    config = load_config()
    cards_dir = config['paths']['cards']
    md_out_dir = config['paths']['review'] + "/cards_md"
    
    os.makedirs(md_out_dir, exist_ok=True)
    
    json_files = glob.glob(os.path.join(cards_dir, "*.json"))
    if not json_files:
        print("未找到任何 JSON 卡片文件。")
        return
        
    for jf in json_files:
        filename = os.path.basename(jf)
        doc_id = os.path.splitext(filename)[0]
        with open(jf, 'r', encoding='utf-8') as f:
            card_data = json.load(f)
            
        md_content = render_markdown(card_data)
        out_path = os.path.join(md_out_dir, f"{doc_id}.card.md")
        
        with open(out_path, 'w', encoding='utf-8') as f:
            f.write(md_content)
        print(f"[{doc_id}] 已渲染 Markdown 至 {out_path}")

if __name__ == "__main__":
    main()
