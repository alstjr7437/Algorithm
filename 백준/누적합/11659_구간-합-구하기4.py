import sys
input = sys.stdin.readline
 
m, n = map(int, input().split())
arr = list(map(int, input().split()))
answer = [0]    
 
temp = 0    
for i in arr:  
    temp += i
    answer.append(temp)
 
# print(answer)

for i in range(n):
    a, b = map(int, input().split())
    print(answer[b] - answer[a-1])
