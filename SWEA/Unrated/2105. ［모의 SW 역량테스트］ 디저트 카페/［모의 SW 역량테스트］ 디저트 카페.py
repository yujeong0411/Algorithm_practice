dir = [(1, 1), (1, -1), (-1, -1), (-1, 1), (0, 0)]  # 우하, 좌하, 좌상, 우상, 시작지점 비교위해 (0,0)
def dessert(y, x, d, visited):
    global i, j, result
    # print(cafes[y][x], d, visited)
    # 방향을 모두 돌았고, 시작 지점에 도착했다면
    if d == 3 and (y, x) == (i, j):
        result = max(result, len(visited))
        return

    # 직진
    ni, nj = y + dir[d][0], x + dir[d][1]
    if 0 <= ni < N and 0 <= nj < N and cafes[ni][nj] not in visited:
        dessert(ni, nj, d, visited + [cafes[ni][nj]])

    # 방향전환
    ni, nj = y + dir[d+1][0], x + dir[d+1][1]
    if 0 <= ni < N and 0 <= nj < N and cafes[ni][nj] not in visited:
        dessert(ni, nj, d+1, visited + [cafes[ni][nj]])


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    cafes = [list(map(int, input().split())) for _ in range(N)]
    result = -1

    # 시작할 수 있는 카페 범위 : i- 0 ~ N-2 / j - 1 ~ N-1
    for i in range(0, N - 2):
        for j in range(1, N - 1):
            dessert(i, j, 0, [])

    print(f'#{test_case} {result}')