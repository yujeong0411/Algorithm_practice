N = int(input())
arr = [[0]*1001 for _ in range(1001)]
num = 0
for _ in range(N):
    x, y, w, h = map(int, input().split())
    num += 1
    for i in range(y, y+h):
        for j in range(x, x+w):
            arr[i][j] = num


for n in range(1, N+1):
    cnt = 0
    for lst in arr:
        cnt += lst.count(n)
    print(cnt)