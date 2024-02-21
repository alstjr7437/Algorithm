"""
https://www.acmicpc.net/problem/1766
골드 2 문제집 문제
"""

n,m = map(int, input().split())
result = []
for i in range(1,n+1):
    result.append(i)

a = []
for i in range(m):
    a,b = map(int, input().split())
    result.remove(b)
    result.index(a)

    index = 0
    for i in range(result.index(a), len(result)):
        print(result, i, len(result))
        print(b, result[i])

        if b > result[i] :
            if i == len(result)-1 :
                index = i
                break
            continue
        else:   
            if i == len(result)-1 :
                index = i
                break 
            print("hello")
            index = i-1
            break

    result.insert(index + 1, b)
    print(result)

print(" ".join(map(str, result)))

# n,m = map(int, input().split())
# result = []
# for i in range(1,n+1):
#     result.append(i)

# a = []
# for i in range(m):
#     a,b = map(int, input().split())
#     result.remove(b)
#     result.index(a)

#     index = 0
#     for i in range(result.index(a), len(result)):
#         print(result, i, len(result))
#         if i == len(result)-1 :
#             index = i + 1
#         if result[i] < b :
#             continue
#         else:    
#             print("Good")
#             index = i + 1
#             break

#     result.insert(index, b)
#     print(result)
# print(" ".join(map(str, result)))