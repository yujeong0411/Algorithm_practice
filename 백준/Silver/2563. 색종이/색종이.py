N = int(input())  # 색종이 수
arr = [[0]*100 for _ in range(100)]
for _ in range(N):
    x, y = map(int, input().split())  # 색종이 위치
    for i in range(y, 10+y):
        for j in range(x, 10+x):
            arr[i][j] = 1

result = 0
for lst in arr:
    result += lst.count(1)
print(result)