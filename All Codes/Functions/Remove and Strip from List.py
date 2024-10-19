l = ["shakeel", "khan", "an", "aan"]

a = []


def remo(l, word):
    for i in l:
        if not i == word:
            a.append(i.strip(word))
    return a


print(remo(l, "an"))
