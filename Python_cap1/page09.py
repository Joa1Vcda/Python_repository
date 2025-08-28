import sys

"""logical operators"""
# and - all conditions need to be true
# or - need at least one condition true
# not - one condition have your logical inverted,ex:one false condition becomes true and vice versa with the presence od this operator

"""and"""

correctpassword = 123456

access = input("do you wanna entry in the system?[E] to entry and [S] for exit: ")

if access == "S" or access == "s":
    print("exiting...")
    sys.exit()

elif access == "e" or access == "E":
    passw = input("Enter the password of the system: ")

if access != "e" and access != "E":
    print("invalid comand,try E to entry or S to quit next time")
    sys.exit()

if passw == "":
    print("Nothing entered,try again later")
    sys.exit()

password = int(passw)

if access == "E" or access == "e" and password == correctpassword:
    print("access permited,welcome to the system")
elif access == "E" or access == "e" and password != correctpassword:
    print("access denied,incorret password")

"""or"""

door = input("do you wanna entry or exit? ")

if door == "entry" or door == "i wanna entry":
    print("You entrered in the system")
elif door == "exit" or door == "i wanna exit":
    print("You exited of the system")
else:
    print("you must enter entry or exit")
    door_2 = input("do you wanna entry or exit? ")
    if door_2 == "entry":
        print("You entrered in the system")
    elif door_2 == "exit":
        print("You exited of the system")

"""not"""

correctpassword = 123456

access = input("do you wanna entry in the system?[E] to entry and [S] for exit: ")

if access == "S" or access == "s":
    print("exiting...")
    sys.exit()

elif access == "e" or access == "E":
    passw = input("Enter the password of the system: ")

if access != "e" and access != "E":
    print("invalid comand,try E to entry or S to quit next time")
    sys.exit()

if not passw:
    print("Nothing entered,try again later")
    sys.exit()

password = int(passw)

if access == "E" or access == "e" and password == correctpassword:
    print("access permited,welcome to the system")
elif access == "E" or access == "e" and password != correctpassword:
    print("access denied,incorret password")
