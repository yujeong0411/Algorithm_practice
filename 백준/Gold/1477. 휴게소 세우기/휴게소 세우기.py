from heapq import heappush, heappop
# 최댓값의 최소화:
# 문제에서 휴게소를 추가한 후 "휴게소가 없는 구간의 최댓값"을 최소화하는 것이 목표입니다. 즉, 휴게소 간의 거리가 균일해질수록 가장 긴 구간이 짧아지며, 최댓값을 줄일 수 있습니다.
# 최댓값을 최소화하려면, 구간이 편차 없이 골고루 나누어져야 하기 때문에 휴게소 간의 거리를 최대한 균등하게 만들어야 합니다.
N, M, L = map(int, input().split())
if N == 0:  # 휴게소가 없는 경우
    rest = []
else:
    rest = list(map(int, input().split()))
    rest.sort()  # 휴게소 순서대로 정렬

distance = []  # 거리 저장, (거기, 구간 개수)
if N == 0: # 휴게소가 없는 경우
    heappush(distance, (-L, 1))  # 전체 구간을 하나의 구간으로 처리 
else:  # 기존 휴게소가 있을 때
    heappush(distance, (-rest[0], 1))  # 시작 지점 ~ 첫 번째 휴게소 거리
    for i in range(1, N):
        heappush(distance, (-(rest[i]-rest[i-1]), 1))
    heappush(distance, (-(L-rest[-1]), 1)) # 마지막 휴게소 ~ 끝 지점 거리
    # print(distance)

for _ in range(M):  # 휴게소 세우기
    max_distance, section = heappop(distance)  # 최대 거리, 구간 개수
    max_distance = -(max_distance) * section   # 초기 구간 길이
    heappush(distance, ((-max_distance/(section+1)), section+1))
    # print(distance)

result = -heappop(distance)[0]  # 최댓값 출력
if result == int(result):
    print(int(result))
else:
    print(int(result)+1)  # 소수점이 있는 경우 올림 처리(가장 긴 길이를 구하기 때문)