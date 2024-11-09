dir = [(0,0), (-1,0), (0,1), (1,0), (0,-1)]
def performance(i, j, c, p, n):
    maps[i][j].append((p, n))
    visited = [[-1] * 10 for _ in range(10)] # 충전범위를 방문배열에 저장
    visited[i][j] = 0
    queue = [(i, j)]
    while queue:
        y, x = queue.pop(0)
        for k in range(1, 5):  # 상하좌우 확인
            ny, nx = y + dir[k][0], x + dir[k][1]
            # 범위 내에 있고, 방문하지 않았다면
            if 0 <= ny < 10 and 0 <= nx < 10 and visited[ny][nx] == -1:
                visited[ny][nx] = visited[y][x] + 1
                # 충전범위를 벗어났다면 넘어가기
                if visited[ny][nx] > c:
                    continue
                maps[ny][nx].append((p, n))
                queue.append((ny, nx))

T = int(input())
for test_case in range(1, T + 1):
    M, A = map(int, input().split())  # 총이동시간, bc개수
    a_route = [0] + list(map(int, input().split()))
    b_route = [0] +  list(map(int, input().split()))
    maps = [[[] for _ in range(10)]for _ in range(10)]
    # 배터리 성능 범위 표시 => n:성능이 같은 배터리가 있을 수 있으므로 숫자 표시
    for n in range(1, A+1):
        i, j, c, p = map(int, input().split())
        performance(j-1, i-1, c, p, n)
    # 성능이 높은 순으로 정렬
    for i in range(10):
        for j in range(10):
            maps[i][j].sort(reverse=True)

    # for lst in maps:
    #     print(lst)

    ai, aj, bi, bj = 0, 0, 9, 9
    result = 0
    for k in range(M+1):  # M 초동안 움직이기
        # print('초:', k, ai, aj, bi, bj)
        ai += dir[a_route[k]][0]
        aj += dir[a_route[k]][1]
        bi += dir[b_route[k]][0]
        bj += dir[b_route[k]][1]
        # a는 있고, b는 없다면
        if maps[ai][aj] and not maps[bi][bj]:
            result += maps[ai][aj][0][0]
        # b는 있고, a는 없다면
        elif maps[bi][bj] and not maps[ai][aj]:
            result += maps[bi][bj][0][0]
        # 둘다 bc 범위에 있고
        elif maps[ai][aj] and maps[bi][bj]:
            if maps[ai][aj][0][1] == maps[bi][bj][0][1]: # 같은 bc라면
                result += maps[ai][aj][0][0]  # 먼저 성능이 높은 것을 더하고
                if len(maps[ai][aj]) > 1 and len(maps[bi][bj]) > 1:  # 각 위치에서 또 다른 bc들이 있다면
                    result += max(maps[ai][aj][1][0], maps[bi][bj][1][0])  # 그 중 성능이 높은 것 더하기
                else:
                    if len(maps[ai][aj]) == 1 and len(maps[bi][bj]) > 1:  # a는 bc가 하나이고, b는 1개 이상일 때
                        result += maps[bi][bj][1][0]  # b가 두번째 bc 충전
                    elif len(maps[bi][bj]) == 1 and len(maps[ai][aj]) > 1:  # b가 하나이고, a는 1개 이상일 때
                        result += maps[ai][aj][1][0]
            else:
                result += (maps[ai][aj][0][0] + maps[bi][bj][0][0])
    print(f'#{test_case} {result}')