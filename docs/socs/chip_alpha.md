# Chip Alpha Documentation

Chip Alpha is a quad-core 64-bit RISC-V SoC with integrated hardware security and PMU components.

## Pinout & Interface Specifications

| Pin Name | Direction | Width | Description |
|----------|-----------|-------|-------------|
| `clk`    | Input     | 1     | System clock (100MHz) |
| `rst_n`  | Input     | 1     | Active-low asynchronous reset |
| `data_i` | Input     | 32    | Data input bus |
| `data_o` | Output    | 32    | Data output bus |

## Operating Constraints

!!! danger "Voltage Limit"
    Do not exceed **1.2V** on the `VDD_CORE` rail. Doing so will cause permanent electromigration damage to the SoC.

!!! note "Clock Gating"
    This IP block features automatic clock gating when `enable_i` is held low for more than 5 cycles.
