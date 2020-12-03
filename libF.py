from conans import ConanFile

class Recipe(ConanFile):
    name = "libF"
    settings = "os", "arch", "compiler", "build_type"

    requires = "libG/1.1.2"
