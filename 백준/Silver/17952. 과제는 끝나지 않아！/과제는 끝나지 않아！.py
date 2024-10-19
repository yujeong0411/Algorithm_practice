from collections import deque

N = int(input())  # 전체 시간
current_score = current_min = 0
assignment = deque()  # 리스트 사용 시 시간초과 남.
result = 0
for _ in range(N):
    info = list(map(int, input().split()))
    # print(info, 'info')
    if current_min == 0:
        result += current_score
        current_score = 0

    if info[0] == 1:
        if current_min and current_score:
            assignment.append((current_score, current_min))
        current_score = info[1]
        current_min = info[2] - 1
    elif info[0] == 0:
        if current_score and current_min:
            current_min -= 1
        elif assignment:
            current_score, current_min = assignment.pop()
            current_min -= 1
    # print(current_score, current_min)
    # print(assignment, 'assignment')
if current_min == 0 and current_score:
    result += current_score
print(result)