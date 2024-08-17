N = int(input())  # 주사위 최대갯수
dice = [list(map(int, input().split())) for _ in range(N)]  # 주사위 종류
# A-F, B-D, E-C 마주보는
# A, B, C, D, E, F = 0 ~ 5
# 마주보는 숫자 인덱스
across_num = {0 : 5, 1 : 3, 2 : 4, 3 : 1, 4 : 2, 5 : 0}


result = 0  # 한면의 최대합구하기
# 첫 번째 주사위에서 윗면 뽑기
for k in range(6):  # 주사위 숫자 1~6
    top = dice[0][k]

    sub_sum = 0  # 한면의 최대합구하기
    for i in range(N):
        for j in range(6):
            if dice[i][j] == top:
                bottom = dice[i][across_num[j]]
                if 6 in (top, bottom): # 윗-아랫면에 5가 포함되어 있으면
                    if 5 in (top, bottom):  # 그 다음 가장 큰 숫자 더하기
                        sub_sum += 4
                    else: sub_sum += 5
                else:   # 6이 포함되어 있지 않으면 가장 큰 숫자는 6
                    sub_sum += 6
        top = bottom   # 윗면 바꿔주기
    result = max(sub_sum, result)

print(result)