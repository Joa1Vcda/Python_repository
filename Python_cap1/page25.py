"""enumerate"""

list_a = ["João", "Sophia", "Mateus", "Nicolas"]
list_a.append("Lucas")

enumerated_list = list(enumerate(list_a))
# print(next(enumerated_list))
print(enumerated_list)
for itens in enumerated_list:
    print(itens)

for index, name in enumerated_list:
    print(index, name)
