# Conan + Qt (Quick) issues
This repository is meant to reproduce issues with the Qt (Quick) recipes from Conan, as well as explore possible fixes.

## Reproduce current issue
Simply run the following commands, as you would do with every Conan + CMake project:
```bash
conan install --output-folder=build --build=missing .
cmake --preset conan-default --fresh
```

### Output
You should now observe the following CMake warnings:
```
CMake Warning at <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Qml/Qt6QmlMacros.cmake:4813 (message):
  The qml plugin 'qtquick2plugin' is a dependency of 'helloworld', but the
  link target it defines (Qt6::qtquick2plugin) does not exist in the current
  scope.  The plugin will not be linked.
Call Stack (most recent call first):
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:818 (qt6_import_qml_plugins)
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:818 (cmake_language)
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:898 (_qt_internal_finalize_executable)
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:867:EVAL:1 (qt6_finalize_target)
  CMakeLists.txt:DEFERRED

CMake Warning at <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Qml/Qt6QmlMacros.cmake:4813 (message):
  The qml plugin 'qmlplugin' is a dependency of 'helloworld', but the link
  target it defines (Qt6::qmlplugin) does not exist in the current scope.
  The plugin will not be linked.
Call Stack (most recent call first):
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:818 (qt6_import_qml_plugins)
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:818 (cmake_language)
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:898 (_qt_internal_finalize_executable)
  <CONAN_HOME>/p/b/qt36e204f188e85/p/lib/cmake/Qt6Core/Qt6CoreMacros.cmake:867:EVAL:1 (qt6_finalize_target)
  CMakeLists.txt:DEFERRED

...
```

### Expected output
These issues do not appear, e.g. when using the official Qt distribution directly:
```bash
cmake -B build-qt -DCMAKE_PREFIX_PATH="C:\Qt\6.8.3\msvc2022_64" .
cmake --build build-qt
```