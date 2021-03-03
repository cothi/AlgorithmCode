#https://programmers.co.kr/learn/courses/30/lessons/12945
#첨에 그냥 단순히 재귀로 했더니 당연히 시간 초과가 났다! DP 바텀업을 써야지

def solution(n):
    data = [0] * 100001
    data[1] = 1
    data[2] = 1
    
    for i in range(3, n+1):
        data[i] = data[i-1] + data[i-2] 
    
    return data[n] % 1234567
  