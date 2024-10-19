user_input = int(input("Enter number to print table: "))
print(f"\n.....Printing table of {user_input}.....\n")
for i in range(11):
    result = i*user_input
    print(f"{user_input} * {i} = {result}")
