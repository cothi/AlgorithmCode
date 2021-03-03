#서로소 집합을 통한 사이클 판별
#합쳐가면서 부모가 같으면 사이클이 일어난 것! 아이디어

def find_parent(parent, a):
  if parent[a] != a:
    parent[a] = find_parent(parent, parent[a])

  return parent[a]

def union_parent(parent, a, b):
  ap = find_parent(parent, a)
  bp = find_parent(parent, b)
  
  if ap > bp:
    parent[a] = bp
  else:
    parent[b] = ap
    

v, e = map(int, input().split())

parent = [0] * (v+1)

#초기화
for i in range(1, v+1):
  parent[i] = i

cycle = False

for _ in range(e):
  a, b = map(int, input().split())
  #사이클이 발생한 경우
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  else:
    union_parent(parent, a, b)


if cycle:
  print("사이클 발생")
else:
  print("발생안함")