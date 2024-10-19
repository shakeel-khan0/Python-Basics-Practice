
try:
    while True:
        user_input = int(input("Enter length of series you want: "))
        if user_input < 0:
            print("\n.....Please Enter a non-negative number.....\n")
        else:
            break
    if user_input == 0:
        print("No fibonacci series to display.")
    else:
        a = 0
        b = 1
        count = 2
        print("\n.....Printing Fibonacci Series.....\n")
        if user_input == 1:
            print(a)
        else:
            print(f"{a}  {b}  ", end="")
            while count < user_input:
                result = a + b
                print(f"{result}  ", end="")
                a = b
                b = result
                count += 1
except ValueError:
    print("Invalid Input! Please enter a valid number.")
