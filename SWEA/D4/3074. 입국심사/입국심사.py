# 이진탐색 !!
# 이분 탐색의 경우 답으로 계산해야하는 대상이 이분 탐색의 기준이 되는 경우가 많다.
# 구해야하는 값 = 최소 심사 시간
def binary_search(time, M):
    min_time = min(time)  # 임의의 최소시간
    max_time = max(time) * M  # 최대 소요 시간, 긴 심사대가 모든 사람을 심사하는 경우
    result = 0
    while min_time <= max_time:
        mid_time = (min_time + max_time) // 2  # 중간값
        people = 0  # mid_time 동안 심사한 사람 수
        for t in time:    # 중간값으로 검사
            people += mid_time // t  # 전체시간 // 각 심사대 시간 = 각 심사대 사람 수
            if people >= M:  # mid_time 동안 M명 이상 심사가능한 경우면 OK
                break
        if people >= M:  # 심사한 사람 수가 심사 받아야 할 수 보다 많은 경우
            result = mid_time
            max_time = mid_time - 1
        else:  # 심사한 사람 수가 심사 받아야 할 수보다 적은 경우
            min_time = mid_time + 1

    return result

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())  # 심사대 수(1~N번), 사람 수
    time = [int(input()) for _ in range(N)]  # 심사 시간
    result = binary_search(time, M)
    print(f'#{test_case} {result}')