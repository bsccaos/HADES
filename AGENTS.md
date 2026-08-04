# Material for MkDocs - Hardware Lab Website Context

## Overview
Material for MkDocs is a highly popular, open-source theme built on MkDocs (a Python static site generator). It converts Markdown into a professional, responsive documentation site. It features built-in client-side search, rich content formatting, and automated syntax highlighting.

## 1. Project Folder Structure
A recommended directory structure for a hardware research lab (SoCs, IPs, Software, and Team):

```text
my-lab-website/
├── mkdocs.yml              # The main configuration file
└── docs/
    ├── index.md            # Lab homepage (mission, news)
    ├── team.md             # PIs, postdocs, PhD students
    ├── publications.md     # Papers and journals
    ├── socs/
    │   ├── index.md        # Overview of lab's SoCs
    │   └── chip_alpha.md   # Specific documentation for Chip Alpha
    ├── ips/
    │   ├── index.md        # Overview of hardware IPs
    │   ├── alu_v2.md       # Docs for your ALU IP
    │   └── crypto_core.md  # Docs for your Crypto Accelerator
    └── software/
        ├── driver_api.md   # Software drivers for your chips
        └── compilers.md    # Custom tools or compilers
```

## 2. Configuration (`mkdocs.yml`)
This configuration enables the specific Markdown extensions required for documenting hardware (tables, admonitions, code tabs, and math support).

```yaml
site_name: Advanced Hardware Architectures Lab
site_description: Research in SoCs, Hardware IPs, and Systems Software
site_author: "Your Name/Lab Group"

theme:
  name: material
  features:
    - navigation.tabs
    - navigation.indexes
    - toc.integrate
    - search.suggest
  palette:
    - scheme: default
      primary: indigo
      accent: deep purple

nav:
  - Home: index.md
  - Our Team: team.md
  - Publications: publications.md
  - Systems on Chip (SoCs):
      - Overview: socs/index.md
      - Chip Alpha: socs/chip_alpha.md
  - Hardware IPs:
      - Overview: ips/index.md
      - ALU v2: ips/alu_v2.md
      - Crypto Core: ips/crypto_core.md
  - Software & Tools:
      - API Drivers: software/driver_api.md
      - Compilers: software/compilers.md

markdown_extensions:
  - admonition
  - pymdownx.details
  - pymdownx.superfences
  - pymdownx.tabbed
  - tables
  - pymdownx.arithmatex:
      generic: true
```

## 3. Hardware Documentation Markdown Patterns

### Pinout & Specs Tables
```markdown
| Pin Name | Direction | Width | Description |
|----------|-----------|-------|-------------|
| `clk`    | Input     | 1     | System clock (100MHz) |
| `rst_n`  | Input     | 1     | Active-low asynchronous reset |
| `data_i` | Input     | 32    | Data input bus |
```

### Safety & Design Constraint Warnings (Admonitions)
```markdown
!!! danger "Voltage Limit"
    Do not exceed **1.2V** on the `VDD_CORE` rail. Doing so will cause permanent electromigration damage to the SoC.

!!! note "Clock Gating"
    This IP block features automatic clock gating when `enable_i` is held low for more than 5 cycles.
```

### Synchronized Code Tabs (HDL / Software)
```markdown
=== "SystemVerilog"
    ```verilog
    crypto_core #(
        .KEY_WIDTH(256)
    ) u_crypto (
        .clk(clk),
        .rst_n(rst_n)
    );
    ```

=== "VHDL"
    ```vhdl
    u_crypto : entity work.crypto_core
        generic map (
            KEY_WIDTH => 256
        )
        port map (
            clk => clk,
            rst_n => rst_n
        );
    ```
```

## 4. Automated Deployment via GitHub Pages

GitHub Pages will automatically host the lab website for free.

**Workflow File Path:** `.github/workflows/publish.yml`

**Workflow Code:**
```yaml
name: publish site
on:
  push:
    branches:
      - main
permissions:
  contents: write
jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: 3.x
      - run: pip install mkdocs-material
      - run: mkdocs gh-deploy --force
```

**Deployment Steps:**
1. Commit and push the `.github/workflows/publish.yml` file to the `main` branch.
2. In the GitHub Repository, navigate to **Settings** > **Pages**.
3. Under "Build and deployment", set the **Source** to **Deploy from a branch**.
4. Select the `gh-pages` branch. The site will be live at `https://<username>.github.io/<repo-name>/`.
