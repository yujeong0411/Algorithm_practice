test = int(input())
for tc in range(1, test+1):
    height = list(map(int, input().split()))[1:]
    cnt = 0
    for i in range(1, 20):
        for j in range(i):
            if height[i] < height[j]:
                cnt += 1
    print(f'{tc} {cnt}')