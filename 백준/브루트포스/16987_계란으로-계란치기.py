def egg_crack(index, eggs):
    if index == len(eggs):
        return sum(1 for durability, _ in eggs if durability <= 0)
    
    if eggs[index][0] <= 0:
        # 현재 계란 깨졋으면 다음 계란
        return egg_crack(index + 1, eggs)
    
    max_broken = 0
    hit = False  # 다른 계란 쳤는지
    
    for i in range(len(eggs)):
        if i != index and eggs[i][0] > 0:
            hit = True
            eggs[index][0] -= eggs[i][1]
            eggs[i][0] -= eggs[index][1]
            
            max_broken = max(max_broken, egg_crack(index + 1, eggs))
            
            eggs[index][0] += eggs[i][1]
            eggs[i][0] += eggs[index][1]
    
    # 칠 수 있는 계란이 없으면 다음 계란으로 넘어감
    if not hit:
        max_broken = max(max_broken, egg_crack(index + 1, eggs))
    
    return max_broken

n = int(input())
egg = [list(map(int, input().split())) for _ in range(n)]

print(egg_crack(0, egg))