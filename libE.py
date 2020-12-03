from conans import ConanFile

class Recipe(ConanFile):
    name = "libE"
    settings = "os", "arch", "compiler", "build_type"

    requires = "libG/1.1.1"
