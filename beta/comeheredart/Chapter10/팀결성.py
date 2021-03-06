#10-2 팀 결성
#0 팀합치기 1 여부 확인

#합치기 연산
def union_parent(parent, a, b):
  ap = find_parent(parent, a)
  bp = find_parent(parent, b)
  
  if ap > bp:
    parent[ap] = b
  else:
    parent[bp] = a

#부모 얻기
def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])
  return parent[a]

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(n+1):
  parent[i] = i


for _ in range(m):
  t, a, b = map(int, input().split())
  if t == 0:
    union_parent(parent, a, b)
  else:
    if find_parent(parent, a) == find_parent(parent, b):
      print("YES")
    else:
      print("NO")