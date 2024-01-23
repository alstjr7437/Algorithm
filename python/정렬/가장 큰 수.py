"""
https://school.programmers.co.kr/learn/courses/30/lessons/42746
Level2 
"""
"""
문제1
3 30이 들어가게 되면 330이 들어가야 303이 들어간 것 보다 크게 들어간다.
0부터 1000까지 원소가 들어갈 수 있어서 
3번을 곱해서 그 3개를 비교해서 들어가도록 하면 되는거 였다!!
3 30 → 333 303030 → 333과 303비교 ! → 333이 더 크므로 들어가게 됨

문제2
제출 후 찾아보니 하나가 틀렸는데 다른 사람들의 답을 보니
return str(int(''.join(num)))
으로 리턴을 했다 처음에 잘 몰랐지만 다시 잘 생각해보니
000이 들어가게 되면 → 0으로 바껴야하는데 int로 바꾸지 않으면 000이 들어가고 끝나게 된다.
"""
def solution(numbers):
    num = list(map(str, numbers))       
    num.sort(key = lambda x : x*3, reverse = True)
    
    return ''.join(num)
