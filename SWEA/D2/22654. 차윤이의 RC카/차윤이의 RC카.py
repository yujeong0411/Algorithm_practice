def move(start, end, dr):
    i, j, direction = start[0], start[1], dr
    for c in command:
        ni, nj = i+dir[direction][0], j+dir[direction][1]
        if c == 'A' and 0 <= ni < N and 0 <= nj < N and field[ni][nj] !='T':
            i, j = ni, nj
        elif c == 'L':
            direction = (direction-1) % 4
        elif c == 'R':
            direction = (direction+1) % 4
            
    # command가 모두 실행될 때까지 도착점에 도달해도 끝낼 수 없다.
    if (i, j) == end:
        return 1
    return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 필드 크기
    field = [list(input().strip()) for _ in range(N)]
    dir = [(-1,0), (0,1), (1,0), (0,-1)]  # 상, 우, 하, 좌
    start = end = None
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                start = (i, j)
            elif field[i][j] == 'Y':
                end = (i, j)

    Q = int(input()) # 조종 횟수
    result = []
    for _ in range(Q):
        C = input().split()
        a = C[0]
        command = C[1]
        # print(command)
        result.append(move(start, end, 0))
    print(f'#{test_case}', *result)

