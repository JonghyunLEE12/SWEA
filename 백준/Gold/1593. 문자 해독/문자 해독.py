g,s_length = map(int,input().split(' '))
W = input()
S = input()

count = 0

wa = [0]*58
sa = [0]*58

for x in W:
    wa[ord(x) - 65] += 1

start , length = 0,0

for i in range(len(S)):
    sa[ord(S[i]) - 65] += 1
    length += 1

    if length == len(W):
        if wa == sa:
            count += 1
        sa[ord(S[start]) - 65]  -= 1
        start += 1
        length -= 1


print(count)