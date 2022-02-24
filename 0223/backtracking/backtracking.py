# DFS 를 이용한 완전 탐색
def powerset(idx, N):
    # idx == N 이 됐을 때, bit 출력
    if idx == N:
        print(bit)
        return
    # 부분 집합 구하는 중
    else:
        bit[idx] = 0
        powerset(idx + 1, N)

        bit[idx] = 1
        powerset(idx + 1, N)


a = [1,2,3]
N = len(a)
bit = [0]*N
powerset(0,N)
