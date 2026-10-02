from collections import deque

def solution(numbers, target):
    answer = 0
    
    queue = deque([(numbers[0], 1), (-numbers[0], 1)])
    
    while len(queue) > 0:
        current, index = queue.popleft()
        if index < len(numbers):
            queue.append((current + numbers[index], index+1))
            queue.append((current - numbers[index], index+1))
        elif index == len(numbers) and target == current:
            answer += 1
    return answer