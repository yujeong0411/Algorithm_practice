def move(si, sj, cnt):
    global result
    result = max(result, cnt)

    for k in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
        ni, nj = si + k[0], sj + k[1]
        if 0 <= ni < R and 0 <= nj < C and board[ni][nj] not in stack:
            stack.add(board[ni][nj])
            move(ni, nj, cnt+1)
            stack.remove(board[ni][nj])


R, C = map(int, input().split())
board = [list(input().strip()) for _ in range(R)]
result = 1
stack = set(board[0][0])
move(0, 0, 1)
print(result)