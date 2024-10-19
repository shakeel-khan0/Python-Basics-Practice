# import math
#
# user_input = int(input("Enter number to find factorial: "))
#
# print(f"The factorial of {user_input} is = {math.factorial(user_input)}")

user_input = input("Enter a number to find its factorial: ")
try:
    user_input = int(user_input)
    if user_input < 0:
        print("Factorial is not defined for negative numbers.")
    else:
        factorial = 1
        number = user_input
        while number > 0:
            factorial *= number
            number -= 1
        print(f"The factorial of {user_input} is = {factorial}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")