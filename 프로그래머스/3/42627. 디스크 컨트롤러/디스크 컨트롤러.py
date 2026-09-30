import heapq

def solution(jobs):
    answer = 0
    time = 0
    number = 0
    start = -1
    
    heap = []
    
    while number < len(jobs):
        for job in jobs:
            if start < job[0] <= time:
                heapq.heappush(heap,[job[1],job[0]])
        
        if heap:
            current = heapq.heappop(heap)
            start = time
            time += current[0]
            answer += time - current[1] #요청으로부터 처리시간
            number += 1
        else:
            time += 1
            
    return answer // len(jobs)
