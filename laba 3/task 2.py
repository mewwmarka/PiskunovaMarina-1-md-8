words = []
while True:
    word = input()
    if word == 'stop':
        break
    words.append(word)
print(" ".join(words))
