def solution(ingredient):
    answer = 0
    index = 0
    while index < len(ingredient)-3:                   # 재료가 4개가 필요하기에 index가 리스트 총 길이 -3일때까지만 반복한다. 
        if ingredient[index] == 1:                     # 첫 재료가 빵일때만 
            if ingredient[index:index+4] == [1,2,3,1]: # 4개의 재료가 햄버거 재료 순서와 맞는지 비교
                del ingredient[index:index+4]          # 맞으면 해당 요소들 리스트에서 제거
                index = index-3                        # index를 -3 요소에서부터 다시 비교하도록 조정(시간을 줄이는 핵심포인트)
                answer += 1                            # 햄버거 카운트
                continue                               # 다음줄 index += 1 실행없이 다시 while문 처음부터 진행
        index += 1                                     # if문에 해당하지 않았으면 다음 index로 +1
    return answer