def move(si, sj, cnt):
    global result
    # 최댓값 갱신
    result = max(result, cnt)
    visited[ord(board[si][sj])-65] = 1

    # 4방향 탐색 (상, 우, 하, 좌)
    for k in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni, nj = si + k[0], sj + k[1]
        # 범위 내에 있고, 지나온 알파벳이 아니면
        if 0 <= ni < R and 0 <= nj < C and not visited[ord(board[ni][nj])-65]:
            visited[ord(board[ni][nj])-65] = 1
            move(ni, nj, cnt+1)   # 다음 위치로 이동
            visited[ord(board[ni][nj]) - 65] = 0


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
result = 1  # 최솟값 1 초기화
visited = [0] * 26  # 알파벳 체크
move(0, 0, 1)
print(result)