"""fifth test"""

number = input("enter a int number: ")
try:
    number_int = int(number)
    if number_int % 2:
        print(f"this number ({number_int}) is odd")
    elif number_int % 2 == False:
        print(f"this number ({number_int}) is even")
except:
    print("plese,try a int number")

hours = input("enter the corresponding hours: ")
try:
    hours_int = int(hours)
    if hours_int >= 0 and hours_int <= 11:
        print("good morning")
    elif hours_int >= 12 and hours_int <= 17:
        print("good afternoon")
    elif hours_int >= 18 and hours_int <= 23:
        print("good evenig")
    else:
        print("please,try a number between 0-24")
except:
    print("please,entry a int number")

name = input("enter your name: ")

if len(name) > 0 and len(name) <= 4:
    print("your name is short")
elif len(name) >= 5 and len(name) <= 6:
    print("your name is medium")
elif len(name) > 6:
    print("your name is big")
else:
    print("Enter at least one letter")
