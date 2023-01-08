cnt = 0
def solution(board, moves):
    answer = 0
    
    stack = [0]
    
    def search(col):
        global cnt
        col = col - 1
        for i in range(len(board)):
            if board[i][col] != 0:
                if stack[-1] == board[i][col]:
                    stack.pop()
                    cnt += 2
                else :   
                    stack.append(board[i][col])
                board[i][col] = 0
                return
    
    
    for move in moves:
        search(move)
    return cnt