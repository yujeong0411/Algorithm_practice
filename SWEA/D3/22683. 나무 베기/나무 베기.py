from heapq import heappush, heappop
def leising(x, y, tree, dr, end):
    queue = []  # (조직횟수, 좌표, 나무 베기 횟수, 방향)
    heappush(queue, (0, x, y, tree, dr))
    while queue:
        current, i, j, cnt, direction = heappop(queue)
        current = dp[i][j][cnt][direction]

        # 현재 조작횟수보다 작으면 넘어가기
        if dp[i][j][cnt][direction] < current:
            continue

        # 도착지에 도달하면 종료
        if (i, j) == end:
            return current

        # 전진
        ni, nj = i+di[direction], j+dj[direction]
        if 0 <= ni < N and 0 <= nj < N:
            # 지나갈 수 있거나 도착지 일 경우
            if arr[ni][nj] == 'G' or arr[ni][nj] == 'Y':
                # 새로운 조작횟수가 기존 횟수보다 작으면 갱신
                if current + 1 < dp[ni][nj][cnt][direction]:
                    dp[ni][nj][cnt][direction] = current + 1
                    heappush(queue, (current+1, ni, nj, cnt, direction))
            # 나무가 있고 벨수 있는 경우
            elif arr[ni][nj] == 'T' and cnt < M:
                if current + 1 < dp[ni][nj][cnt+1][direction]:
                    dp[ni][nj][cnt+1][direction] = current + 1
                    heappush(queue, (current + 1, ni, nj, cnt+1, direction))
        # 좌회전
        left_dr = (direction-1) % 4
        if current + 1 < dp[i][j][cnt][left_dr]:
            dp[i][j][cnt][left_dr] = current + 1
            heappush(queue, (current + 1, i, j, cnt, left_dr))

        # 우회전
        right_dr = (direction + 1) % 4
        if current + 1 < dp[i][j][cnt][right_dr]:
            dp[i][j][cnt][right_dr] = current + 1
            heappush(queue, (current + 1, i, j, cnt, right_dr))

    return -1

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(input().strip()) for _ in range(N)]
    # print(arr)
    #DP 배열 : 가장 큰 값으로 초기화
    # i, j 좌표에서 나무를 k번 벤 상태에서 방향이 dr일때, 최소 조작 횟수
    dp = [[[[21e8]*4 for _ in range(M+1)] for _ in range(N)] for _ in range(N)]
    # print(dp)
    di =  [-1, 0, 1, 0 ]  # 북, 동, 남, 서
    dj = [0, 1, 0, -1]
    # 시작점, 끝점 찾기
    start = end = None
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'X':
                start = (i, j)
            elif arr [i][j] == 'Y':
                end = (i, j)

    # 처음은 북쪽(dr=0)을 바라보며 시작
    y_start, x_start = start
    dp[y_start][x_start][0][0] = 0
    result = leising(x_start, y_start, 0, 0, end)
    print(f'#{test_case} {result}')





