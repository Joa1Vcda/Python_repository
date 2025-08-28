"""Unpacking Positional Arguments"""

string = "ABC"
list_1 = ["Carlos", "Ricardo", "Daniel", "Maria", "Jéssica"]
tuple_1 = "Python", "is", "cool"

print(list_1)
print("Carlos", "Ricardo", "Daniel", "Maria", "Jéssica", sep="-")
print(*list_1, sep="-")
print(*tuple_1)
print(*string, sep="~")
