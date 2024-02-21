"""
잃어버린 괄호
그리디
https://www.acmicpc.net/problem/1541
"""

"""
실수 부분
처음에 생각할때 -를 자르고 어떻게 +를 짜르지 생각했는데
생각해보니
1. -로 split 배열(minus)
2. minus를 다돌면서 +를 잘라서 그 수를 결과에 넣어주고
3. 결과는 그럼 +를 다 한 부분과 -로 짤린 부분으로 됏으므로
4. result 전체를 돌면서 빼주면 끝!!! 

문제를 생각할때 어떻게 풀어나갈지 잘 생각해 나가자!

"""
# 

n = input()
minus = n.split('-')
result = []

for i in minus:
    flus = i.split("+")
    sum = 0
    for j in flus:
        sum += int(j)
    result.append(sum)

all = result[0]
for i in result[1:]:
    all -= i

print(all)