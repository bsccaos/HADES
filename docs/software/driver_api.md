# Low-Level Driver APIs

Software interface specifications for controlling HADES IP cores and SoC components.

## C API Sample

```c
#include "hades_crypto.h"

int main(void) {
    crypto_init(CRYPTO_BASE_ADDR);
    crypto_encrypt_block(key, input_data, output_data);
    return 0;
}
```
