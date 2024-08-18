N, M = map(int, input().split())  # N장 카드, 외치는 숫자 M
card = list(map(int, input().split()))
# 카드 3장 합이 M에 가깝게

result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum_v = card[i] + card[j] + card[k]   # 세 카드의 합
            if result < sum_v <= M:
                result = sum_v
print(result)