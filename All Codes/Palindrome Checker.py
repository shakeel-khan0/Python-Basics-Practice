while True:
    user_input = input("Enter any string to check if it is a palindrome (or type 'exit' to quit): ")

    if user_input.lower() == "exit":
        print("Exiting...")
        break

    reverse_string = user_input[::-1]

    if reverse_string == user_input:
        print("String is a palindrome")
    else:
        print("String is not a palindrome")
