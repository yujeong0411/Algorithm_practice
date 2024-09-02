import heapq
# dfs -> RecursionError

def loopy(i, j, cnt):
    heapq.heappush(h, (cnt, i, j))   # 최소 비용을 위해 cnt 먼저
    while h:
        cnt, i, j = heapq.heappop(h)
        # 마지막 좌표이면 출력
        if i == N-1 and j == N-1:
            print(f'Problem {tc}: {cnt}')
            return

        for k in [(1,0), (0,1), (-1,0), (0,-1)]: # 하, 우, 상, 좌
            ni, nj = i + k[0], j + k[1]
            # 범위 내에 있고, 방문하지 않았으면
            if 0 <= ni < N and 0 <= nj < N and not v[ni][nj]:
                v[ni][nj] = 1  # 방문표시
                heapq.heappush(h, (cnt+arr[ni][nj], ni, nj))


tc = 1
while True:
    N = int(input())
    if N == 0:
        break
        
    arr = [list(map(int, input().split())) for _ in range(N)]
    v = [[0]*N for _ in range(N)]  # 방문표시
    h = []
    v[0][0] = 1  # 방문표시
    loopy(0, 0, arr[0][0]) # 좌표, cnt 값

    tc += 1

