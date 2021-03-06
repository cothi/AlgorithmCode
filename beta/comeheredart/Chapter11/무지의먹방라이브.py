#그리디. 처음엔 -1 해가면서 반복문으로 접근했는데 시간이랑 효율성에서 어림도 없었다
#남은 접시 양까지 출력하는거 아니고 그 순서 번호만 나오면 되는거니까 걸리는 시간이 적은 음식부터 빼가면서 생각해야겠다 힙을 써야하겠다

import heapq
def solution(food_times, k):
    
    if sum(food_times) <= k:
        return -1
    
    q = []
    
    #시간 순대로 정렬 - 우선순위 큐에 넣기
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i+1))
    
    time = 0 #누적 먹은 시간
    length = len(food_times) #남은 접시 개수
    pre = 0 #전에 먹은 걸린 시간
    
    while time + ((q[0][0] - pre) * length) <= k: #시간되면 먹는 거 반복
        now = heapq.heappop(q)[0]
        time += (now - pre) * length
        length -= 1
        pre = now
        
    result = sorted(q, key=lambda x:x[1]) #이번엔 번호순으로 정렬
    return result[(k-time) % length][1] #계산해서 출력