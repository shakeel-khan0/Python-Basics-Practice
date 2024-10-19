# Celsius to fahrenheit...
# .........Take input from user.........
def temperature():
    get_temp = int(input("Enter temperature: "))
    fahrenheit = (get_temp * 9 / 5) + 32
    print(fahrenheit)


temperature()


# .........By passing argument.........


def temp(fah):
    celsius = (fah * 9 / 5) + 32
    print(f"Temperature in celsius {celsius}")


temp(35)


# .........Default Argument.........


def tempe(fah=35):
    celsius = (fah * 9 / 5) + 32
    print(f"{celsius}")


tempe()

# .........Fahrenheit to Celsius

f = int(input("Enter temperature in F: "))


def f_to_c(a):
    return 5 * (a - 32) / 9


print(f"Temperature in Celsius {round(f_to_c(f), 2)}°F")
