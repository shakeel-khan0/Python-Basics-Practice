user_input = int(input("Enter number to check it is prime or not: "))

for i in range(2, user_input):
    if user_input%i == 0:
        print("Number is not prime.")
        break
    else:
        print("number is prime")
