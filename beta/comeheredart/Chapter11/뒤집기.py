#11-3 문자열 뒤집기
#https://www.acmicpc.net/problem/1439


s = list(input())
val = [0,0]
pre = int(s[0])

if pre == 1:
  val[1] += 1
else:
  val[0] += 1

for i in range(1, len(s)):
  now = int(s[i])
  
  if pre != now:
    val[now] += 1

  pre = now


print(min(val))