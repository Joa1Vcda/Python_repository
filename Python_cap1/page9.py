"""if/elif/else(conditions)"""

condition = True

"""
if condition:
    print('Condition is True')
else:
    print('The Condition is False')
"""

door = input("do you wanna entry or exit? ")

if door == "entry":
    print("You entrered in the system")
elif door == "exit":
    print("You exited of the system")
else:
    print("you need to digit entry or exit")
    door_2 = input("do you wanna entry or exit? ")
    if door_2 == "entry":
        print("You entrered in the system")
    elif door_2 == "exit":
        print("You exited of the system")
