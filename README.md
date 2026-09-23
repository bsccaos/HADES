# HADES – HArdware Dependability for Embedded Systems

Welcome to the documentation repository for the **HArdware Dependability for Embedded Systems (HADES)** research group at the **Barcelona Supercomputing Center (BSC-CNS)**.

This repository powers the official HADES website, presenting our research directions, team roster, publications, Systems on Chip (SoCs), Hardware IPs, and Software tools.

---

## 🚀 Local Development & Preview

This website is built using [MkDocs](https://www.mkdocs.org/) with the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

### Prerequisites

Ensure you have Python 3.10 or higher installed.

### 1. Install Dependencies

Install MkDocs and the Material theme:

```bash
pip install mkdocs-material
```

### 2. Build the Site Locally

To verify that the documentation compiles cleanly without errors:

```bash
python -m mkdocs build
```

This generates the compiled static website inside the `site/` folder.

### 3. Run the Development Server

To preview the website live in your browser with automatic hot-reloading:

```bash
python -m mkdocs serve
```

Open your browser and navigate to:  
👉 **`http://127.0.0.1:8000/`**

---

## 🤖 Working with AI Agents

If you are using an AI coding assistant (such as Antigravity, Claude, ChatGPT, etc.) to modify or expand this codebase, follow these instructions to ensure smooth collaboration:

### 1. Instruct the Agent to Read `AGENTS.md`

Always instruct the AI agent to read [`AGENTS.md`](AGENTS.md) at the start of any conversation.

**Example Prompt for AI Agent:**
> *"Please read the `AGENTS.md` file to understand the project context, completed tasks, and git commit directives before making any changes."*

### 2. AI Commit & Testing Policies

The [`AGENTS.md`](AGENTS.md) file enforces the following guidelines for AI assistants:

- **Local Verification First**: The AI must always test changes locally using `python -m mkdocs build` before asking to commit or push.
- **Explicit Confirmation**: The AI is **never allowed** to execute `git commit` or `git push` automatically without receiving your explicit user confirmation first.
- **Documentation Preservation**: Maintain docstrings, links, and structure integrity across all pages.

### 3. Managing Pending Tasks

All **pending tasks** and **completed tasks** are tracked and logged directly inside [`AGENTS.md`](AGENTS.md).

- **Finding Work to Do**: Check the **📌 Pending Tasks** section in [`AGENTS.md`](AGENTS.md) to see planned features, documentation updates, and technical tasks.
- **Adding New Tasks**: If you or a team member want to plan new work, add the task items to [`AGENTS.md`](AGENTS.md) so all human contributors and AI agents remain synchronized.


---

## 📊 Managing Content via CSV Datasets

The HADES documentation site uses structured CSV files to manage dynamic content:

1. **Team Directory** ([`docs/team.csv`](docs/team.csv) ➔ `docs/team.md`):
   - Edit [`docs/team.csv`](docs/team.csv) to add or update team members, roles, emails, and ORCID URLs.
2. **Hardware IPs** ([`docs/ips.csv`](docs/ips.csv) ➔ `docs/ips/index.md`):
   - Edit [`docs/ips.csv`](docs/ips.csv) to add hardware components, descriptions, DOIs, and repository links.
3. **Software & Tools** ([`docs/software.csv`](docs/software.csv) ➔ `docs/software/index.md`):
   - Edit [`docs/software.csv`](docs/software.csv) to add software tools, preprints/DOIs, and repository links.

> 💡 **Automated Pipeline**:
> - **In GitLab CI/CD**: The pipeline automatically runs `python scripts/generate_team.py`, `python scripts/generate_ips.py`, and `python scripts/generate_software.py` on every push. You only need to edit the CSV files!
> - **In Local Development**: Run `python scripts/generate_ips.py` or `python scripts/generate_software.py` to regenerate the pages locally before previewing.

---

## 📦 Deployment & CI/CD


The website is configured for automatic deployment using **GitLab Pages**:

- **CI/CD Configuration**: Defined in [`.gitlab-ci.yml`](.gitlab-ci.yml).
- **Deployment Pipeline**: Every commit pushed to the `main` branch automatically triggers the pipeline, building the documentation and deploying it to GitLab Pages.
- **Live URL**: `http://caos_hw.gitlab-pages.bsc.es/hades_webpage/`