from conan import ConanFile
from conan.tools.cmake import CMakeDeps, CMakeToolchain


class ConanQmlBugRecipe(ConanFile):
    name = "ConanQmlBug"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("qt/6.11.1", options={
            'shared': True,
            # qt quick/qml
            'qtdeclarative': True,
            'qtshadertools': True
        })

    def generate(self):
        deps = CMakeDeps(self)
        deps.generate()
        tc = CMakeToolchain(self)
        tc.generate()
