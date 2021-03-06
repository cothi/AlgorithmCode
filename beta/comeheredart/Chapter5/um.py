n, m = map(int, input().split())
til = []

for _ in range(n):
  til.append(list(map(int, input())))

def dfs(x,y):
  if x < 0 or y < 0 or x >= n or y >= m:
    return False
  
  #방문을 안했으면
  if til[x][y] == 0:
    til[x][y] = 1 #방문
    dfs(x-1, y)
    dfs(x+1, y)
    dfs(x, y-1)
    dfs(x, y+1)
    return True

  return False


result = 0
for i in range(n):
  for j in range(m):
    if dfs(i,j) == True:
      result += 1


print(result)
