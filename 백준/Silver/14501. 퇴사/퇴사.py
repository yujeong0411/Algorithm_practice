def backtracking(day, total_wage):
    global result
    if day > N:  # 퇴사날이면
        result = max(result, total_wage)  # 최대 수익
        return
    else:   # 마지막 날이 아니면 일..
        # 오늘 일하고, 다음에도 일 할 수 있다면(퇴사일 이전이라면)
        if day + schedule[day][0] <= N+1:  # 최대 N+1까지 일을 끝내야한다.(일이 없어야 한다.)
            backtracking(day+schedule[day][0], total_wage+schedule[day][1])  # 다음 일하는 날, 전체 수익+오늘 수익
        # 오늘말고 다음 날 일하는 경우
        # 최대 수익을 위해 모든 경우 탐색
        backtracking(day+1, total_wage)

N = int(input())  # 일하는 날
schedule = [(0,0)]   # 인덱스와 날짜 맞추기 위해 인덱스 0값 추가
for s in range(N):
    day, wage = map(int, input().split())  # 날짜, 금액
    schedule.append((day, wage))

result = 0
backtracking(1, 0)
print(result)

