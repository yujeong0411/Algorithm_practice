def c(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i] != lst[i - 1]:
                cnt += 1
    return cnt

N = int(input())  # 색종이 수
arr = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())  # 색종이 위치
    for i in range(y, 10+y):
        for j in range(x, 10+x):
            arr[i][j] = 1

arr2 = list(map(list, zip(*arr)))
result = c(arr) + c(arr2)
print(result)



