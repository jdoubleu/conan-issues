# Conan + Qt (Quick) issues
This repository is meant to reproduce an issue with Qt (Quick) and Conan, as well as explore possible fixes.

## Reproduce issue
Simply run the following commands, as you would do with every Conan + CMake project. This is assuming
```bash
conan install --output-folder=build --build=missing c tools.cmake.cmaketoolchain:generator=Ninja .
cmake --preset conan-debug
cmake --build --preset conan-debug
cmake --build --preset conan-debug --target all_qmllint
```

### Output
You should now observe the following warnings:
```
Warning: C:/path/to/project/src/Main.qml:1:1: Warnings occurred while importing module "QtQuick": [import]
import QtQuick
^^^^^^
---
Warning: 1:1: Failed to import QtQuick. Are your import paths set up properly? [import]
---
```

## Expected output
These issues do not appear, e.g. when using the official Qt distribution directly:
```bash
cmake -B build-qt -DCMAKE_PREFIX_PATH="C:\Qt\6.8.3\msvc2022_64" -G "Ninja" .
cmake --build build-qt
cmake --build build-qt --target all_qmllint
```