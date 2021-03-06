#https://www.acmicpc.net/problem/1012
#DFS다! 이코테 얼음얼리기?랑 비슷한 듯

N = int(input())


for _ in range(N):
  Y, X, chu = map(int, input().split())
  graph = [[0] * Y for i in range(X)]
  ans = 0


  #배추 입력받기
  for _ in range(chu):
    b, a = map(int, input().split())
    graph[a][b] = 1


  def dfs(x, y):
    if x < 0 or y < 0 or x >= X or y >= Y:
      return False

    if graph[x][y] == 1:
      graph[x][y] = 0
      dfs(x-1, y)
      dfs(x, y-1)
      dfs(x+1, y)
      dfs(x, y+1)
      return True

    return False


  for i in range(X):
    for j in range(Y):
      if dfs(i, j) == True:
        ans += 1


  print(ans)

