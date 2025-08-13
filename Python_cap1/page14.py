"basic string interpolation"

name = "João Vitor"
value = 87.9082547191
value_1 = -87.9082547191
number = 980
var = "%s,the value is %.2f" % (name, value)
print(var)
hexa = "%i is %X in hexadecimal" % (number, number)
print(hexa)

"""f-strings"""

var_1 = f"{name}, the value is {value:+.2f}"
print(var_1)

var_2 = f"{name}, the value is {value_1:-.2f}"
print(var_2)

print(f"{number} is {number:X} in hexadecimal")

print(f"{name: >10}.")
print(f"{name: <10}.")
print(f"{name:-^10}.")

"""slicing strings"""

name = "joão Vitor"
print(len(name))  # len si for count elements
print(name[:5])
print(name[5:10])
print(name[: len(name) : 2])
print(name[-1 : -len(name) : -2])
