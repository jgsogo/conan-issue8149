from conans import ConanFile

class Recipe(ConanFile):
    name = "libD"
    settings = "os", "arch", "compiler", "build_type"

    requires = "libE/1.1.1", "libF/1.1.1"
