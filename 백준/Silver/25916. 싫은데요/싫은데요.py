N, M = map(int, input().split())  # 구멍 개수, 햄스터 부피
hamster = list(map(int, input().split()))  # 각 구멍의 크기

# 투 포인터 기법
start, end = 0, 0
current_sum = 0
max_volume = 0

while end < N:
    current_sum += hamster[end]
    
    # 현재 구간의 합이 M을 초과하면 start 포인터를 이동시켜 구간을 줄임
    while current_sum > M:
        current_sum -= hamster[start]
        start += 1
    
    # 현재 구간의 합이 M 이하일 때 최대값 갱신
    max_volume = max(max_volume, current_sum)
    
    end += 1

print(max_volume)
