#11-4 만들 수 없는 금액

n = int(input())
val = list(map(int, input().split()))
val.sort()

target = 1

for x in val:
  if target < x:
    break
  target += x