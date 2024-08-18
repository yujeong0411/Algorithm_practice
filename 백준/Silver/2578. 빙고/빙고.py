def check(c, bingo):
    # 가로
    for i in range(5):
        if bingo[i] == [0] * 5:
            c += 1

    # 세로
    for i in range(5):
        if all(bingo[j][i] == 0 for j in range(5)):
            c += 1

    # 대각선
    if all(bingo[i][i] == 0 for i in range(5)):
        c += 1

    # 역대각선
    if all(bingo[i][4-i] == 0 for i in range(5)):
        c += 1
    return c

bingo = [list(map(int, input().split())) for _ in range(5)]
num = []
for _ in range(5):
    num += list(map(int, input().split()))
cnt = 0
c = 0
for n in range(25):
    for i in range(5):
        for j in range(5):
            if num[n] == bingo[i][j]:
                bingo[i][j] = 0
                cnt += 1
    if cnt >= 12:
        result = check(c, bingo)
        if result >= 3:
            print(n+1)
            break