"""
SETUP v.O.1
Programme qui affiche le setup de la machine python
Changelog:
-dec 19: initialisation
"""
import sys
import os
import datetime


def printseparator():

    print("~" * 50)


a = "Bonjour Monde!"
print(a)  # j'affiche l'objet a
printseparator()
# print(sys.executable)
# print(sys.platform)
# print(sys.path)


print(sys.version_info)
v = sys.version_info
print(type(v))  # type de sys
print(dir(v))  # introspection de sys

print(f"Python version {v.major}.{v.minor}.{v.micro}")
# print("Python version {}.{}.{}".format(v.major, v.minor, v.micro))
# print("Python version %s.%s.%s" % (v.major, v.minor, v.micro)) #Version 2.7, déprécié


printseparator()
print("Environnement PythonPath :" + os.getenv("PYTHONPATH", "Vide"))

printseparator()
print(datetime)
print(datetime.__file__)

dt = datetime.datetime.now()
print(f"Date et Heure {dt} - Année {dt.year}")

printseparator()

help(printseparator)
