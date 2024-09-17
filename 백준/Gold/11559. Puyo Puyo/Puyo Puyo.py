def puyo1():
    global result
    cnt = 0

    # 뿌요 찾기
    for i in range(12):
        visited = [[0] * 6 for _ in range(12)]
        for j in range(6):
            if not visited[i][j] and arr[i][j] != '.':
                visited[i][j] = 1
                queue = [(i, j)]
                temp = [(i, j)]  # 터트릴 뿌요 임시 저장

                while queue:
                    ny, nx = queue.pop()
                    # print((ny, nx), 'pop')
                    for k in [(0,1), (1,0), (-1,0), (0,-1)]:
                        ni, nj = ny + k[0], nx + k[1]
                        if 0 <= ni < 12 and 0 <= nj < 6 and not visited[ni][nj] and arr[ni][nj] == arr[i][j]:
                            visited[ni][nj] = 1
                            queue.append((ni, nj))
                            temp.append((ni, nj))
                            # print(queue, "queue")
                            # print(temp, "temp")

                if len(temp) >= 4:
                    cnt += 1
                    for y, x in temp:
                        arr[y][x] = '.'

    # 뿌요 내리기
    for i in range(6):
        idx = 11
        for j in range(11, -1, -1):
            if arr[j][i] != '.':
                arr[j][i], arr[idx][i] = arr[idx][i], arr[j][i]
                idx -= 1
    # print(arr)

    if cnt >= 1:
        result += 1
        # print(result, "result")
        puyo1()


arr = [list(input()) for _ in range(12)]
result = 0
puyo1()
print(result)