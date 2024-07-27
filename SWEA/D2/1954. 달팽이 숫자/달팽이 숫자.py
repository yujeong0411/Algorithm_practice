T = int(input())
for test_case in range(1, T + 1):
    N = int(input()) 
    
    # 0으로 된 N*N 배열 생성
    arr = [[0 for _ in range(N)] for _ in range(N)]

    # x축, y축 방향 전환
    di = [0, 1 ,0, -1]
    dj = [1, 0 ,-1, 0]

    num = 1
    i, j = 0, 0
    d_idx = 0  # di, dj의 인덱스
    arr[i][j]= num   # 먼저 (0,0) 값 지정
    num += 1
    while num <= N*N:   # num는 배열의 칸 갯수까지 가능
        i_idx = i + di[d_idx]  # 다음 순서 인덱스
        j_idx = j + dj[d_idx]
        if 0 <= i_idx < N and 0 <= j_idx < N and arr[i_idx][j_idx] == 0:
                i, j = i_idx, j_idx
                arr[i][j]= num  
                num += 1
        else:       # 배열 방향 전환
            d_idx = (d_idx + 1) % 4  # d_idx 0에서 3까지 인덱스 돌리기
        
    print(f'#{test_case}')
    for list in arr:
        print(*list)
        