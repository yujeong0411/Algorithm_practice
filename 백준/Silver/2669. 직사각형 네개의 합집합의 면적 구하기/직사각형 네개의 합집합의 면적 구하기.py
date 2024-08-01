arr = [[0 for _ in range(100)] for _ in range(100)]

# 좌표 입력받기
for i in range(4):
    a, b, c, d = map(int, input().split())  
    for i in range(b, d):     # x = j, y = i
        for j in range(a, c):
            arr[i][j] = 1    # 해당 면적을 1로 바꾸기

# 면적 구하기(배열에서 1인 부분)
area = 0
for lst in arr:
    for k in lst:
        area += k
print(area)