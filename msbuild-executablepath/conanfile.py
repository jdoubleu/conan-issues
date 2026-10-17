from conan import ConanFile
from conan.tools.microsoft import vs_layout, MSBuildDeps


class ConanQmlBugRecipe(ConanFile):
    name = "MSBuildExecutablePath"
    settings = "os", "compiler", "build_type", "arch"

    def layout(self):
        vs_layout(self)

    def requirements(self):
        # uses CMake as transitive dependency
        self.requires("wil/1.0.260126.7")

    def generate(self):
        deps = MSBuildDeps(self)
        deps.generate()
