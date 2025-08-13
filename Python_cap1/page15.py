"""fourth test"""

import sys

name = input("Enter your name: ")
if name:
    idade = input("Enter your years old: ")
else:
    print("NAME NOT ENTERED,TRY AGAIN LATER")
    sys.exit()
if idade:
    print(f"your name is: {name}")
    print(f"your inveted name is: {name[::-1]}")
    if (" ") in name:
        print(f"{name} countain space's")
    else:
        print(f"{name} dont countain space's")
    print(f"your name ({name}) countain {len(name)} strings")
    print(f"the first letter of your name is: {name[0]}")
    print(f"and the last letter of your name is: {name[len(name)-1:len(name)]}")
else:
    print("YEARS OLD NOT ENTERED,TRY AGAIN")
