def pattern(n):
    if n == 0:
        return
    print("*" * n)
    pattern(n-1)
pattern(5)


def patt(n):
    if n == 1:
        return
    # print(" " * (n-1) + "*" * (2 * n-1))
    # patt(n-1)
    print(" " * (n - 1) + "*" * (2 * (5 - n) + 1))
    patt(n-1)


patt(5)

