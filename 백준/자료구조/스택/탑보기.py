import sys
input = sys.stdin.readline

n = int(input())
l = [0] + list(map(int, input().split()))

result = [[0, -int(1e9)] for _ in range(n+1)]

stack = []
for i in range(1, n+1):
    while stack and l[stack[-1]] <= l[i]:  
        stack.pop()
    result[i][0] += len(stack)    
    if stack:
        result[i][1] = stack[-1]  
    stack.append(i)

stack = []
for i in range(n, 0, -1):
    while stack and l[stack[-1]] <= l[i]:  
        stack.pop()
    result[i][0] += len(stack)    
    if stack and stack[-1]-i < i-result[i][1]:
        result[i][1] = stack[-1]  
    stack.append(i)

for i in range(1, n+1):
    if result[i][0] != 0:
        print(result[i][0], result[i][1])
    else:
        print(0)