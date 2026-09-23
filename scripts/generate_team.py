#!/usr/bin/env python3
import csv
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
repo_root = os.path.abspath(os.path.join(script_dir, ".."))

csv_path = os.path.join(repo_root, "docs", "team.csv")
md_path = os.path.join(repo_root, "docs", "team.md")

with open(csv_path, "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    team_data = list(reader)

category_headers = [
    ("Group Leader", "👥 Group Leader"),
    ("Senior Staff", "⭐️ Senior Staff"),
    ("Early Career Researchers", "🔬 Early Career Researchers"),
    ("Research Engineers", "⚙️ Research Engineers"),
    ("Visitors & External Collaborators", "🤝 Visitors & External Collaborators"),
]

md_lines = [
    "# HADES Team & Organization",
    "",
    "The **HArdware Dependability for Embedded Systems (HADES)** group is part of the **High-Performance Embedded Systems (HPES)** laboratory at the **Barcelona Supercomputing Center (BSC-CNS)**.",
    "",
    "---",
    ""
]

for cat_key, cat_title in category_headers:
    cat_items = [item for item in team_data if item["category"].strip() == cat_key]
    if cat_items:
        md_lines.append(f"## {cat_title}")
        md_lines.append("")
        for item in cat_items:
            name_str = item["name"].strip()
            pos_str = item["position"].strip()
            orcid = item["orcid"].strip() if "orcid" in item and item["orcid"] else ""
            
            orcid_html = ""
            if orcid:
                orcid_html = f' <a href="{orcid}" target="_blank" title="ORCID iD: {orcid}"><img src="https://orcid.org/sites/default/files/images/orcid_16x16.png" alt="ORCID iD" style="vertical-align: middle; width: 16px; height: 16px; margin-left: 4px;" /></a>'
            
            md_lines.append(f"* **{name_str}**{orcid_html} – {pos_str}")
        
        md_lines.append("")
        md_lines.append("---")
        md_lines.append("")

md_lines.extend([
    "## 🏛️ Sister Research Groups",
    "",
    "HADES collaborates closely within the HPES laboratory with its sister research groups:",
    "",
    "- [**SODES**](https://www.bsc.es/discover-bsc/organisation/research-structure/software-dependability-embedded-systems-sodes) – SOftware Dependability for Embedded Systems",
    "- [**AIDES**](https://www.bsc.es/discover-bsc/organisation/research-structure/applications-intelligent-dependable-embedded-systems) – Applications for Intelligent Dependable Embedded Systems",
    "",
    "---",
    "",
    "## 📍 Contact & Location",
    "",
    "- **Location**: Barcelona Supercomputing Center (BSC-CNS)",
    "- **Address**: Plaça Eusebi Güell, 1-3, 08034 Barcelona, Spain",
    "- **Official Webpage**: [BSC HADES Team Directory](https://www.bsc.es/discover-bsc/organisation/research-structure/hardware-dependability-embedded-systems-hades/team-people)",
    ""
])

with open(md_path, "w", encoding="utf-8") as f:
    f.write("\n".join(md_lines))

print(f"Generated {md_path} from {csv_path}")
