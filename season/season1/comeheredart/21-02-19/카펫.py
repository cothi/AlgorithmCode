#yellow가 관건. yellow 가 나올 수 있는 경우의 수 다 보면서 2(가로+세로)+4해서 그게 브라운이면 답.
#첨에 yellow % i == 0 조건을 안두고 했다가 계속 틀려서 짜증났다
#https://programmers.co.kr/learn/courses/30/lessons/42842

import math
def solution(brown, yellow):
    answer = []
    for i in range(1, int(math.sqrt(float(yellow)))+1):
        if yellow % i == 0:
            row = i
            col = yellow // i
        
            if ((row + col) * 2) + 4 == brown:
                answer.append(col+2)
                answer.append(row+2)
                break

    return answer