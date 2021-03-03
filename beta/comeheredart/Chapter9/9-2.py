#9-2 미래도시

n, m = map(int, input().split())

INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신 초기화
for a in range(1, n+1):
  for b in range(1, n+1):
    if a == b:
      graph[a][b] = 0

#입력받기
for _ in range(m):
  a, b = map(int, input().split())
  graph[a][b] = 1
  graph[b][a] = 1

x, k = map(int, input().split())


#플로이드 알고리즘
for k in range(1, n+1):
  for a in range(1, n+1):
    for b in range(1, n+1):
      graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])


answer = graph[1][k] + graph[k][x]

if answer == INF:
  print("-1")
else:
  print(answer)
