#위상 정렬
#아이디어는 큐에 진입차수가 0인 걸 넣고 큐가 빌때까지 큐에서 원소를 꺼내 간선을 지우고, 진입차수가 0이 된 노드를 큐에 넣는다. 

from collections import deque

v, e = map(int, input().split())
#진입차수
indegree = [0] * (v + 1)
#연결리스트
graph = [[] for i in range(v + 1)]

#그래프 정보 입력받기
for _ in range(e):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1 #진입차수 증가시키기  

def topology_sort():
  result = []
  q = deque()

#시작할 때 진입차수가 0인 노드 삽입
  for i in range(1, v+1):
    if indegree[i] == 0:
      q.append(i)
  
  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)


  for i in result:
    print(i, end=' ')

topology_sort()
