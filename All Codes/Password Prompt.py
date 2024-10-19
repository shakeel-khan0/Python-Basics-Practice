correct_password = "secret"
count = 0
limit = 0
limit_end = 5
while True:
    input_password = input("Enter Password: ")
    count += 1
    limit +=1
    remaining_limit = limit_end - limit
    if input_password == correct_password:
        print(f"your password is correct")
        break
    elif limit == limit_end:
        print("You exceed your limit...!")
        break
    else:
        print("wrong password! please try again")
    print(f"you have {remaining_limit} tries left")
