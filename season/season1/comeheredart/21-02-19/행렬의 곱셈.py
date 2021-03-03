 #https://programmers.co.kr/learn/courses/30/lessons/12949
 #생각보다 오래걸렸다.. 구현 연습을 더 하자!

 def solution(arr1, arr2):
    
    #결과의 행, 열
    row = len(arr1)
    col = len(arr2[0])
    answer = [[0] * col for _ in range(row)]
    
    #같을 때만 곱할 수 있으니까 3 * 2 X 2 * 3 이렇게
    if len(arr1[0]) == len(arr2):
        for i in range(row):
            for j in range(col):
                for k in range(len(arr2)):
                    answer[i][j] += arr1[i][k] * arr2[k][j]
    
    return answer