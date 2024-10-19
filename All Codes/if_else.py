l = {"shakeel", "khan", "jadoon"}
user_input = input("Enter name: ")
if user_input in l:
    print(f"{user_input} is available in current list.")
else:
    print("fuck you bitch")



user_input = input("Enter username: ")
length = len(user_input)
if length < 10:
    print("Your username is less then. \nUser name should be greater then 10 characters.")
else:
    print("Username is correct Good.")
