# 사진 찍을 수 있는곳 4방향 이상, 기준좌표로부터 인접 지역들 탐색
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # N줄 M개
    arr = [list(map(int, input().split())) for _ in range(N)]

    di = [0, 1, 0, -1, -1, -1, 1, 1]  # 우, 하, 좌, 상, 좌상, 우상, 좌하, 우하
    dj = [1, 0, -1, 0, -1, 1, -1, 1]
    candidate = 0   # 후보지 카운트
    for i in range(N):
        for j in range(M):
            dr_cnt = 0  # 방향 카운트, 기준점마다 초기화
            target = arr[i][j]  # 기준점
            for k in range(8):  # 인접 좌표 돌기
                near_i = i + di[k]
                near_j = j + dj[k]
                # 배열 벗어나지 않게 조건 걸기, 기준점보다 높이가 낮으면
                if 0 <= near_i < N and 0 <= near_j < M and target > arr[near_i][near_j]:
                    dr_cnt += 1   # 방향 카운트

            if dr_cnt >= 4:   # 4방향 이상이면 후보지 등록
                candidate += 1

    print(f'#{test_case} {candidate}')