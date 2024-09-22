from heapq import heappush, heappop

# 입력 받기
N, M, L = map(int, input().split())  # N: 현재 휴게소 수, M: 추가할 휴게소 수, L: 고속도로 길이

if N == 0:  # 휴게소가 없는 경우
    rest = []
else:
    rest = list(map(int, input().split()))  # 휴게소 위치 입력
    rest.sort()  # 휴게소 위치 정렬

distance = []  # 거리 저장, (거리, 구간 개수)

# 휴게소가 없는 경우, 전체 구간을 고속도로의 시작 ~ 끝으로 간주하고 구간을 나눔
if N == 0:
    heappush(distance, (-L, 1))  # 고속도로 전체 구간 L을 하나의 구간으로 처리
else:
    # 시작 지점 ~ 첫 번째 휴게소 구간
    heappush(distance, (-rest[0], 1))

    # 휴게소들 사이 거리 계산
    for i in range(1, N):
        heappush(distance, (-(rest[i] - rest[i-1]), 1))

    # 마지막 휴게소 ~ 끝 지점 구간 추가
    heappush(distance, (-(L - rest[-1]), 1))

# 휴게소 추가 과정
for _ in range(M):  # 휴게소 세우기
    max_distance, section = heappop(distance)  # 가장 긴 구간을 꺼냄
    max_distance = -(max_distance) * section   # 초기 구간 길이
    heappush(distance, (-max_distance / (section + 1), section + 1))  # 나눈 구간 다시 추가

# 최종적으로 가장 긴 구간을 결과로 출력
result = -heappop(distance)[0]
if result == int(result):
    print(int(result))
else:
    print(int(result) + 1)  # 소수점이 있는 경우 올림 처리
