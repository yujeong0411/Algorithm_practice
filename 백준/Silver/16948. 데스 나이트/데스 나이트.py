def bfs(r, c, end_r, end_c):
    global result
    q = []
    q.append((r, c, 0))
    visited[r][c] = 1
    while q:
        i, j, cnt= q.pop(0)
        for k in [(-2,-1),(-2,1),(0,-2),(0,2),(2,-1),(2,1)]:
            ni, nj = i + k[0], j + k[1]
            if ni == end_r and nj == end_c:
                return cnt + 1
            elif 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
                visited[ni][nj] = 1
                q.append((ni,nj, cnt+1))
    return -1

N = int(input())  # 체스판 크기
num = list(map(int, input().split()))
r1, c1 = num[0], num[1]
r2, c2 = num[2], num[3]
visited = [[0]*N for _ in range(N)]
result = bfs(r1, c1, r2, c2)
print(result)