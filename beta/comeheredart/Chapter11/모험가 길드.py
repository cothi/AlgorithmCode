#11-1 모험가 길드
#최대로 결성해야하니까 최소부터 보면서 그룹 결성하기

n = map(int, input())
val = list(map(int, input().split()))

val.sort()

answer = 0

count = 0
for i in val:
  count += 1
  if count >= i:
    answer += 1
    count = 0

print(answer)