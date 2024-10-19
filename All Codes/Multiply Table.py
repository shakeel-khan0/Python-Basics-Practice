user_input = int(input("Enter number to print its table: "))
length = int(input("Enter length of table you want to print: "))
print(f".....Printing table of {user_input}.....")
count = 1
number = 1
while number <= length:
    result = user_input * number
    print(f"{user_input} x {number} = {result}")
    count += 1
    number += 1