H, W = map(int, input().split())
cloud = [input() for _ in range(H)]

arr = [[0]*W for _ in range(H)]
for i in range(H):
    cnt = -1
    for j in range(W):
        if cloud[i][j] == 'c':
            cnt = 0
        else:
            if cnt >= 0 :
                cnt += 1
        arr[i][j] = cnt
for lst in arr:
    print(*lst)