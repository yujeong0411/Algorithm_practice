T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0] * (N+1) for _ in range(N+1)]   # N+1 : padding

    arr[1][1] = 1
    for i in range(2, N+1): 
        for j in range(1, i+1):   # i = 열 길이
            arr[i][j] = arr[i-1][j] + arr[i-1][j-1]  

    print(f'#{test_case}')
    for i in range(1, N+1):
        for j in range(1, i+1):
            print(arr[i][j], end=' ')
        print()