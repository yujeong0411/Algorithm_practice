import sys
input = lambda : sys.stdin.readline()

def tetromino(y, x, cnt, total):
    global result
    # 가지치기 : 남은 도형 개수*배열 최대값을 더한 것이 최대합보다 작으면 탐색할 가치가 없다.
    if result >= total + arr_max*(3-cnt):
        return

        # 종료조건 :  도형 4개를 연결한 경우
    if cnt == 3:
        result = max(result, total)  # 최대값 갱신
        return

        # 블럭 연결하기
    for k in [(0,1),(1,0),(-1,0),(0,-1)]:  # 우, 하, 상, 좌
        ny, nx = y + k[0], x + k[1]
        # 범위 내에 있고, 방문하지 않은 경우
        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            if cnt == 1:  # 도형 2개를 연결한 경우 'ㅏ' 만들기
                visited[ny][nx] = 1
                # 2개까지 연결한 좌표로 돌아와서 탐색
                tetromino(y, x, cnt+1, total+arr[ny][nx])
                visited[ny][nx] = 0

            # 남은 4가지 도형
            visited[ny][nx] = 1
            tetromino(ny, nx, cnt+1, total+arr[ny][nx])
            visited[ny][nx] = 0

N, M = map(int, input().split())  # 세로, 가로
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
arr_max = max(map(max, arr))  
result = 0
for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        tetromino(i, j, 0, arr[i][j])
        visited[i][j] = 0
print(result)