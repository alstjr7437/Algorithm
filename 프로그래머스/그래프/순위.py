"""
https://school.programmers.co.kr/learn/courses/30/lessons/49191
"""

def solution(n, results):
    answer = 0
    win_graph = {}    # 이긴 애들
    lose_graph = {}   # 진 애들
    
    for i in range(1, n+1):
        win_graph[i] = set()
        lose_graph[i] = set()

    for winner, loser in results:  # 결과에서 이기고 진 애들 그래프화
        if winner not in win_graph:
            win_graph[loser] = set()
        if loser not in lose_graph:
            lose_graph[winner] = set()
        win_graph[loser].add(winner)
        lose_graph[winner].add(loser)

    for i in range(1, n+1):         
        for winner in win_graph[i]:  # i한테 진 애들 -> i를 이긴 애들한테도 짐
            if i in lose_graph:
                lose_graph[winner].update(lose_graph[i])
                print(win_graph, lose_graph)
        for loser in lose_graph[i]:  # i한테 이긴 애들 -> i한테 진 애들한테도 이김
            if i in win_graph:
                win_graph[loser].update(win_graph[i])
        print(win_graph, lose_graph)
    
    for i in range(1, n+1):
        if len(win_graph[i]) + len(lose_graph[i]) == n-1:  # i한테 이기고 진 애들 합쳐서 n-1이면 순위가 결정된 것
            answer += 1

    return answer
