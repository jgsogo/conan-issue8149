from conans import ConanFile

class Recipe(ConanFile):
    name = "libE"
    settings = "os", "arch", "compiler", "build_type"

    def requirements(self):
        if self.version == "1.1.2":
            self.requires("libG/1.1.1")
