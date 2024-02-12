words = ["leet","code"]
x = 'e'
count = []
for i in range(len(words)):
    for j in words[i]:
        if j == x:
            if i in count:
                break
            else:
                count.append(i)
print(count)