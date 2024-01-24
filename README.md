# Algorithm
알고리즘 공부 공간


<!-- PR은 최대한 다른 사람이 알아보기 쉽도록 자세히 써주세요. 특히 수도 코드 부분은 더더욱요...!!-->

## 🔗 문제 링크
<!-- 해결한 문제의 링크를 올려주세요. -->
[석유 시추](https://school.programmers.co.kr/learn/courses/30/lessons/250136)

## ✔️ 소요된 시간
<!-- 문제를 해결하는데 소요된 시간을 적어주세요. -->
1시간

## ✨ 수도 코드
<!-- 내가 작성한 코드를 모르는 사람이 봐도 이해할 수 있도록 글로 쉽게 풀어서 설명해주세요. -->
<!-- 알고리즘에 대한 지식이 전혀 없는 사람이 봐도 이해할 수 있도록 작성해주세요. 시각자료를 이용하면 더 좋습니다. -->
![Alt text](image.png)
위와 같은 석유가 있는데 시추관을 통해 하나만 뚫을 수 있을때 가장 많은 석유를 뽑을 수 있는 시추관의 위치 찾기 문제

？ 생각해야할 부분 : 각 시추관(x 좌표1~8)의 석유 양이 얼마나 되는지?

1. 1~8까지의 배열 만들기
2. 각 석유 덩어리가 1~8의 시추관중 어디에 속하는 석유인지 찾기
3. 예로 위 사진의 석유 덩어리에서 석유의 min_x(1) ~ max_x(3)까지는 다 +8 을 진행
    - BFS를 통해 land == 1과 visited == 0이 오면
    - 해당 석유 부터 들어가서 덩어리들 찾기
        1. 처음 x,y 큐에 넣기
        2. min, max을 계속해서 비교하면서 min과 max 갱신하기
        3. 석유 덩어리의 석유의 개수 추가(count++)
        4. 큐가 전부 없어질때 까지 진행
            1. 제일 왼쪽 빼기
            2. 각 상하좌우 움직이기
            3. 만약 visit도 안했고 land가 1(석유)이면 큐에 넣어주기
        5. result배열에 석유의 개수(count) 넣기
4. 똑같은 방식으로 모든 석유 덩어리들을 진행

1번 석유 덩어리 진행시
|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|
|8|8|8|0|0|0|0|0|

2번 석유 덩어리 진행시
|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|
|8|8|8|7|7|7|7|0|

3번 석유 덩어리 진행시
|1|2|3|4|5|6|7|8|
|---|---|---|---|---|---|---|---|
|8|8|8|7|7|7|9|2|

### 최종 코드
```python
from collections import deque

dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x, y, visited, land, result):
    count = 0
    visited[x][y] = 1
    q = deque()
    q.append([x,y])
    min_y, max_y = y, y
    while q:
        x,y = q.popleft()
        min_y = min(min_y, y)
        max_y = max(max_y, y)
        count += 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= len(land) or ny < 0 or ny >= len(land[0]):
                continue
                
            if visited[nx][ny] == 0 and land[nx][ny] == 1:
                visited[nx][ny] = 1
                q.append([nx,ny])
                
    for i in range(min_y, max_y+1):
        result[i] += count

def solution(land):
    result = [0] * len(land[0])
    visited = [[0 for i in range(len(land[0]))] for j in range(len(land))]
    
    for i in range(len(land)):
        for j in range(len(land[0])):
            if land[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, visited, land, result)
                
    print(result)       # 1번 예제 [8,8,8,7,7,7,9,2]
    return max(result)
```

## 📚 새롭게 알게된 내용
<!-- 새롭게 알게된 내용이 있다면 작성 해주시고 출처를 남겨주세요. -->
