"""for in python"""

Name = "João Vitor"
new_name = ""
for letra in Name:
    new_name += letra
print(new_name)

for i in range(10):
    if i == 2:
        print("i is 2,jumping...")
        continue

    if i == 8:
        print("your else will not complete")
        break

    for j in range(1, 3):
        print(i, j)

else:
    print("completed")

# """range"""

# number = range(0, 10, 1)
# for number_1 in number:
#     print(number_1)

# """methods"""
# i = 0
# name = "João Vitor"
# iterator = iter("João Vitor")  # iterator
# new_name = ""


# while i < len(name):
#     try:
#         new_name += next(iterator)
#     except StopIteration:
#         print(new_name)
#         break

# # for letters in name:
# #     new_name += next(iterator)
# # print(new_name)
