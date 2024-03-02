from collections import deque

n = int(input())
a = list(map(int,input().split()))

balloon = deque()
for i in range(n):
    balloon.append([i+1, a[i]])

answer = []
while balloon:
    temp = balloon.popleft()
    answer.append(temp[0])
    move = temp[1]
    if not balloon :
        break
    if move > 0:
        for _ in range(move-1):
            balloon.append(balloon.popleft())
    else :
        for _ in range(-move):
            balloon.appendleft(balloon.pop())

print(" ".join(map(str, answer)))

