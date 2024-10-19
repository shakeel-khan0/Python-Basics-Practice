input_string = input("Write anything: ")
vowels = "aeiouAEIOU"

count = 0
index = 0
while index < len(input_string):
    if input_string[index] in vowels:
        count += 1
    index += 1

print(f"Total vowels {count}")