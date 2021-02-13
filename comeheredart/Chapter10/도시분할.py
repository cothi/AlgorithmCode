#10-3 도시 분할 계획
#두개로 나누는 거니까 최소 신장 알고리즘으로 총 합 구한다음 제일 큰거 빼면 되겠다
#https://www.acmicpc.net/problem/1647

def find_parent(parent, a):
    if parent[a] != a:
      parent[a] = find_parent(parent, parent[a])
    return parent[a]

def union_parent(parent, a, b):
  ap = find_parent(parent, a)
  bp = find_parent(parent, b)

  if ap > bp:
    parent[ap] = b
  else:
    parent[bp] = a

n, m = map(int, input().split())
parent = [0] * (n+1)
for i in range(1, n+1):
  parent[i] = i
edges = []
result = 0
max_val = 0

for _ in range(m):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))
  
edges.sort()

for edge in edges:
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    max_val = max(max_val, cost)

print(result - max_val)