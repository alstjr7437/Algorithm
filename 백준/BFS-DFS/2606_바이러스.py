from collections import deque

n = int(input())
m = int(input())

computer = {i : [] for i in range(1, n+1)}

for i in range(m):
    a,b = map(int, input().split())
    computer[a].append(b)
    computer[b].append(a)

queue = deque()
queue.append(1)

visited = [False] * n
visited[0] = True

while queue:
    q = queue.popleft()
    # print(f"pop item = {q}")
    for i in computer[q]:
        if visited[i-1] == False:
            queue.append(i)
            visited[i-1] = True
            
print(visited.count(True)-1)