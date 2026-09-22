# Software & Tools

The HADES research group develops specialized software libraries, compiler toolchains, and runtime environments to support fault tolerance, real-time predictability, and software-level diverse redundancy on high-performance embedded systems.

---

## 💻 Software Libraries & Tooling

### 1. SafeSoftDR – Safe Software Diverse Redundancy Library
The **Safe Software Diverse Redundancy library (SafeSoftDR)** provides programmers with a structured software interface to enable software diverse redundant execution within user-defined functions. SafeSoftDR allows critical embedded software applications to achieve fault tolerance and time/algorithmic diversity across processing cores without requiring dedicated hardware redundancy.

- **DOI / Preprints**: [arXiv:2210.00833](https://doi.org/10.48550/arXiv.2210.00833)
- **Repository**: [bsc-loca/SafeSoftDR](https://github.com/bsc-loca/SafeSoftDR)

??? info "📥 Export Citation (BibTeX)"

    **arXiv Preprint 2022**: [Download .bib File](https://api.crossref.org/works/10.48550/arXiv.2210.00833/transform/application/x-bibtex)
    ```bibtex
    @misc{Mazzocchetti_2022_SafeSoftDR,
      title={SafeSoftDR: A Library to Enable Software-based Diverse Redundancy for Safety-Critical Tasks},
      author={Mazzocchetti, Fabio and Alcaide, Sergi and Bas, Francisco and Benedicte, Pedro and Cabo, Guillem and Chang, Feng and Fuentes, Francisco and Abella, Jaume},
      year={2022},
      publisher={arXiv},
      doi={10.48550/arXiv.2210.00833},
      url={https://arxiv.org/abs/2210.00833}
    }
    ```

---

### 2. Dependable Real-Time Software Frameworks
- **Multicore Interference Accounting**: Software drivers and low-level runtime integration for hardware monitoring units (e.g. SafeSU and SafeTI).
- **GPU & SYCL Tooling for Critical Systems**: Compiler extensions and runtime environments for deterministic, safety-compliant GPU acceleration in automotive and avionics workloads.
