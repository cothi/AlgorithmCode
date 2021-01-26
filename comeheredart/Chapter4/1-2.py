# 입력 파트, 문제 풀이
row, col = map(int, input().split())

ans = 0

for _ in range(row):
    cards = list(map(int, input().split()))
    min_val = min(cards)
    ans = max(ans, min_val)


#출력 파트
print(ans)

