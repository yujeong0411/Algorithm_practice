T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    di = [0, 1, 0, -1]  # 우, 하, 좌, 상
    dj = [1,0, -1, 0]
    d_idx = 0   # 델타 인덱스

    arr[0][0] = 1  # 첫번째 1로 설정
    i = j = 0
    num = 2
    while num <= N*N:   # 배열 안 숫자가 N*N보다 작을때 까지
        ni = i + di[d_idx]
        nj = j + dj[d_idx]
        # 배열을 벗어나지 않게 조건 설정
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] == 0:
            arr[ni][nj] = num
            i, j = ni, nj   # i, j 업데이트
            num += 1
        else:
            d_idx = (1+d_idx) % 4

    print(f'#{test_case}')
    for lst in arr:
        print(*lst)