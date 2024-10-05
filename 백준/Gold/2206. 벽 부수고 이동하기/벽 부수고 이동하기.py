from heapq import heappush, heappop

def move(i, j, brick):
    queue = []
    heappush(queue, (1, i, j, brick))
    while queue:
        # 현재 이동 칸 수, 좌표, 벽돌 부순 횟수
        current, y, x, brick = heappop(queue)
        current = dp[y][x][brick]
        if (y, x) == (N-1, M-1):
            return current

        for k in [(1,0), (-1,0), (0,-1), (0,1)]:
            ny, nx = y + k[0], x + k[1]
            if 0 <= ny < N and 0 <= nx < M:
                if map[ny][nx] == 1 and brick == 0:
                    dp[ny][nx][1] = current + 1
                    heappush(queue, (current + 1, ny, nx, 1))
                if map[ny][nx] == 0 and dp[ny][nx][brick] == 0:
                    dp[ny][nx][brick] = current + 1
                    heappush(queue, (current + 1, ny, nx, brick))
    return -1


N, M = map(int, input().split())  # 도착점
map = [list(map(int, input().strip())) for _ in range(N)]
# print(map)
# 좌표, 부순 횟수
dp = [[[0, 0] for _ in range(M)] for _ in range(N)]
# print(dp)
dp[0][0][0] = 1  # 시작하는 칸도 이동에 포함
result = move(0, 0,0)  # 시작 좌표, 벽돌 부수는 횟수
print(result)