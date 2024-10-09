import sys
from heapq import heappop, heappush
# 정렬없이 중간값에 접근하려면 중간 값을 기준으로 최대힙과 최소힙으로 나누어서 저장
N = int(input())  # 정수 개수
left_heapq = []  # 최대힙
right_heapq = []  # 최소힙
for i in range(N):
    # n = int(input())
    n = int(sys.stdin.readline().strip())
    # left 부터 넣을 때, left와 right의 길이가 같으면 left 차례
    if len(left_heapq) == len(right_heapq):
        heappush(left_heapq, -n)
    else:
        heappush(right_heapq, n)

    # left는 작은 값들 중 가장 큰 값이 pop
    # right는 큰 값들 중 가장 작은 값이 pop
    # 이때 leftheapq > rightheapq 라면 두 수의 자리를 바꾼다.
    if right_heapq and right_heapq[0] < -left_heapq[0]:
        r_value = heappop(right_heapq)
        l_value = heappop(left_heapq)
        heappush(right_heapq, -l_value)
        heappush(left_heapq, -r_value)
    # print(left_heapq, 'l')
    # print(right_heapq, 'r')
    print(-left_heapq[0])