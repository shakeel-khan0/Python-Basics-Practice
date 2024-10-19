
count = 0
while True:
    try:
        get_number1 = int(input("Enter first number: "))
        get_number2 = int(input("Enter second number: "))
        operator = input("Enter Operator (+, -, *, /, % or type exit to quit)  -->  ")
        if operator.lower() == "exit":
            print("Exiting...")
            break
        if operator == "+":
            sum = get_number1 + get_number2
            print(f"Sum of {get_number1} and {get_number2} = {sum}")
        elif operator == "-":
            dif = get_number1 - get_number2
            print(f"Difference of {get_number1} and {get_number2} = {dif}")
        elif operator == "*":
            mul = get_number1 * get_number2
            print(f"Multiplication of {get_number1} and {get_number2} = {mul}")
        elif operator == "/":
            if get_number2 == 0:
                print("you cannot divide any number with '0'")
            else:
                div = get_number1 / get_number2
                print(f"Division of {get_number1} and {get_number2} = {div}")
        elif operator == "%":
            qou = get_number1 % get_number2
            print(f"Quotient of {get_number1} and {get_number2} = {qou}")
        else:
            print("Invalid operator! please enter one of following '+,-,*,/,%'")
        count += 1
        print()
    except ValueError:
        print("Invalid input! Enter valid number")

