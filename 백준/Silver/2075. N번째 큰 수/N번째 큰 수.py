import heapq
N = int(input())
h = []
for _ in range(N):
    hip = list(map(int, input().split()))
    if not h:
        for num in hip:
            heapq.heappush(h, num)
    else:
        for num in hip:
            if h[0] < num:
                heapq.heappush(h, num)
                heapq.heappop(h)
print(h[0])