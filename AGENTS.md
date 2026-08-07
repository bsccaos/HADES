# AGENTS.md

## Agent Instructions & Commit Policy

### ⚠️ Git Commit and Push Directive
- **ALWAYS ask for explicit user confirmation before executing any `git commit` or `git push`**.
- Always perform build and test tasks locally first so the user can review changes locally (`python -m mkdocs build` and `python -m mkdocs serve`).
- Do NOT auto-commit or auto-push changes under any circumstances without first asking and receiving user approval.

---

## 📋 Completed Tasks Log

1. **Repository Setup & Cloning**
   - Cloned remote repository `bsccaos/HADES` locally into `C:\Users\bscuser\Documents\Repos\HADES`.
   - Configured `site_url: https://bsccaos.github.io/HADES/` in [`mkdocs.yml`](file:///C:/Users/bscuser/Documents/Repos/HADES/mkdocs.yml).
   - Created GitHub Actions workflow in [`.github/workflows/publish.yml`](file:///C:/Users/bscuser/Documents/Repos/HADES/.github/workflows/publish.yml).

2. **Homepage Content (`docs/index.md`)**
   - Extracted official BSC HADES description, research directions, lab affiliations, and contact details.

3. **Team Roster Update (`docs/team.md`)**
   - Corrected sister research groups to **SODES** and **TAIES** only.
   - Extracted and populated all **28 team members** across all 3 pages (`page=0`, `page=1`, `page=2`).
   - Added **Senior Staff** section right after Group Leader (Feng Chang, Ivan Rodriguez Ferrandez, Ramon Canal, Juan Carlos Rodriguez Rivas, Matina Maria Trompouki, Sergi Alcaide).

4. **Publications Extraction (`docs/publications.md`)**
   - Extracted **all 298 publications** across all 10 pages (`page=0` to `page=9`) from the official BSC HADES publications repository.
   - Added complete **Authors**, **Venue/Journal names**, paper **Titles**, and direct repository links.
   - Verified clean local compilation via `python -m mkdocs build`.
