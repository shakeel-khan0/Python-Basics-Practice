get_input = int(input("Enter any number: "))
even = get_input % 2 ==0
if even:
    print(f"{get_input} is even")
else:
    print(f"{get_input} is odd")