# 입력 파트

n = input()
x = int(n[1])
y = int(ord(n[0])) - int(ord('a')) + 1

#수평2 수직1
#수평1 수직2
count = 0
moves = [(1, 2), (2, 1), (-1, 2), (2, -1), (-1, -2),(-2, -1), (1, -2), (-2, 1)]


for move in moves:
  dx = x + move[0]
  dy = y + move[1]
  if dx < 1 or dy < 1 or dx > 8 or dy > 8:
    continue

  count += 1

#출력 파트
print(count)