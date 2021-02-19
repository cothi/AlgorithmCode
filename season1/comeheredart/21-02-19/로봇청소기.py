#https://www.acmicpc.net/problem/14503
#로봇청소기!

n, m = map(int, input().split())
x, y, d = map(int, input().split())
graph = [[] * m for i in range(n)]
visited = [[0] * m for i in range(n)]
visited[x][y] = 1

for i in range(n):
  graph[i] = list(map(int, input().split()))

def turn_left():
  global d
  d -= 1
  if d == -1:
    d = 3

def check():
  return graph[nx][ny] == 0 and visited[nx][ny] == 0

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


ans = 1
turn_time = 0
while True:
  turn_left()
  nx = x + dx[d]
  ny = y + dy[d]

  if check():
    visited[nx][ny] = 1
    x = nx
    y = ny
    ans += 1
    turn_time = 0
    continue

  else:
    turn_time += 1
    if turn_time == 4:
      nx = x - dx[d]
      ny = y - dy[d]

      if graph[nx][ny] == 0:
        x = nx
        y = ny
      else:
        break
      
      turn_time = 0
    
print(ans)

    
