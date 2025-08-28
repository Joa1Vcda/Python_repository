"""Packaging and unpacking in python"""

names = ["João", "Pedro", "Lucas", "Enzo"]
name_1, name_2, name_3, name_4 = names
print(name_1)
print(name_2)

name_1, name_2, name_3, name_4 = ["João", "Pedro", "Lucas", "Enzo"]
print(name_1)
print(name_2)

name_1, *_ = ["João", "Pedro", "Lucas", "Enzo"]
print(name_1)

_, _, name_1, *_ = ["João", "Pedro", "Lucas", "Enzo"]
print(name_1)
