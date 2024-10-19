def in_to_cm(inch):
    return inch * 2.54


user_input = int(input("Enter inches: "))
print(f"Centimeters = {in_to_cm(user_input)}")


def cm_to_in(n):
    return n / 2.54


print(f"Inches = {cm_to_in(25.4)}")
