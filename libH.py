from conans import ConanFile

class Recipe(ConanFile):
    name = "libH"
    settings = "os", "arch", "compiler", "build_type"
