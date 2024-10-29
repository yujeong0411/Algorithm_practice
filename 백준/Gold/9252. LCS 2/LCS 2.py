str1 = [""] + list(input().strip())
str2 = [""] + list(input().strip())
# print(str1)
N, M = len(str1), len(str2)
dp = [[''] * (M) for _ in range(N)]
for i in range(1, N):
    for j in range(1, M):
        if str1[i] == str2[j]:
            dp[i][j] = dp[i-1][j-1] + str1[i]
        else:
            if len(dp[i][j-1]) > len(dp[i-1][j]):
                dp[i][j] = dp[i][j-1]
            else:
                dp[i][j] = dp[i-1][j]
        # print(dp)
print(len(dp[N-1][M-1]))
print(dp[N-1][M-1])
