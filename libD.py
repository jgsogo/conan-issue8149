from conans import ConanFile

class Recipe(ConanFile):
    name = "libD"
    settings = "os", "arch", "compiler", "build_type"

    def requirements(self):
        if self.version == "1.1.2":
            self.requires("libE/1.1.2")
            self.requires("libF/1.1.2")
