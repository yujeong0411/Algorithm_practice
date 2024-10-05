def bfs(i, j):
    cnt = 1
    q = [(i, j, 1)]
    visited[i][j] = 1
    while q:
        y, x , time = q.pop(0)  # 현재 좌표, 시간
        # 이동시간이 끝났으면 종료
        if time == L:
            return cnt
        # 위치에 맞는 방향 탐색
        for dy, dx in pipe[tunnel[y][x]]:
            ny, nx = y+dy, x+dx  # 다음 갈 수 있는 위치
            # 범위 내에 있고, 방문하지 않았고, 이동시간이 남은 경우
            if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx] and time < L:
                # 다음 위치가 현재 방향과 연결되는지 확인 (연결-> 반대방향)
                if (-dy, -dx) in pipe[tunnel[ny][nx]]:
                    q.append((ny, nx, time+1))
                    visited[ny][nx] = 1
                    cnt += 1
    return cnt

T = int(input())
for test_case in range(1, T + 1):
    N, M, R, C, L = list(map(int, input().split()))  # 세로, 가로, 맨홀 좌표, 소요시간
    tunnel = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0]*M for _ in range(N)]
    # 파이프 방향
    pipe = [[], [(0,1),(1,0),(0,-1),(-1,0)], [(-1,0),(1,0)], [(0,1),(0,-1)], [(-1,0),(0,1)], [(1,0),(0,1)], [(1,0),(0,-1)], [(-1,0),(0,-1)]]
    result = bfs(R, C)
    print(f'#{test_case} {result}')