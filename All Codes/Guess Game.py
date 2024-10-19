#print("You have three tries")
secrect_no = 9
guess_count = 0
guess_limit = 3
while guess_count < guess_limit:
    guess = int(input("Guess number 0-9 ->  "))
    guess_count += 1
    if guess == secrect_no:
        print("you won! Congratulations")
        break
else:
    print("Sorry you failed!")
