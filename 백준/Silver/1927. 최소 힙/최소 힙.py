import sys
import heapq

N = int(input())
h = []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num == 0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)

    else:
        heapq.heappush(h, num)