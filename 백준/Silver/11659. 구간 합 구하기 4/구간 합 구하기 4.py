import sys
input = sys.stdin.readline

N, M = map(int, input().split())
n_lst = list(map(int, input().split()))

# 누적합 리스트
total_sum = [0]
sub_sum = 0
for num in n_lst:
    sub_sum += num
    total_sum.append(sub_sum)

# 구간합 구하기
for _ in range(M):
    i, j = map(int, input().split())
    result = total_sum[j] - total_sum[i-1]
    print(result)