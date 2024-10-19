zero = 0
count = 0
sum_numbers = 0
while True:
    get_numbers = int(input("Enter number (enter '0' to quit: "))
    count += 1
    if get_numbers == zero:
        break
    sum_numbers += get_numbers
print(f"sum of {get_numbers} is {sum_numbers}")
