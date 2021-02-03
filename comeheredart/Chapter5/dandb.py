from collections import deque

n, m, v = map(int, input().split())
matrix = [(n + 1) * [0] for _ in range(n + 1)]
visited = [False] * (n+1)
visited2 = [False] * (n+1)
#인접행렬 표현
for _ in range(m):
  line = list(map(int, input().split()))
  matrix[line[0]][line[1]] = 1
  matrix[line[1]][line[0]] = 1

#인접행렬 출력
for i in range(n+1):
  for j in range(n+1):
    print(matrix[i][j], end=' ')
  print()


def dfs(v, visited):
  visited[v] = True
  print(v, end=' ')

  for i in range(1, n+1):
    if visited[i] == False and matrix[v][i] == 1:
      dfs(i, visited)


def bfs(v, visited):
  queue = deque([v])

  visited2[v] = True

  while queue:
    i = queue.popleft()
    print(i, end=' ')

    for j in range(1, n+1):
      if visited2[j] == 0 and matrix[i][j] == 1:
        queue.append(j)
        visited2[j] = True



dfs(v, visited)
print()
bfs(v, visited2)
