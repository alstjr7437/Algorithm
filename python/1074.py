# Z  
# 분할정복, 재귀
# https://www.acmicpc.net/problem/1074

'''
1사분면: 가로 < 2^(n-1) AND 세로 < 2^(n-1)
2사분면: 가로 ≥ 2^(n-1) AND 세로 < 2^(n-1)
3사분면: 가로 < 2^(n-1) AND 세로 ≥ 2^(n-1)
4사분면: 가로 ≥ 2^(n-1) AND 세로 ≥ 2^(n-1)
아래 배열을 4분면으로 나누면, 시작점이 0, 4, 8, 12 이다.
'''

N, r, c = map(int, input().split())
count = 0

while N != 0:
    N -= 1
    size = 2 ** N

    # 1사분면
    if r < size and c < size:
        count += 0

    # 2사분면
    elif r < size and c >= size:
        count += size * size
        c -= size

    # 3사분면
    elif r >= size and c < size:
        count += size * size * 2
        r -= size

    # 4사분면
    else:
        count += size * size * 3
        r -= size
        c -= size

print(count)


'''
# 굳이 똑같은 배열을 만들어서 할 필요가 없음
dx = [1,-1,1,1]
dy = [0,1,0,-1]
result = [[0] * (2**N) for _ in range(2**N)]
x,y = 0, 0

for i in range(4**N):
    result[y][x] = i
    if dx[i%4] + x >= 2**N :
@ -14,3 +56,4 @@ for i in range(4**N):
        y = dy[i%4] + y

print(result[r][c])
'''