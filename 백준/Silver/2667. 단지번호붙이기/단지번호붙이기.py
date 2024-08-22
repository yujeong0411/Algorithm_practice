def DFS(N):
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    stack = []
    result = []
    for i in range(N):
        for j in range(N):
            if town[i][j] == 1:  # 집이 있다면 주변 탐색
                cnt = 1
                town[i][j] = 0  # 방문 표시
                stack.append((i, j))

                while stack:
                    ci, cj = stack[-1]   # 현재 위치 = stack 마지막 요소
                    for k in range(4):  # 인접 방향 탐색
                        ni = ci + di[k]
                        nj = cj + dj[k]
                        if 0 <= nj < N and 0 <= ni < N and town[ni][nj] == 1:
                            town[ni][nj] = 0   # 방문 표시
                            cnt += 1  # 집 카운트
                            stack.append((ni, nj))
                            break
                    else:
                        stack.pop()  # 더이상 갈 곳이 없으면 제거
                result.append(cnt)
    result.sort()
    return result


N = int(input())  # 배열크기
town = [list(map(int, input())) for _ in range(N)]
result = DFS(N)
print(len(result))
for i in result:
    print(i)