N, K = map(int, input().split())  # 가치
dp = [ 0 for _ in range(K+1)]  # 배낭무게=인덱스, 최대 가치 저장
for _ in range(N):
    W, V = map(int, input().split())  # 무게, 가치
    for i in range(K, -1, -1):
        if W <= i:
            # 물건을 담지 않으면, dp[i]유지
            # 물건을 담았을 때, 남은 공간(i-W)의 최대 가치 계산
            dp[i] = max(dp[i], dp[i-W]+V)
            # print(dp)
print(dp[K])