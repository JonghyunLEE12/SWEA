n = int(input())
graph = []
for i in range(n):
    graph.append(input().split())


def avoid(x, y):
    global n, graph
    dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
    can_avoid = False
    for dx, dy in dirs:
        nx = x + dx
        ny = y + dy
        while 0 <= nx < n and 0 <= ny < n:
          if graph[nx][ny] == 'X':
            nx += dx
            ny += dy
          elif graph[nx][ny] =='S':
            return False
          else:
            break
    return True
    
def dfs(last):
      global n, graph
      if last == 0:
          possible = True
          for i in range(n):
              for j in range(n):
                  if graph[i][j] == 'T':
                      possible &= avoid(i, j)
          return possible
      result = False
      
      for i in range(n):
          for j in range(n):
              if graph[i][j] == 'X':
                    graph[i][j] = 'O'
                    result |= dfs(last - 1)
                    graph[i][j] = 'X'
      return result

if dfs(3):
    print('YES')
else:
    print('NO')