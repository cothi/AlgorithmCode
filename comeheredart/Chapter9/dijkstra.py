import sys
input = sys.stdin.readline
INF = int(1e9)

#노드개수, 간선개수
n,m = map(int, input().split())
#시작노드
start = int(input())
#그래프
graph = [[] for i in range(n+1)]
visited = [False] * (n+1)
distance = [INF] * (n+1)

#간선 정보 입력받기
for _ in range(m):
  a,b,c = map(int, input().split())
  graph[a].append((b, c))

#방문안한 노드 중 최단 거리가 짧은 노드 반환
def get_smallest_node():
  min_val = INF
  index = 0
  for i in range(1, n+1):
    if distance[i] < min_val and not visited[i]:
      min_val = distance[i]
      index = i

  return index


def dijkstra(start):
  #시작노드 초기화
  distance[start] = 0
  visited[start] = True
  for j in graph[start]:
    distance[j[0]] = j[1]
  
  #나머지 노드 반복
  for _ in range(n-1):
    now = get_smallest_node()
    visited[now] = True

    for j in graph[now]:
      if j[1] + distance[now] < distance[j[0]]:
        distance[j[0]] = j[1] + distance[now]


dijkstra(start)

for i in range(1, n+1):
  if distance[i] == INF:
    pass
  else:
    print(distance[i])