# using formula
"""
we pass value 10 to argument "n"
n = 10.... put in formula
10 * (10 + 1) // 2  =>  10 * (11) // 2 ( divided by 2 )
10 * 5.5  ==  55
"""

user_input = int(input("Enter number: "))


def sum_natural(n):
    if n == 1:
        return 1
    return n * (n + 1) // 2


print(sum_natural(user_input))
print()

# using range function


def sum_nat(n):
    if n == 1:
        return 1
    return sum(range(1, n + 1))


print(sum_nat(20))
