# 입력 파트
N, K = map(int, input().split())

# 문제 풀이
ans = 0

while N != 1:
    if N % K == 0:
        N = N // K
        ans += 1
    else:
        N -= 1
        ans += 1
        

# 출력 파트
print(ans)
