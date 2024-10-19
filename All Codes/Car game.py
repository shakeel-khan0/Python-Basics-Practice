command = ""
while True:
    command = input("> ").lower()
    if command == "start":
        print("Car Start...")
    elif command == "stop":
        print("Car stop...!")
    elif command == "help":
        print("""
start - start the car
stop - stop the car
quit - exit game
        """)
    elif command == "quit":
        print("Exiting...")
        break
    else:
        print("Sorry! I don't understand that")
