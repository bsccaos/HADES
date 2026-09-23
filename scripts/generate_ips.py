#!/usr/bin/env python3
import csv
import os
import urllib.request
import urllib.parse
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, ".."))

csv_path = os.path.join(repo_root, "docs", "ips.csv")
md_path = os.path.join(repo_root, "docs", "ips", "index.md")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    items = list(reader)

def get_bibtex(doi):
    headers = {"Accept": "application/x-bibtex; charset=utf-8"}
    url = f"https://doi.org/{doi.strip()}"
    try:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=5) as resp:
            return resp.read().decode('utf-8').strip()
    except Exception as e:
        return f"% BibTeX for {doi} could not be retrieved automatically: {e}"

md_lines = [
    "# Hardware IPs",
    "",
    "The HADES research group develops a suite of open-source Register Transfer Level (RTL) IP cores designed for timing verification, fault-tolerance, diversity monitoring, and safety-critical execution in high-performance embedded systems across space, automotive, and railway domains.",
    "",
    "---",
    "",
    "## 🛡️ Featured Hardware IP Cores",
    ""
]

for idx, item in enumerate(items, 1):
    title = item["title"].strip()
    desc = item["description"].strip()
    dois = [d.strip() for d in item["dois"].split(";") if d.strip()]
    labels = [l.strip() for l in item["doi_labels"].split(";") if l.strip()]
    repo_name = item["repository_name"].strip()
    repo_url = item["repository_url"].strip()

    md_lines.append(f"### {idx}. {title}")
    md_lines.append(desc)
    md_lines.append("")

    doi_links = []
    for d in dois:
        doi_links.append(f"[{d}](https://doi.org/{d})")
    
    if doi_links:
        md_lines.append(f"- **DOI / Publications**: {' | '.join(doi_links)}")
    
    if repo_url:
        md_lines.append(f"- **Repository**: [{repo_name}]({repo_url})")
    
    if dois:
        md_lines.append("")
        md_lines.append('??? info "📥 Export Citation (BibTeX)"')
        md_lines.append("")
        for d, lbl in zip(dois, labels if len(labels) == len(dois) else ["Citation"] * len(dois)):
            bib = get_bibtex(d)
            md_lines.append(f"    **{lbl}**: [Download .bib File](https://api.crossref.org/works/{d}/transform/application/x-bibtex)")
            md_lines.append("    ```bibtex")
            for bib_line in bib.splitlines():
                md_lines.append(f"    {bib_line}")
            md_lines.append("    ```")
            md_lines.append("")

    md_lines.append("---")
    md_lines.append("")

with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Generated {md_path} from {csv_path}")
