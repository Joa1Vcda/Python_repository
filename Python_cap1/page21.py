"""test 6"""

# number = input("Enter a number: ")
# operator = input("Enter a operator: ")
# number_1 = input("Enter a second number: ")

while True:
    number = input("Enter a number: ")
    operator = input("Enter a operator: ")
    number_1 = input("Enter a second number: ")
    try:
        number_float = float(number)
        number_1_float = float(number_1)
        if operator == "+":
            sum = number_float + number_1_float
            print(sum)
        elif operator == "-":
            subtraction = number_float - number_1_float
            print(subtraction)
        elif operator == "/":
            division = number_float / number_1_float
            print(division)
        elif operator == "*":
            multiplication = number_float * number_1_float
            print(multiplication)
        else:
            print(f"operator invalid {(operator)},try (+) (-) (*) (/)")

        exit = input(
            "do you wanna exit of the calculator?if yes:type (s),if no just enter another thing: "
        )
        exit = exit.lower().startswith("s")
        if exit is True:
            print("successful exit")
            break
    except:
        print(
            "the itens need to be a digit:int or float,letters or symbols not will be permited,try again"
        )
