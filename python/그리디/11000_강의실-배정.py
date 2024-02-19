import heapq
import sys
n = int(sys.stdin.readline())
st = []
for i in range(n):
    st.append(list(map(int, sys.stdin.readline().split())))

st.sort(key=lambda x:(x[0],x[1]))

room = []
heapq.heappush(room, st[0][1])

for i in range(1, n):
    if room[0] <= st[i][0]:
        heapq.heappop(room)
    heapq.heappush(room, st[i][1])
print(len(room))