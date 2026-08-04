# ALU v2 IP Core

## Specifications

| Interface | Type | Width | Description |
|-----------|------|-------|-------------|
| `op_a`    | In   | 64    | Operand A |
| `op_b`    | In   | 64    | Operand B |
| `alu_op`  | In   | 4     | Operation code |
| `res`     | Out  | 64    | Result output |

!!! info "Pipelining"
    ALU v2 supports single-cycle throughput with 2-stage execution pipelined latency.
