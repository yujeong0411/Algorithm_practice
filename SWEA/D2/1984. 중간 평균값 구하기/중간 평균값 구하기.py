# T = int(input())
# for test_case in range(1, T + 1):
#     N = int(input())
#     num = list(map(int, input().split()))
#
#     while True:
#
#
#     print(f'#{test_case} {}')

T = int(input())
for test_case in range(1, T + 1):
    num = list(map(int, input().split()))

    max_idx = 0
    min_idx = 0
    sum_n = 0
    for idx in range(10):   # 총 10개의 수만 입력받음
        if num[max_idx] < num[idx]:   # 최댓값
            max_idx = idx
        if num[min_idx] > num[idx]:   # 최솟값
            min_idx = idx

        sum_n += num[idx]   # 전체 합
    result = (sum_n - num[min_idx] - num[max_idx])/8   # 최대, 최소를 뺀 평균
    print(f'#{test_case} {int(round(result,0))}')