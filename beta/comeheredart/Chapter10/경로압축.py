#경로 압축
#서로소 집합 알고리즘에서 재귀였던 부분은 최악의 상황에서 노드가 v개일 경우 O(v)이므로 이 부분을 경로압축으로!! 나머지는 똑같다

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


v, e = map(int, input().split())

parent = [0] * (v+1)

#부모 테이블 초기화
for i in range(1, v+1):
  parent[i] = i

for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)


for i in range(1, v+1):
  print(find_parent(parent, i), end=' ')
  #그럼 parent[i]랑 똑같겠지?!