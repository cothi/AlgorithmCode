# 입력 파트
N, M, K = map(int, input().split())
val = list(map(int, input().split()))
val.sort()
val.reverse()

ans = 0


#문제 풀이
while M != 0:
    for i in range(K):
        ans += val[0]
        M -= 1
    ans += val[1]
    M -= 1



#출력 파트
print(ans)
