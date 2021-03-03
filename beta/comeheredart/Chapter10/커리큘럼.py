#10-4 커리큘럼
#진입 차수 문제.

from collections import deque
import copy

n = int(input())

jin = [0] * (n+1)
time = [0] * (n+1)
graph = [[] for i in range(n+1)]

for i in range(1, n+1):
  input_val = list(map(int, input().split()))
  time[i] = input_val[0]
  for x in input_val[1:-1]:
    jin[i] += 1
    graph[x].append(i)

q = deque()
result = copy.deepcopy(time)
def topology():
  #먼저 진입차수가 0이면 큐에 넣고
  for i in range(1, n+1):
    if jin[i] == 0:
      q.append(i)

  #큐가 빌때까지 빼고 넣기
  while q:
    now = q.popleft()

    for i in graph[now]:
      jin[i] -= 1
      result[i] = max(result[i], result[now] + time[i])

      if jin[i] == 0:
        q.append(i)

  for i in range(1, n+1):
    print(result[i])


topology()

    