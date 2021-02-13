#크루스칼 알고리즘
#아이디어는 데이터를 비용에 따라 오름차순으로 정렬하고, 사이클이 생기면 트리에 안넣고 안생기면 트리에 넣는다! 최적해 보장!

def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a > b:
    parent[a] = b
  else:
    parent[b] = a

v, e = map(int, input().split())
parent = [0] * (v+1)

edges = []
result = 0

#부모 초기화
for i in range(1, v+1):
  parent[i] = i

for _ in range(e):
  a, b, cost = map(int, input().split())
  edges.append((cost, a, b))

edges.sort()
print(edges)

for edge in edges:
  #사이클 없을 때만 합치기 수행
  cost, a, b = edge
  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    result += cost
    

print(result)