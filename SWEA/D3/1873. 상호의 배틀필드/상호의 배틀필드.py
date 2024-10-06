def battle(i, j, dr):
    for c in command:
        # print(c)
        if c == 'S':
            ni, nj = i+dir[dr][0], j+dir[dr][1]
            while 0 <= ni < H and 0 <= nj < W:  # 범위 내에서 진행
                if maps[ni][nj] == '*': # 벽돌이라면
                    maps[ni][nj] = '.'
                    # print('shoot', maps)
                    break
                elif maps[ni][nj] == '#': # 강철이라면
                    break
                else:
                    # 계속 이동
                    ni += dir[dr][0]
                    nj += dir[dr][1]
                    # print('s못하고 이동', maps)
        else:  # 이동
            new_dr = movement.index(c)  # 이동방향 c의 인덱스 찾기
            maps[i][j] = tank[new_dr]
            ni, nj = i+dir[new_dr][0], j+dir[new_dr][1]
            if 0 <= ni < H and 0 <= nj < W:  # 범위 내에 있다면
                if maps[ni][nj] == '.':  # 평지면 이동
                    maps[i][j] = '.'  # 이전 탱크 위치 평지로 변경
                    maps[ni][nj] = tank[new_dr]  # 탱크 위치 갱신
                    i, j = ni, nj
                    # print('평지이동', maps)
                # else:
                    # print('방향만 전환', maps)
            dr = new_dr
    return i, j, dr

T = int(input())
for test_case in range(1, T + 1):
    H, W = map(int, input().split())  # 맵의 세로, 가로
    maps = [list(input().strip()) for _ in range(H)]

    dir = [(-1,0), (1,0), (0,-1), (0,1)]  # 위, 아래, 왼, 오
    tank = ['^', 'v', '<', '>']
    movement = ['U', 'D', 'L', 'R']

    N = int(input())  # 커맨드 개수
    command = list(input().strip())
    # 전차 찾기
    flag = 0
    for i in range(H):
        for j in range(W):
            for t in range(4):
                if maps[i][j] == tank[t] and flag == 0:
                    battle(i, j, t)
                    flag = 1
                    # print('tank')
                    break

    print(f'#{test_case}', end=' ')
    for r in maps:
        print(''.join(r))
