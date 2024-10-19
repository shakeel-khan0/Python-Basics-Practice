import random

count = 0
start_number = 1
end_number = 100
random_number_generator = random.randint(start_number, end_number)
attempts = 0
max_attempts = 5
while attempts < max_attempts:
    try:
        user_guess = int(input("Enter your guess number b/w 1 - 100 -->  "))
        count += 1
        if user_guess > end_number or user_guess < start_number:
            print("you number is out of range. Please! try to guess between 1 - 100.")
            continue
        attempts += 1
        remaining_attempts = max_attempts - attempts
        if user_guess == random_number_generator:
            print("Your Guess is correct. Congratulations You win!")
            break
        elif user_guess < random_number_generator:
            if attempts == max_attempts:
                print("Your guess is lesser.\n You loose! out of attempts")
                break
            else:
                print(f"Close...! your guess is less then secret number. \nTry again! \nyou have {remaining_attempts} attempts left")
                print()
        elif user_guess > random_number_generator:
            if attempts == max_attempts:
                print("Your guess is greater.\nYou loose! out of attempts")
                break
            else:
                print(f"Close...! your guess is greater then secret number. \nTry again! \nyou have {remaining_attempts} attempts left")
                print()
    except ValueError:
        print("Invalid input! Please enter a valid number")
