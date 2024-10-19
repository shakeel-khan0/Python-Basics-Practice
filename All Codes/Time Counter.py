import time

user_input = input("Enter value to start timer in seconds: ")

try:
    remaining_time = int(user_input)
    if remaining_time <= 0:
        print("Invalid input! Please enter a positive value.")
    else:
        while remaining_time > 0:
            minutes = remaining_time // 60
            seconds = remaining_time % 60
            print(f"Remaining Time {minutes:02d}:{seconds:02d}")  # Format with leading zeros
            time.sleep(1)
            remaining_time -= 1
        print("Countdown Finished...!")
except ValueError:
    print("Invalid Input! Please enter a valid number...")
