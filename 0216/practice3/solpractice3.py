import sys

sys.stdin = open('input.txt',encoding='UTF-8')

T = 10
def find_target(target , arr):
    cnt = 0                                         # 찾아야 하는 문자열이 몇개있는지 count
    i = 0                                           # 인덱스 값 선언
    while True:
        if i >= len(arr)-(len(target)-1):           # i가 전체 문자열길이 - (찾아야 하는 단어 길이 -1 ) 인 경우 종료
            break
        sum_word = []                               # word 가 범위를 순회하면서 단어들을 담을 리스트 선언
        for word in range(i,i+len(target)):
            sum_word.append(arr[word])              # i가 순회 하면서 해당 범위의 단어들을 append
        if "".join(sum_word) == target:             # 합쳐진 단어가 target 과 같으면 cnt 증가
            cnt += 1
        i += 1                                      # 인덱스 증가

    return cnt


for tc in range(1, T + 1):
    N = int(input())
    target = input()                            # 찾아야 하는 문자열 입력
    string = list(input())                      # 총 문자열 입력
    rlt = find_target(target,string)
    print(f'#{tc} {rlt}')

