from heapq import heappop, heappush

N = int(input())
heap = []
for _ in  range(N):
    heappush(heap, int(input()))

result = 0
while len(heap) != 1:
    sum_v = heappop(heap) + heappop(heap)
    result += sum_v
    heappush(heap, sum_v)
print(result)
