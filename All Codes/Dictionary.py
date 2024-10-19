
d = {}
for i in range(2):
    friends = input("Enter your name: ")
    lan = input("Enter your fav language: ")
    d.update({friends: lan})
print(d)
find = input("Enter key to find its value: ")
print(d[find])


s = set()
s.add(1)
s.add("1")

print(s)


unique = set()
for num in range(9):
    number = int(input("Enter any number"))
    unique.add(number)
print(unique)

words = {
    "madad": "Help",
    "bili": "Cat",
    "kutta": "Dog"
}
word = input("Enter a word to get meaning: ")
print(words[word])
