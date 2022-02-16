T='ABC ABCDAB ABCDABCDABDE'
P='ABCDABD'

def getPi(pattern):
    pi = [-1] * len(pattern)
    j=0
    for i in range(1, len(pi)):  # i끝, j앞
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j - 1] #순간이동
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
    print(f'접두사 , 접미사 {pi}')
    return pi


def kmp(word, pattern):
    pi = getPi(pattern)
    print(pi)
    results = []
    j=0
    for i in range(len(word)): #i word, j pattern
        while j > 0 and word[i] != pattern[j]:
            j = pi[j - 1]
        if word[i] == pattern[j]:
            if j==len(pattern)-1:
                results.append(i-len(pattern)+1)
                j=pi[j]
            else:
                j+=1
    print(f'결과 : {results}')
    return results

results = kmp(T, P)
print(len(results))
for r in results:
    print(r+1)