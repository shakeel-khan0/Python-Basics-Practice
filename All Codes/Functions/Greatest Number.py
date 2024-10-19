a = int(input("Enter first number: "))
b = int(input("Enter first number: "))
c = int(input("Enter first number: "))


def check_greater(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    elif c > a and c > b:
        return c


print(f"The greatest number is {check_greater(a, b, c)}")
