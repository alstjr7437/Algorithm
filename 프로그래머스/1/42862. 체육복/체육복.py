def solution(n, lost, reserve):
    cnt = [0] + [1] * n + [0]   # 0번, n+1번은 가상의 학생

    for i in lost: cnt[i] -= 1
    for i in reserve: cnt[i] += 1

    for i in range(1, n + 1):
        if cnt[i] == 0:
            if cnt[i-1] == 2:
                cnt[i-1] = 1
                cnt[i] = 1
            elif cnt[i+1] == 2:
                cnt[i+1] = 1
                cnt[i] = 1

    return sum(1 for i in range(1, n + 1) if cnt[i] >= 1)