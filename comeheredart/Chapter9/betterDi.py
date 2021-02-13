#우선순위 큐를 이용한 dijkstra
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
start = int(input())
graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def di(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      if dist + i[1] < distance[i[0]]:
        distance[i[0]] = dist + i[1]
        heapq.heappush(q, (dist + i[1], i[0]))


di(start)
for i in range(1, n+1):
  if distance[i] == INF:
    pass
  else:
    print(distance[i])