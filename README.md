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

## 👥 Updating the Team Roster

The HADES team directory ([`docs/team.md`](docs/team.md)) is generated from the structured dataset in [`docs/team.csv`](docs/team.csv).

If you are a new member of HADES or need to update your details:

1. Open [`docs/team.csv`](docs/team.csv).
2. Add a new row (or update your existing entry) with the following fields:
   - **`name`**: Full Name
   - **`category`**: Select one of: `Group Leader`, `Senior Staff`, `Early Career Researchers`, `Research Engineers`, or `Visitors & External Collaborators`
   - **`position`**: Your role / title (e.g., *Junior Research Engineer*)
   - **`email`**: Your BSC email address
   - **`orcid`**: Your full ORCID URL (e.g. `https://orcid.org/0000-0001-9751-1058`). Leave blank if you do not have one.
3. If an ORCID URL is present, a small clickable ORCID logo icon will automatically appear next to your name on the team page!

> 💡 **Automatic Generation**:
> - **In GitLab CI/CD**: The website pipeline automatically runs `python scripts/generate_team.py` on every push, so editing `docs/team.csv` is all you need to do!
> - **In Local Development**: Run `python scripts/generate_team.py` to update `docs/team.md` locally before previewing.

---

## 📦 Deployment & CI/CD


The website is configured for automatic deployment using **GitLab Pages**:

- **CI/CD Configuration**: Defined in [`.gitlab-ci.yml`](.gitlab-ci.yml).
- **Deployment Pipeline**: Every commit pushed to the `main` branch automatically triggers the pipeline, building the documentation and deploying it to GitLab Pages.
- **Live URL**: `http://caos_hw.gitlab-pages.bsc.es/hades_webpage/`