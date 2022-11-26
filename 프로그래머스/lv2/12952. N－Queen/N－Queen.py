# def dfs(queen,n,row):
#     count = 0
    
#     if n == row:
#         return 1
#     for col in range(n):
#         queen[row] = col
        
#         for x in range(row):
#             if queen[x] == queen[row]:
#                 break
#             if abs(queen[x] - queen[row]) == (row - x):
#                 break
#     else:
#         count += dfs(queen , n , row + 1)        
                
#     return count


# def solution(n):
#     queen = [0]* n
#     answer = dfs(queen,n,0)
#     return answer



def dfs(queen, row, n):
    count = 0
    if n == row:
        return 1
    for col in range(n):
        queen[row] = col
        for i in range(row):
            if queen[i] == queen[row]:
                break
            if abs(queen[i]-queen[row]) == row - i:
                break
        else:
            count += dfs(queen, row + 1, n)
    return count
def solution(n):
    return dfs([0]*n, 0, n)