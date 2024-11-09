def color(i, j, visited, *color):
    stack = [(i, j)]
    while stack:
        y, x = stack.pop()
        for k in [(0,1), (1,0), (-1,0), (0,-1)]:
            ni, nj = y + k[0], x + k[1]
            if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj] and arr[ni][nj] in color:
                visited[ni][nj] = 1
                stack.append((ni, nj))


N = int(input())
arr = [list(input().strip()) for _ in range(N)]
normal_visited = [[0] * N for _ in range(N)]  # 적록색약이 아닌 경우
not_normal_visited = [[0] * N for _ in range(N)]  # 적록색약인 경우
normal = 0
not_normal = 0
for i in range(N):
    for j in range(N):
        # 적록색약이 아닌 경우
        if not normal_visited[i][j]:
            color(i, j, normal_visited, arr[i][j])  # 현재 색상만 찾기
            normal += 1
        # 적록색약인 경우
        if not not_normal_visited[i][j]:
            if arr[i][j] == 'R' or arr[i][j] == 'G':
                color(i, j, not_normal_visited, 'R', 'G')  # R, G를 같은 색으로 취급
            else:
                color(i, j, not_normal_visited, arr[i][j])  # B는 원래대로 찾기
            not_normal += 1

print(normal, not_normal)