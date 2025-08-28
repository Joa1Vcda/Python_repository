"""class 2 of lists in python"""

import sys

list = [10, 20, 30, 40]
number = list[3]
print(number)
tester = ""
# list[2] = 300
# del list[2]
# print(list)
# print(list[2])
while not isinstance(tester, int):
    create = input("enter a int number which you want to add to the list: ")
    try:
        int_list = int(create)
        tester = int_list
        list.append(int_list)
    except:
        print("Enter a int number,try again")

print(list)
remover = list.pop(-2)
print(list)
print(f"the value in which has been removed {remover}")
