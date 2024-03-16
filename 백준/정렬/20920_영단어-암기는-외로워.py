# import sys
# input = sys.stdin.readline

# N, M = map(int, input().rstrip().split()) # 단어 개수, 단어 길이
# word_lst = {} # 딕셔너리

# for _ in range(N):
#     word = input().rstrip()
    
#     if len(word) < M: # 단어가 M미만인 경우
#         continue
#     else: # 단어가 M이상인 경우
#         if word in word_lst: # 단어가 있는 경우
#             word_lst[word] += 1
#         else: # 단어가 없는 경우
#             word_lst[word] = 1

# print(word_lst)
# word_lst = sorted(word_lst.items(), key = lambda x : (-x[1], -len(x[0]), x[0])) # x[0] = 단어, x[1] = 단어 빈도수
# # -x[1] = 자주 나오는 단어 앞에 배치
# # -len(x[0]) = 단어 길이 길수록 앞에 배치
# # x[0] = 단어 사전 순 정렬

# for i in word_lst:
#     print(i[0])


    # 통과된 코드
import sys
input = sys.stdin.readline
N,M = map(int, input().split())
word_count = {}
for _ in range(N):
    word = input().rstrip()
    if len(word) >= M :
        if word in word_count :
            word_count[word][0] += 1
        else :
            word_count[word] = [1,len(word)]

print(word_count)
sorted_word_list = sorted(word_count, key=lambda key : (-word_count[key][0], -word_count[key][1], key))
print()
for word in sorted_word_list :
    print(word) 