def climb(i, j, one):
    global result
    result = max(result, visited[i][j])  # 최댓값 갱신

    # 4방향 탐색
    for k in [(0,1), (1,0), (0,-1), (-1,0)]:
        ni, nj = i + k[0], j + k[1]
        # 범위 내에 있고, 방문하지 않은 경우
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            if maps[i][j] > maps[ni][nj]:  # 지형이 낮다면
                visited[ni][nj] = visited[i][j] + 1  # 방문 표시
                climb(ni, nj, one)
                visited[ni][nj] = 0 # 방문 해제

            # 공사 기회가 있고, 공사할 경우 지형이 낮다면
            elif one and maps[i][j] > maps[ni][nj] - K:
                visited[ni][nj] = visited[i][j] + 1   # 방문 표시
                temp = maps[ni][nj]
                maps[ni][nj] = maps[i][j] - 1   # 가장 긴 경로를 찾아야 하므로 이전 지형에서 -1 깎기
                climb(ni, nj, one-1)
                visited[ni][nj] = 0   # 방문 해제
                maps[ni][nj] = temp   # 원래 값 되돌리기


T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 배열크기, 공사가능 깊이
    maps = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    # 최대 높이 찾기
    top = 0
    for i in range(N):
        for j in range(N):
            if maps[i][j] > top:
                top = maps[i][j]

    # 등산로 찾기
    result = 0  # 최대 등산로 길이
    for i in range(N):
        for j in range(N):
            if maps[i][j] == top:
                visited[i][j] = 1
                climb(i, j, 1)
                visited[i][j] = 0

    print(f'#{test_case} {result}')