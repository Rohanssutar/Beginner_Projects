user = input("Enter a sentence: ").split(" ")
count = {}

for word in user:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

for x, y in count.items():
    print(f"{x}:",y)
