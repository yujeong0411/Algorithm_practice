N = int(input())  # 재료 개수
flavor = [list(map(int, input().split())) for _ in range(N)] # 신맛, 쓴맛
result = 21e8  # 신맛, 쓴맛 차이
for comb in range(1, 1 << N):  # 재료는 1개부터 시작, 2^N-1가지 경우의 수
    S, B = 1, 0  # 신맛은 곱, 쓴맛은 합
    for i in range(N):
        if comb & (1 << i) != 0:  # comb의 i번째 비트가 1이면 해당 재료 선택
            S *= flavor[i][0]
            B += flavor[i][1]
    result = min(result, abs(S-B))
print(result)