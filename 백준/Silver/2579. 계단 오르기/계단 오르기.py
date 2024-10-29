N = int(input())  # 계단 수
stairs = [int(input()) for _ in range(N)]
dp = [0] * N
for i in range(N):
    if i == 0:
        dp[i] = stairs[0]
    elif i == 1:
        dp[i] = stairs[0] + stairs[1]
    else:
        dp[i] = max(dp[i-2] + stairs[i], dp[i-3] + stairs[i-1] + stairs[i])

print(dp[-1])