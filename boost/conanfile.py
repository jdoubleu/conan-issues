from conan import ConanFile


class BoostUsageConan(ConanFile):
    name = "boost-usage"
    settings = "os", "compiler", "build_type", "arch"

    def requirements(self):
        self.requires("boost/1.91.0", options={
            'shared': True,
        })
