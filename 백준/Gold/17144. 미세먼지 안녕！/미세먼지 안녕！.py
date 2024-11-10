def dust():
    temp = [[0] * C for _ in range(R)]  # 확산될 미세먼지를 임시 저장할 배열

    # 미세먼지가 있는 모든 칸에서 확산량 계산
    for i in range(R):
        for j in range(C):
            if room[i][j] > 0:  # 미세먼지가 있는 칸
                plus = room[i][j] // 5  # 확산되는 양
                cnt = 0  # 확산된 방향 수

                for di, dj in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C and room[ni][nj] != -1:
                        temp[ni][nj] += plus
                        cnt += 1

                room[i][j] -= plus * cnt  # 확산되고 남은 미세먼지

    # 확산된 미세먼지 합치기
    for i in range(R):
        for j in range(C):
            room[i][j] += temp[i][j]


# 공기청정기 작동
dir = [(-1,0), (0,1), (1,0), (0, -1)]
def clean(up_i, down_i):
    # 위쪽 공기청정기 (반시계 방향)
    # 아래로
    for i in range(up_i - 1, 0, -1):
        room[i][0] = room[i - 1][0]
    # 왼쪽으로
    for j in range(0, C - 1):
        room[0][j] = room[0][j + 1]
    # 위로
    for i in range(0, up_i):
        room[i][C - 1] = room[i + 1][C - 1]
    # 오른쪽으로
    for j in range(C - 1, 1, -1):
        room[up_i][j] = room[up_i][j - 1]
    room[up_i][1] = 0

    # 아래쪽 공기청정기 (시계 방향)
    # 위로
    for i in range(down_i + 1, R - 1):
        room[i][0] = room[i + 1][0]
    # 왼쪽으로
    for j in range(0, C - 1):
        room[R - 1][j] = room[R - 1][j + 1]
    # 아래로
    for i in range(R - 1, down_i, -1):
        room[i][C - 1] = room[i - 1][C - 1]
    # 오른쪽으로
    for j in range(C - 1, 1, -1):
        room[down_i][j] = room[down_i][j - 1]
    room[down_i][1] = 0

R, C, T = map(int, input().split())  # 세로, 가로, 초
room = [list(map(int, input().split())) for _ in range(R)]
# 공기 청정기 좌표 구하기
air_purifier = []
for i in range(R):
    for j in range(C):
        if room[i][j] == -1:
            air_purifier.append((i, j))

up_i, up_j = air_purifier[0][0], air_purifier[0][1]
down_i, down_j = air_purifier[1][0], air_purifier[1][1]
for _ in range(T):  # T초 동안
    dust()
    # for lst in room:
    #     print(lst)
    clean(up_i, down_i)

result = 0
for i in range(R):
    for j in range(C):
        if room[i][j] > 0:
            result += room[i][j]

print(result)