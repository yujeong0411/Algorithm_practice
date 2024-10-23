# bfs로 가능한 모든 상태 탐색
# 빨간 구슬만 구멍에 들어가는 경우의 최소 이동 횟수
#
def bfs(ri, rj, bi, bj, cnt):
    global result
    visited[ri][rj][bi][bj] = 1
    queue = [(ri, rj, bi, bj, cnt)]  # 빨간공 위치(ri,rj), 파란공 위치(bi,bj), 이동횟수(cnt)

    while queue:
        ry, rx, by, bx, cnt = queue.pop(0)  # 큐에서 현재 상태를 꺼냄
        if cnt > 9:  # 10번 초과 시 실패
            continue

        # 4방향 탐색 (좌,상,우,하)
        for k in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
            # 각 공을 현재 방향으로 이동시킴 (벽이나 구멍을 만날때까지)
            nry, nrx, r_moves = moving(ry, rx, k[0], k[1])  # 빨간공 이동
            nby, nbx, b_moves = moving(by, bx, k[0], k[1])  # 파란공 이동

            if (ry, rx) == (nry, nrx) and (by, bx) == (nby, nbx):
                continue  # 공들이 움직이지 않았으면 생략

            # 실패 조건
            if board[nby][nbx] == 'O':  # 파랑이 구멍에 빠지면 실패이므로 스킵
                continue  # 다른 방향 상태를 보기 위해 continue

            if (nry, nrx) == (nby, nbx):  # 두 공의 좌표가 같을 때 뒷쪽 공 좌표 옮기기
                if r_moves > b_moves:  # 뒤쪽 공이면 더 많이 이동
                    nry -= k[0]
                    nrx -= k[1]
                else:
                    nby -= k[0]
                    nbx -= k[1]

                # 성공 조건 (빨간 구슬만 구멍에 들어가야 함.)
            if board[nry][nrx] == 'O' and board[nby][nbx] != 'O':
                result = min(result, cnt + 1)
                return

            if not visited[nry][nrx][nby][nbx]:  # 방문하지 않은 곳의 좌표를 queue에 넣기
                visited[nry][nrx][nby][nbx] = 1
                queue.append((nry, nrx, nby, nbx, cnt + 1))


# 기울였을 때 움직이기
def moving(i, j, dx, dy):
    moves = 0  # 두 공이 같은 좌표에 있을 수 없으므로 더 많이 움직인 공(뒤쪽에 있는 공)을 찾아서 좌표 변경하기
    while True:
        ni, nj = i + dx, j + dy  # 다음 좌표
        if not (0 <= ni < N and 0 <= nj < M):  # 범위 내에 없으면 중단
            break
        if board[ni][nj] == '#':  # 벽이면 중단
            break
        if board[ni][nj] == 'O':  # 구멍이면 반환
            return ni, nj, moves + 1
        # 위 조건이 아니라면 계속 이동
        moves += 1
        i, j = ni, nj
    return i, j, moves


N, M = map(int, input().split())
board = [list(input().strip()) for _ in range(N)]
# 방문 체크 : 두 구슬의 모든 위치 조합을 저장 : 중복방지
visited = [[[[0] * M for _ in range(N)] for _ in range(M)] for _ in range(N)]  # 빨강, 파랑 방문 표시
# 빨강, 파랑 위치 찾기
for i in range(N):
    for j in range(M):
        if board[i][j] == 'R':
            ri, rj = i, j
        elif board[i][j] == 'B':
            bi, bj = i, j
result = 21e8
bfs(ri, rj, bi, bj, 0)

if result == 21e8:
    print(-1)
else:
    print(result)