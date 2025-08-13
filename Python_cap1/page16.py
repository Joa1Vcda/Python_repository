"""try and except"""

print(1234)
print(456)
int("a")

numero_str = input("enter a number you want to double: ")

"""
testing = numero_str.isdigit()
# if testing:
#     numero_float = float(numero_str)
#     input(f"the double of your number is {numero_float*2:.2f}")
# else:
#     print("please type a digit,letter's or symbols not is permited")
"""

try:
    numero_float = float(numero_str)
    input(f"the double of your number is {numero_float*2:.2f}")
except:
    print("please type a digit", "letter's or symbols is not permited", sep="---")
