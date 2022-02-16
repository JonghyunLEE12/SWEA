import sys

sys.stdin = open('input.txt')

T = int(input())

def change(arr):
    global change_dict                          # 딕셔너리를 불러온 후
    num_list=[]                                 # 숫자로 바뀐 단어들을 담을 리스트
    for word in arr:
        num_list.append(change_dict.get(word))  # key값을 기반으로  숫자 append
    return num_list

def change_word(arr):
    change_word = { v : k for k,v in change_dict.items()}   # 딕셔너리의 key 값 과 value 값을 바꿔준다.
    word_list=[]
    for num in arr:                                     # 버블 소트로 인해 정렬된 단어들이 들어오게 된다.
        word_list.append(change_word.get(num))          # key 값을 기반으로 단어 append
    return word_list

def buble_sort(arr):
    for i in range(len(arr)-1):                         # 숫자로 된 단어들 버블 소트 이용하여 정렬
        for j in range(i,len(arr)):
            if arr[i] > arr[j]:
                arr[i],arr[j] = arr[j] , arr[i]
    return arr


for tc in range(1, T + 1):
    test_len = list(input().split())
    testcase = list(input().split())

    # 딕셔너리 형태로 언어와 숫자를 저장
    change_dict = dict(ZRO=0, ONE=1, TWO=2, THR=3, FOR=4, FIV=5, SIX=6, SVN=7, EGT=8, NIN=9)

    rlt = buble_sort(change(testcase))
    change_word(rlt)
    print(f'#{tc} {" ".join(change_word(rlt))}')

