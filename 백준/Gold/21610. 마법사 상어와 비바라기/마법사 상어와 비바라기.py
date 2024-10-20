N, M = map(int, input().split())
sky = [list(map(int, input().split())) for _ in range(N)]
      #           ←,       ↖,        ↑,       ↗,       →,     ↘,      ↓,       ↙
dir = [(0, 0), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
cloud = [(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)]
for _ in range(M):
    direction, distance = map(int, input().split())
    # 비구름 이동
    move_cloud = []
    for i, j in cloud:
        ni, nj = (i + (dir[direction][0] * distance) + N) % N, (j + (dir[direction][1] * distance) + N) % N
        sky[ni][nj] += 1  # 물 양 증가
        move_cloud .append((ni, nj))

    # 물복사버그 마법 (대각선)
    for ci, cj in move_cloud :
        for k in range(2, 9, 2):
            ni, nj = ci + dir[k][0], cj + dir[k][1]
            if 0 <= nj < N and 0 <= ni < N and sky[ni][nj] > 0:
                sky[ci][cj] += 1

    # 새 구름 생성
    cloud= []
    for i in range(N):
        for j in range(N):
            if (i, j) not in move_cloud :
                if sky[i][j] >= 2:
                    cloud.append((i, j))
                    sky[i][j] -= 2

print(sum(sum(lst) for lst in sky))
