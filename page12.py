"""logical operators"""

# and - all conditions need to be true
# or - need at least one condition true
# not - one condition have your logical inverted,ex:one false condition becomes true and vice versa with the presence od this operator
"""and"""

correctpassword = 123456
access = input("do you wanna entry in the system?[E] to entry and [S] for exit")
passw = input("digit the password of the system: ")

if access == "E" and passw == correctpassword:
    print("access permited,welcome to the system")
elif access == "E" and passw != correctpassword:
    print("access denied,incorret password")
else:
    print("exiting...")

"""or"""
door = input("do you wanna entry or exit? ")

if door == "entry" or door == "i wanna entry":
    print("You entrered in the system")
elif door == "exit" or door == "i wanna exit":
    print("You exited of the system")
else:
    print("you need to digit entry or exit")
    door_2 = input("do you wanna entry or exit? ")
    if door_2 == "entry":
        print("You entrered in the system")
    elif door_2 == "exit":
        print("You exited of the system")
