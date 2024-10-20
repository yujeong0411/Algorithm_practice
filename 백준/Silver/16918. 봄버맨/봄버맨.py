def bomb(arr):
    new_arr = [['O'] * C for _ in range(R)]  # 모든 칸을 폭탄으로 채움
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'O':  # 폭발할 폭탄 위치
                new_arr[i][j] = '.'
                # 인접한 4방향도 파괴
                for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < R and 0 <= nj < C:
                        new_arr[ni][nj] = '.'
    return new_arr

R, C, N = map(int, input().split())
arr = [list(input().strip()) for _ in range(R)]

if N == 1:  # 1초 후: 초기 상태
    result = arr
elif N % 2 == 0:  # 짝수 초: 모든 칸이 폭탄
    result = [['O']*C for _ in range(R)]
else:  # 홀수 초: 폭발 후 상태
    if (N-1) % 4 == 2:  # 3, 7, 11... 초
        result = bomb(arr)
    else:  # 5, 9, 13... 초
        result = bomb(bomb(arr))

# 결과 출력
for row in result:
    print(''.join(row))