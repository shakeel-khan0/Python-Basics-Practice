text = "Hello this is shakeel"

words = text.split()
index = 1
longest_word = " "

while index < len(words):
    if len(words[index]) > len(longest_word):
        longest_word = words[index]
    index += 1
print(f"Longest word is: {longest_word}")
