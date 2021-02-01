from collections import deque
n, m = map(int, input().split())
graph = []

for _ in range(n):
  graph.append(list(map(int, input())))

#상하좌우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
  queue = deque()

  queue.append((x,y))

  while queue:
   x, y = queue.popleft()
   
   for i in range(4):
     nx = x + dx[i]
     ny = y + dy[i]

     if nx < 0 or ny < 0 or nx >= n or ny >= m: #범위 나갈때
       continue

     if graph[nx][ny] == 0: #괴물일때
        continue 

     if graph[nx][ny] == 1:
