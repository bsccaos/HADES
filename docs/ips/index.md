# Hardware IPs

The HADES research group develops a suite of open-source Register Transfer Level (RTL) IP cores designed for timing verification, fault-tolerance, diversity monitoring, and safety-critical execution in high-performance embedded systems across space, automotive, and railway domains.

---

## 🛡️ Featured Hardware IP Cores

### 1. SafeSU – Safe Statistics Unit
The **Safe Statistics Unit (SafeSU)** is an RTL IP core that implements advanced mechanisms for multicore timing interference verification, validation, and monitoring. SafeSU has been integrated and validated in commercial space-grade RISC-V and SPARCv8 MPSoCs.

- **DOI / Publications**: [10.1109/ETS50041.2021.9465444](https://doi.org/10.1109/ETS50041.2021.9465444) | [10.23919/DATE54114.2022.9774515](https://doi.org/10.23919/DATE54114.2022.9774515)
- **Repository**: [bsc-loca/SafeSU](https://github.com/bsc-loca/SafeSU/)

---

### 2. SafeTI – Safe Traffic Injector
The **Safe Traffic Injector (SafeTI)** unit acts as an AHB Master IP connected to the main AMBA bus. Controlled via APB registers, SafeTI performs a controlled set of bus transactions to AHB Slave RAM memory based on data descriptors configured at startup. It allows researchers to generate controlled bus traffic and measure multicore interference alongside processing cores and monitoring units.

- **DOI / Publications**: [10.1109/IOLTS52814.2021.9486689](https://doi.org/10.1109/IOLTS52814.2021.9486689)
- **Repository**: [bsc-loca/SafeTI](https://github.com/bsc-loca/SafeTI/)

---

### 3. SafeDE – Safe Diversity Enforcer
The **Safe Diversity Enforcer (SafeDE)** hardware module provides light-lockstep support using a non-intrusive and flexible hardware core. It preserves time staggering across cores running redundant threads, bringing enforced temporal diversity to avoid common cause failures (CCFs) in safety-critical systems.

- **DOI / Publications**: [10.1109/TDMR.2022.3156799](https://doi.org/10.1109/TDMR.2022.3156799) | [10.1109/IOLTS52814.2021.9486715](http://dx.doi.org/10.1109/IOLTS52814.2021.9486715)
- **Repository**: [bsc-loca/SafeDE](https://github.com/bsc-loca/SafeDE/)

---

### 4. SafeDM – Safe Diversity Measurer
The **Safe Diversity Measurer (SafeDM)** is a dedicated hardware module that continuously monitors runtime execution diversity between two redundant processors executing redundant tasks.

- **DOI / Publications**: [10.23919/DATE54114.2022.9774540](https://doi.org/10.23919/DATE54114.2022.9774540)
- **Repository**: [bsc-loca/SafeDM](https://github.com/bsc-loca/SafeDM)

---

### 5. SafeLS – Safe Lockstep Core
The **Safe Lockstep (SafeLS)** unit is an open-source RISC-V lockstep core based on Frontgrade Gaisler AB's NOEL-V core tailored for the space domain. SafeLS has been integrated into the FPGA-synthesizable [SELENE SoC](https://gitlab.com/selene-riscv-platform/selene-hardware) platform, successfully assessed against space, automotive, and railway safety standards.

- **DOI / Publications**: [10.1109/IOLTS59296.2023.10224867](https://doi.org/10.1109/IOLTS59296.2023.10224867)
- **Repository**: [bsc-loca/SafeLS](https://github.com/bsc-loca/SafeLS)

---

### 6. SAURIA – DRAC Automotive Accelerator
**SAURIA** is a Convolutional Neural Network (CNN) hardware accelerator module based on a 2D systolic array architecture with on-chip convolutional mapping, written in SystemVerilog. Developed as part of the DRAC project, it targets a 22 nm ASIC implementation for automotive deep learning workloads.

- **Repository**: [bsc-loca/sauria](https://github.com/bsc-loca/sauria)
