# from itertools import product

# def solution(word):
#     words = []
#     answer = 0
#     alpha = ['A','E','I','O','U']
#     for i in (1,6):
#         for c in product(alpha,repeat=i):
#             words.append(''.join(list(c)))
#     words.sort()
#     print(words.index(word)+1)
#     return answer



from itertools import product

def solution(word):
    words = []
    alpha = ['A','E','I','O','U']
    for i in range(1, 6):
        for c in product(alpha, repeat=i):
            words.append(''.join(list(c)))

    words.sort()
    print()
    return words.index(word) + 1