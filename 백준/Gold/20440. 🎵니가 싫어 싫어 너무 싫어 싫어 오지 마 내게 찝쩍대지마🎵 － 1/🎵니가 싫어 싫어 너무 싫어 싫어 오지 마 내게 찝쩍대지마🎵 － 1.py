N = int(input())  # 모기 수
mosquito = {}
for _ in range(N):
    start, end = map(int, input().split())
    # 시간대가 없다면 추가
    if start not in mosquito:
        mosquito[start] = 0
    if end not in mosquito:
        mosquito[end] = 0
    mosquito[start] += 1  # 시작시간에 모기 추가
    mosquito[end] -= 1  # 종료 시간에 감소 
# print(mosquito)

# 최대 모기수, 현재 모기수, 시작시간, 종료 시간
max_mosquito = current_mosquito = start_time = end_time = 0
flag = False  # 최대 구간 여부 확인 
for time in sorted(mosquito.keys()):  # 시간을 오름차순으로 정렬 
    current_mosquito += mosquito[time]  # 현재 모기수 갱신
    if current_mosquito > max_mosquito:  # 최대 모기수 갱신
        max_mosquito = current_mosquito
        start_time = time
        flag = True  # 최대 구간 시작
    # 모기 수가  줄어들면 종료 
    if flag and current_mosquito < max_mosquito:
        end_time = time
        flag = False
print(max_mosquito)
print(start_time, end_time)
