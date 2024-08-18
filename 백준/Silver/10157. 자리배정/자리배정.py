C, R = map(int, input().split())
K = int(input())

if R*C < K:     # 배정이 불가능한 경우 0
    print(0)
else:           # 배정하면서 K가 되면 그때 좌표 출력
    di, dj = [1, 0, -1, 0], [0, 1, 0, -1]
    # 주변을 1로 둘러싸면: 범위체크 필요 없음
    arr = [[1]*(C+2)]+[[1]+[0]*C+[1] for _ in range(R)]+[[1]*(C+2)]

    ci, cj, dr = 1, 1, 0
    for n in range(1, K):
        arr[ci][cj] = n
        ni,nj = ci+di[dr], cj+dj[dr]
        if arr[ni][nj]==0:          # 비어있으니 이동가능
            ci,cj = ni,nj
        else:                       # 범위밖 또는 이미 기록한 위치
            dr = (dr+1)%4           # 방향 꺽기
            ci,cj = ci+di[dr], cj+dj[dr]
    print(f'{cj} {ci}')