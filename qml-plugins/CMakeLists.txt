cmake_minimum_required(VERSION 3.15)
project(ConanQmlBug CXX)

set(CMAKE_CXX_STANDARD 17)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

find_package(Qt6 6.11 REQUIRED COMPONENTS Core Gui Qml Quick QuickControls2)

qt_policy(set QTP0001 NEW)
qt_policy(set QTP0004 NEW)

qt_standard_project_setup()

qt_add_executable(helloworld
    src/main.cpp
)

qt_add_qml_module(helloworld
    URI hello
    QML_FILES
        src/Main.qml
)

target_link_libraries(helloworld PRIVATE
    Qt6::Core
    Qt6::Gui
    Qt6::Qml
    Qt6::Quick
    Qt6::QuickControls2)