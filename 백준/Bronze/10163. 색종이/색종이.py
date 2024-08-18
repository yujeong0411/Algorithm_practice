N = int(input())
arr = [[0]*101 for _ in range(101)]
num = 0
for _ in range(N):
    x, y, w, h = map(int, input().split())
    num += 1
    for i in range(y, y+h):
        for j in range(x, x+w):
            arr[i][j] = num

result = [0] * N
for i in range(101):
    for j in range(101):
        for k in range(1, N+1):
            if arr[i][j] == k:
                result[k-1] += 1

print(*result)