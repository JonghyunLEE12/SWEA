import sys

sys.stdin = open('input.txt')

T = int(input())

def transpose(words):
    max_len = 0
    length = []
    for word in words:
        length.append(len(word))
        if len(word) > max_len:
            max_len=len(word)

    rlt = ''
    for i in range(max_len):
        for j in range(5):
            if length[j] > i:
                rlt += words[j][i]


    return rlt

for tc in range(1, T + 1):
    words = [list(input()) for _ in range(5)]
    rlt=transpose(words)
    print(f'#{tc} {rlt}')

