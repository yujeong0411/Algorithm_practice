N = int(input())  # 기둥 개수
N_lst = [0] * 1001
L_lst = [] # 위치 저장
for _ in range(N):
    L, H = map(int, input().split())  # 위치 높이
    N_lst[L] = H
    L_lst.append(L)

M = N_lst.index(max(N_lst))  # 가장 큰 기둥 위치
result = 0

# 가장 큰 기둥까지의 왼쪽 부분 계산
pre_pillar = 0
for i in range(min(L_lst), M+1):
    if N_lst[i] > pre_pillar:
        pre_pillar = N_lst[i]
    result += pre_pillar

# 가장 큰 기둥 이후 오른쪽 부분 계산
pre_pillar = 0
for i in range(max(L_lst), M, -1):
    if N_lst[i] > pre_pillar:
        pre_pillar = N_lst[i]
    result += pre_pillar

print(result)
