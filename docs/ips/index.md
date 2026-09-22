# Hardware IPs

The HADES research group develops a suite of open-source Register Transfer Level (RTL) IP cores designed for timing verification, fault-tolerance, diversity monitoring, and safety-critical execution in high-performance embedded systems across space, automotive, and railway domains.

---

## 🛡️ Featured Hardware IP Cores

### 1. SafeSU – Safe Statistics Unit
The **Safe Statistics Unit (SafeSU)** is an RTL IP core that implements advanced mechanisms for multicore timing interference verification, validation, and monitoring. SafeSU has been integrated and validated in commercial space-grade RISC-V and SPARCv8 MPSoCs.

- **DOI / Publications**: [10.1109/ETS50041.2021.9465444](https://doi.org/10.1109/ETS50041.2021.9465444) | [10.23919/DATE54114.2022.9774515](https://doi.org/10.23919/DATE54114.2022.9774515)
- **Repository**: [bsc-loca/SafeSU](https://github.com/bsc-loca/SafeSU/)

??? info "📥 Export Citation (BibTeX)"

    **IEEE ETS 2021**: [Download .bib File](https://api.crossref.org/works/10.1109/ETS50041.2021.9465444/transform/application/x-bibtex)
    ```bibtex
    @inproceedings{Cabo_2021_SafeSU,
      title={SafeSU: an Extended Statistics Unit for Multicore Timing Interference},
      author={Cabo, Guillem and Bas, Francisco and Lorenzo, Ruben and Trilla, David and Alcaide, Sergi and Moreto, Miquel and Hernandez, Carles and Abella, Jaume},
      booktitle={2021 IEEE European Test Symposium (ETS)},
      pages={1--4},
      year={2021},
      publisher={IEEE},
      doi={10.1109/ETS50041.2021.9465444}
    }
    ```

    **DATE 2022**: [Download .bib File](https://api.crossref.org/works/10.23919/DATE54114.2022.9774515/transform/application/x-bibtex)
    ```bibtex
    @inproceedings{Cabo_2022_SafeSU2,
      title={SafeSU-2: a Safe Statistics Unit for Space MPSoCs},
      author={Cabo, Guillem and Alcaide, Sergi and Hernandez, Carles and Benedicte, Pedro and Bas, Francisco and Mazzocchetti, Fabio and Abella, Jaume},
      booktitle={2022 Design, Automation & Test in Europe Conference & Exhibition (DATE)},
      pages={1085--1086},
      year={2022},
      publisher={IEEE},
      doi={10.23919/DATE54114.2022.9774515}
    }
    ```

---

### 2. SafeTI – Safe Traffic Injector
The **Safe Traffic Injector (SafeTI)** unit acts as an AHB Master IP connected to the main AMBA bus. Controlled via APB registers, SafeTI performs a controlled set of bus transactions to AHB Slave RAM memory based on data descriptors configured at startup. It allows researchers to generate controlled bus traffic and measure multicore interference alongside processing cores and monitoring units.

- **DOI / Publications**: [10.1109/IOLTS52814.2021.9486689](https://doi.org/10.1109/IOLTS52814.2021.9486689)
- **Repository**: [bsc-loca/SafeTI](https://github.com/bsc-loca/SafeTI/)

??? info "📥 Export Citation (BibTeX)"

    **IEEE IOLTS 2021**: [Download .bib File](https://api.crossref.org/works/10.1109/IOLTS52814.2021.9486689/transform/application/x-bibtex)
    ```bibtex
    @inproceedings{Sala_2021_SafeTI,
      title={SafeTI: a Hardware Traffic Injector for MPSoC Functional and Timing Validation},
      author={Sala, Oriol and Alcaide, Sergi and Cabo, Guillem and Bas, Francisco and Lorenzo, Ruben and Benedicte, Pedro and Trilla, David and Gil, Guillermo and Mazzocchetti, Fabio and Abella, Jaume},
      booktitle={2021 IEEE 27th International Symposium on On-Line Testing and Robust System Design (IOLTS)},
      pages={1--7},
      year={2021},
      publisher={IEEE},
      doi={10.1109/IOLTS52814.2021.9486689}
    }
    ```

---

### 3. SafeDE – Safe Diversity Enforcer
The **Safe Diversity Enforcer (SafeDE)** hardware module provides light-lockstep support using a non-intrusive and flexible hardware core. It preserves time staggering across cores running redundant threads, bringing enforced temporal diversity to avoid common cause failures (CCFs) in safety-critical systems.

- **DOI / Publications**: [10.1109/TDMR.2022.3156799](https://doi.org/10.1109/TDMR.2022.3156799) | [10.1109/IOLTS52814.2021.9486715](http://dx.doi.org/10.1109/IOLTS52814.2021.9486715)
- **Repository**: [bsc-loca/SafeDE](https://github.com/bsc-loca/SafeDE/)

??? info "📥 Export Citation (BibTeX)"

    **IEEE TDMR 2022**: [Download .bib File](https://api.crossref.org/works/10.1109/TDMR.2022.3156799/transform/application/x-bibtex)
    ```bibtex
    @article{Bas_2022_SafeDE_TDMR,
      title={SafeDE: A Low-Cost Hardware Solution to Enforce Diverse Redundancy in Multicores},
      author={Bas, Francisco and Alcaide, Sergi and Cabo, Guillem and Benedicte, Pedro and Abella, Jaume},
      journal={IEEE Transactions on Device and Materials Reliability},
      volume={22},
      number={2},
      pages={111--119},
      year={2022},
      publisher={IEEE},
      doi={10.1109/TDMR.2022.3156799}
    }
    ```

    **IEEE IOLTS 2021**: [Download .bib File](https://api.crossref.org/works/10.1109/IOLTS52814.2021.9486715/transform/application/x-bibtex)
    ```bibtex
    @inproceedings{Bas_2021_SafeDE_IOLTS,
      title={SafeDE: a flexible Diversity Enforcement hardware module for light-lockstepping},
      author={Bas, Francisco and Alcaide, Sergi and Lorenzo, Ruben and Cabo, Guillem and Gil, Guillermo and Sala, Oriol and Mazzocchetti, Fabio and Trilla, David and Abella, Jaume},
      booktitle={2021 IEEE 27th International Symposium on On-Line Testing and Robust System Design (IOLTS)},
      pages={1--7},
      year={2021},
      publisher={IEEE},
      doi={10.1109/IOLTS52814.2021.9486715}
    }
    ```

---

### 4. SafeDM – Safe Diversity Measurer
The **Safe Diversity Measurer (SafeDM)** is a dedicated hardware module that continuously monitors runtime execution diversity between two redundant processors executing redundant tasks.

- **DOI / Publications**: [10.23919/DATE54114.2022.9774540](https://doi.org/10.23919/DATE54114.2022.9774540)
- **Repository**: [bsc-loca/SafeDM](https://github.com/bsc-loca/SafeDM)

??? info "📥 Export Citation (BibTeX)"

    **DATE 2022**: [Download .bib File](https://api.crossref.org/works/10.23919/DATE54114.2022.9774540/transform/application/x-bibtex)
    ```bibtex
    @inproceedings{Bas_2022_SafeDM,
      title={SafeDM: a Hardware Diversity Monitor for Redundant Execution on Non-Lockstepped Cores},
      author={Bas, Francisco and Benedicte, Pedro and Alcaide, Sergi and Cabo, Guillem and Mazzocchetti, Fabio and Abella, Jaume},
      booktitle={2022 Design, Automation & Test in Europe Conference & Exhibition (DATE)},
      pages={358--363},
      year={2022},
      publisher={IEEE},
      doi={10.23919/DATE54114.2022.9774540}
    }
    ```

---

### 5. SafeLS – Safe Lockstep Core
The **Safe Lockstep (SafeLS)** unit is an open-source RISC-V lockstep core based on Frontgrade Gaisler AB's NOEL-V core tailored for the space domain. SafeLS has been integrated into the FPGA-synthesizable [SELENE SoC](https://gitlab.com/selene-riscv-platform/selene-hardware) platform, successfully assessed against space, automotive, and railway safety standards.

- **DOI / Publications**: [10.1109/IOLTS59296.2023.10224867](https://doi.org/10.1109/IOLTS59296.2023.10224867)
- **Repository**: [bsc-loca/SafeLS](https://github.com/bsc-loca/SafeLS)

??? info "📥 Export Citation (BibTeX)"

    **IEEE IOLTS 2023**: [Download .bib File](https://api.crossref.org/works/10.1109/IOLTS59296.2023.10224867/transform/application/x-bibtex)
    ```bibtex
    @inproceedings{Sarraseca_2023_SafeLS,
      title={SafeLS: An Open Source Implementation of a Lockstep NOEL-V RISC-V Core},
      author={Sarraseca, Marcel and Alcaide, Sergi and Fuentes, Francisco and Rodriguez, Juan Carlos and Chang, Feng and Lasfar, Ilham and Canal, Ramon and Cazorla, Francisco J. and Abella, Jaume},
      booktitle={2023 IEEE 29th International Symposium on On-Line Testing and Robust System Design (IOLTS)},
      pages={1--7},
      year={2023},
      publisher={IEEE},
      doi={10.1109/IOLTS59296.2023.10224867}
    }
    ```

---

### 6. SAURIA – DRAC Automotive Accelerator
**SAURIA** is a Convolutional Neural Network (CNN) hardware accelerator module based on a 2D systolic array architecture with on-chip convolutional mapping, written in SystemVerilog. Developed as part of the DRAC project, it targets a 22 nm ASIC implementation for automotive deep learning workloads.

- **DOI / Publications**: [10.1109/TVLSI.2023.3286122](https://doi.org/10.1109/TVLSI.2023.3286122)
- **Repository**: [bsc-loca/sauria](https://github.com/bsc-loca/sauria)

??? info "📥 Export Citation (BibTeX)"

    **IEEE TVLSI 2023**: [Download .bib File](https://api.crossref.org/works/10.1109/TVLSI.2023.3286122/transform/application/x-bibtex)
    ```bibtex
    @article{Fornt_2023_SAURIA,
      title={An Energy-Efficient GeMM-Based Convolution Accelerator With On-the-Fly im2col},
      author={Fornt, Jordi and Fontova-Must{\'e}, Pau and Caro, Mart{\'i} and Abella, Jaume and Moll, Francesc and Altet, Josep and Studer, Christoph},
      journal={IEEE Transactions on Very Large Scale Integration (VLSI) Systems},
      volume={31},
      number={11},
      pages={1874--1878},
      year={2023},
      publisher={IEEE},
      doi={10.1109/TVLSI.2023.3286122}
    }
    ```

