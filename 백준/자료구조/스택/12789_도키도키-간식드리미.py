# from collections import deque

# n = int(input())
# ticket = deque(list(map(int, input().split())))
# nop = []

# ticket_num = 1

# while ticket :
#     a = ticket.popleft()
#     if ticket_num != a:
#         nop.append(a)
#     else :
#         ticket_num = a+1

#     for i in range(len(nop)):
#         if ticket_num == nop[-1]:
#             ticket_num = nop[-1] + 1
#             nop.pop()
#         else :
#             break

# if nop:
#     print("Sad")
# else :
    # print("Nice")

n = 10
dict = {i : 0 for i in range(n)}
print(dict)