#https://www.acmicpc.net/problem/7568
#덩치. 첨엔 정렬인가 했는데 그냥 단순하게 하면 된듯

n = int(input())
people = []

for _ in range(n):
  w, h = map(int, input().split())
  people.append((w, h))

for now in people:
  count = 1
  for temp in people:
    if now[0] < temp[0] and now[1] < temp[1]:
      count += 1
      
  print(count)

 