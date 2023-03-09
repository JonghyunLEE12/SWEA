def solution(n, m, section):
    cnt = 0
    # 모든 영역을 다 칠할 때 까지 반복
    while section:
        # 윈도우 설정
        end = section[-1] - 1
        start = end - m + 1
        # 범위 초과 경우
        if start < 0:
            start, end = 0, m - 1
        cnt += 1
        while start <= (section[-1] - 1):
            section.pop()
            # 다 제거한 경우
            if not section:
                break
    return cnt