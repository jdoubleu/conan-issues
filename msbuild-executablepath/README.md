# MSBuildDeps ExecutablePath
Reproduces an issue with CMake as transitive dependency when using the [MSBuildDeps](https://docs.conan.io/2/reference/tools/microsoft/msbuilddeps.html) generator.

## Reproduce
Install Conan dependencies using the local profile:
```sh
conan install --profile:all .\Profile --build=missing .
```

You may have to clear your local conan cache, to force some dependencies to be re-built correctly:
```sh
conan remove --confirm '*:*'
```