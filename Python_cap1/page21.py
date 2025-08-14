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
            print(
                f"the result of addition ({number_float}) + ({number_1_float}) is: {sum}"
            )

        elif operator == "-":
            subtraction = number_float - number_1_float
            print(
                f"the result of subtraction ({number_float}) - ({number_1_float}) is: {subtraction}"
            )

        elif operator == "/":
            try:
                division = number_float / number_1_float
                print(
                    f"the result of division ({number_float}) / ({number_1_float}) is: {division}"
                )
            except:
                print("it is impossible to divide a number by zero")
        elif operator == "*":
            multiplication = number_float * number_1_float
            print(
                f"the result of multiplyng ({number_float}) * ({number_1_float}) is: {multiplication}"
            )

        else:
            print(
                f"operator invalid ({operator}),try (+) (-) (*) (/),just one per time"
            )

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
        exit_1 = input(
            "do you wanna exit of the calculator?if yes:type (s),if no just enter another thing: "
        )
        exit_1 = exit_1.lower().startswith("s")
        if exit_1 is True:
            print("successful exit")
            break
