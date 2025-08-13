import sys

"""operators in & not in"""

name = "João Vitor"

"""  
print(name[4])
print(name[-6])

print(" " in name)
print("p" in name)

print(" " not in name)
print("p" not in name)
"""
seacher = input(f"send a part in which you want to find in {name}: ")
if seacher in name:
    print(f"the part you type ({seacher}) is in the{name}")
elif seacher not in name:
    print(f"the part you type ({seacher}) is not in the {name}")


correct_login = "main@gmail.com"
correct_login2 = "secundary@gmail.com"
correct_passw = "123456"


login = input("Enter the username: ")

if login in (correct_login, correct_login2):
    passw = input("Enter the password: ")
elif login not in (correct_login, correct_login2):
    print("Incorret username,exiting...")
    sys.exit()

if passw not in (correct_passw):
    print("Incorrect password,try again later")
elif not passw:
    print("Nothing entered,try again later")
else:
    print("access garanted sucefully")
