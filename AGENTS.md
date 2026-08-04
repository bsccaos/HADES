# AGENTS.md

## Agent Instructions & Commit Policy

### ⚠️ Git Commit and Push Directive
- **Do NOT ask to git commit or git push by default**.
- Always perform build and test tasks locally first so the user can review changes locally (`python -m mkdocs build` and `python -m mkdocs serve`).
- Only execute `git commit` or `git push` when explicitly commanded by the user.

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
   - Extracted and populated all **28 team members** across all 3 pages (`page=0`, `page=1`, `page=2`):
     - **Group Leader**: Leonidas Kosmidis
     - **Researchers (9)**: Feng Chang, Ivan Rodriguez Ferrandez, Ramon Canal, Ahlame El Afghani, Francisco Javier Fuentes Diaz, Iker Fernandez Andonegui, Ilham Lasfar, Jeremy Jens Giesen Leon, Marc Sole Bonet.
     - **Engineers (14)**: Juan Carlos Rodriguez Rivas, Matina Maria Trompouki, Sergi Alcaide, Jannis Gunter Josef Wolf, Omar Alymlahi, Alvaro Jover Alvarez, Eric Rufart Blasco, Guillermo Vidal Sule, Isabel Peralta Gonzalez, Josue Pedrajas Perez, Marc Grau I Fornt, Pau Adell Raventos, Pau Lopez Castillon, Xavier Caricchio Hernandez.
     - **Visitors (4)**: Adam Sztamborski, Alfonso Martinez Conejo, Dan Joshua Hagen, Noah Perret.

4. **Publications Extraction (`docs/publications.md`)**
   - Extracted **all 298 publications** across all 10 pages (`page=0` to `page=9`) from the official BSC HADES publications repository.
   - Added complete **Authors**, **Venue/Journal names**, paper **Titles**, and direct repository links.
   - Verified clean local compilation via `python -m mkdocs build`.
