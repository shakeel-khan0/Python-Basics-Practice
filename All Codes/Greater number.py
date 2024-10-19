get_input1 = int(input("Enter first digit: "))
get_input2 = int(input("Enter second digit: "))
get_input3 = int(input("Enter third digit: "))

if get_input1 > get_input2 and get_input3:
    print(f"{get_input1} is greater from both {get_input2} and {get_input3}")
elif get_input2 > get_input3 and get_input1:
    print(f"{get_input2} is greater from both {get_input1} and {get_input3}")
elif get_input3 > get_input1 and get_input2:
    print(f"{get_input3} is greater from both {get_input1} and {get_input2}")
else:
    print(f"All numbers {get_input1}, {get_input2} and {get_input3} are equal")