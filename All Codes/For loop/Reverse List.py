original_list = [1, 2, 3, 4, 5]
print(f"Original List is: {original_list}")
reverse_list = []
for i in original_list:
    reverse_list = [i] + reverse_list
print(reverse_list)
