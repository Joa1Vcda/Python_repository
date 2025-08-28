"""mutable or immutable data"""

name = "luiz"
name = "João Vitor"
print(name)

list_a = ["João", "Sophia", "Lucas"]
list_b = list_a
list_c = list_a.copy()

list_a.pop(-1)
print(list_b)
print(list_c)

"""'for in in lists"""

list = ["João", "Sophia"]
for nome in list:
    print(nome)

indexes = range(len(list))

for index in indexes:
    print(f"index: {index},item: {list[index]}")

i = 0
while i < len(list):
    print(f"index: {i},item: {list[i]}")
    i += 1
