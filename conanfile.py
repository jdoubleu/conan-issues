from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain


class ConanQmlBugRecipe(ConanFile):
    name = "ConanQmlBug"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("qt/6.8.3", options={
            # qt quick/qml
            'qtdeclarative': True,
            'qtshadertools': True
        })

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
