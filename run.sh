set -x

conan create libH.py libH/1.1.1@
conan create libH.py libH/1.1.2@

conan create libG.py libG/1.1.1@
conan create libG.py libG/1.1.2@

conan create libE.py libE/1.1.1@
conan create libE.py libE/1.1.2@

conan create libF.py libF/1.1.1@
conan create libF.py libF/1.1.2@

conan create libD.py "libD/1.1.2@"
conan create libDalt.py "libD/1.1.2@"
