from itertools import combinations
N = int(input())  # 재료 개수
flavor = [list(map(int, input().split())) for _ in range(N)] # 신맛, 쓴맛
result = 21e8  # 신맛, 쓴맛 차이
# 재료 조합
for i in range(1, N+1):  # 재료는 1개부터 N개까지 사용
    for combs in combinations(flavor, i):  # 재료 조합
        # print(combs)
        S, B = 1, 0  # 신맛은 곱, 쓴맛은 합
        for s, b in combs:
            S *= s
            B += b
        result = min(result, abs(S-B))  # 최소값 갱신
print(result)

