user_input = int(input("Enter the number: "))
for i in range(1, user_input+1):
    if i == 1 or i == user_input:
        print("*"* user_input, end="")
    else:
        print("*", end="")
        print(" "* (user_input-2), end="")
        print("*", end="")

    print()