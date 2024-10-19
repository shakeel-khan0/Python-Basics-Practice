numbers = [1, 3, 5, 7, 9, 5, 5, 7]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)