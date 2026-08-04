# Crypto Core IP

High-performance cryptographic accelerator supporting SystemVerilog and VHDL integrations.

## Instantiation Examples

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
