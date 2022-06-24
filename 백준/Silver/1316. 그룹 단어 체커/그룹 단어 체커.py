n = int(input())
rlt = n
for i in range(n):
    word = input()
    for w in range(len(word)-1):
        if word[w] != word[w+1]:
            new = word[w+1:]
            if word[w] in new:
                rlt -= 1
                break
print(rlt)
