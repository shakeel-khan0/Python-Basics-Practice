user_input = int(input("Enter number for factorial: "))
factorial = 1
for i in range(1, user_input+1):
    factorial *= i
print(f"The factorial of {user_input} is {factorial}")


