# 입력 파트
N, M = map(int, input().split()) 
x, y, direct = map(int, input().split())

did = [[0] * N for i in range(M)]

mapp = []
for i in range(N):
  mapp.append(list(map(int, input().split())))

# 변수

dic = [(-1, 0), (0, 1), (1, 0), (0, -1)]
did[x][y] = 1
ans = 1
turn = 0

# 왼쪽으로 도는 함수

def turnLeft():
  global direct
  direct -= 1
  if direct == -1:
    direct = 3



while True:
  turnLeft()

  nx = x + dic[direct][0]
  ny = y + dic[direct][1]

  #가보지 않았다면
  if mapp[nx][ny] == 0 and did[nx][ny] == 0:
    ans += 1
    x = nx
    y = ny
    did[x][y] = 1
    turn = 0

  else: #가봤던 칸이거나 바다라면
    turn += 1

  if turn == 4:
    nx = x + dic[direct][1]
    ny = y + dic[direct][0]
    if mapp[nx][ny] == 0:
      x = nx
      y = ny
    else:
      break
    turn = 0


print(ans)
