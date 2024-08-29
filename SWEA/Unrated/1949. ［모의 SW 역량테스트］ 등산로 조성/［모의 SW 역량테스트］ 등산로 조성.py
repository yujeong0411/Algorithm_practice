# 가장 높은 봉우리에서 시작
# 높->낮, 가로 또는 세로로 연결
# 한 곳을 정해서 K 깊이 만큼 공사
# 가장 긴 등산로 찾기
def climb(i, j, one):
    global result
    result = max(result, visited[i][j])  # 최대 높이 갱신
    for k in [(0, 1), (1, 0), (-1, 0), (0, -1)]:
        ni, nj = i + k[0], j + k[1]
        if 0 <= ni <N and 0 <= nj < N and not visited[ni][nj]:
            if arr[i][j] > arr[ni][nj]:  # 최대 높이 산보다 작다면 방문
                visited[ni][nj] = visited[i][j] + 1 # 등산로 방문 및 길이 표시
                climb(ni, nj, one)
                visited[ni][nj] = 0  # 되돌리기
                # 이동할 곳이 없는데, 공사 기회(one)가 있고, K만큼 지형을 깎아서 이동 가능한 경우
            elif arr[i][j] > arr[ni][nj] - K and one:
                visited[ni][nj] = visited[i][j] + 1 # 등산로 방문 및 길이 표시
                temp = arr[ni][nj]  # 값 저정해두기
                arr[ni][nj] = arr[i][j] - 1  # 다음 등산로 = 현재 등산로에서 -1 뺀 만큼으로 설정
                climb(ni, nj, one-1)  # 공사 기회 사용
                visited[ni][nj] = 0   # 되돌리기
                arr[ni][nj] = temp  # 되돌리기

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())  # 한 변 길이, 최대 가능 공사 깊이
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 최대 높이 찾기
    top = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] > top:
                top = arr[i][j]

    result = 0  # 최대 등산로 길이
    visited = [[0]*N for _ in range(N)]  # 등산로의 길이를 저장하면서 방문표시
    for i in range(N):
        for j in range(N):
            if arr[i][j] == top:  # 최대 높이라면
                visited[i][j] = 1  # 방문표시
                climb(i, j, 1)  # 좌표, 공사 기회(1번)
                visited[i][j] = 0  # 되돌리기
    print(f'#{test_case} {result}')