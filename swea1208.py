testcase = 10
for tc in range(1,testcase+1):
    # 덤프 횟수를 저장할 변수
    dump_num = int(input())
    # 박스의 높이값
    box_height = list(map(int,input().split()))

    for i in range(dump_num+1):
        # 박스 높이 최고점 과 인덱스
        max_height = max(box_height)
        max_idx = box_height.index(max_height)

        # 박스높이 최저점 과 인덱스
        min_height = min(box_height)
        min_idx = box_height.index(min_height)

        # 최고점에서 -1 , 최저점 + 1
        box_height[max_idx] -= 1
        box_height[min_idx] += 1

        # 주어진 덤프 횟수 이내에 평탄화가 완려되면 더 이상 덤프를 수행할 수 없으므로, 그 떄의 최고점과 최저점
        # 높이차를 반환 해야한다.
        if max_height - min_height <= 1:
            result = max_height - min_height
            break

        else:
            result = max_height - min_height
    print(f'#{tc} {result}')