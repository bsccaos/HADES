# Compilers & Toolchains

Custom LLVM pass and GCC toolchain configurations for HADES SoC extensions.

## Toolchain Build Instructions

```bash
git clone https://github.com/bsccaos/HADES.git
cd HADES
# Build custom LLVM back-end target
mkdir build && cd build
cmake -G Ninja -DLLVM_ENABLE_PROJECTS="clang" ../llvm
ninja
```
