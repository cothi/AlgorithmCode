#9-3 전보
import heapq
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, c = map(int, input().split())
graph = [[] for i in range(n+1)]

distance = [INF] * (n+1)

for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a].append((b, c))


def di(start):
  q = []
  heapq.heappush(q, (0, start))
  distance[start] = 0
  #초기화

  while q:
    dist, now = heapq.heappop(q)
    
    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      
      if cost < distance[i[0]]:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))


di(c)

count = 0
cost = 0

for i in distance:
  if i != INF:
    count += 1
    cost = max(cost, i)

print(graph)
print(distance)
print(count-1, cost)