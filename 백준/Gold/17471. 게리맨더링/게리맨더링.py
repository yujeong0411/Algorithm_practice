from itertools import combinations

def check(group):  # 그룹 연결성 확인 및 인구수 저장
    queue = []
    queue.append(group[0])
    visited[group[0]] = 1
    sumV = 0
    while queue:
        area = queue.pop()
        sumV += people[area]  # 꺼낸 구역의 인구수 더하기
        for i in info[area]:  # 해당 구역과 인접 구역 확인
            if i in group and visited[i] == 0:  # 그룹내에 있꼬 방문하지 않았다면 방문처리
                visited[i] = 1
                queue.append(i)

    # 그룹 내 구역이 인접한지 확인
    for i in group:
        if visited[i] == 0:
            return -1
    return sumV

N = int(input())  # 구역 수
people = [0] + list(map(int, input().split()))  # 인구 수
info = [[] for _ in range(N+1)]  # 인접구역
for i in range(1, N+1):
    a = list(map(int, input().split()))
    info[i].extend(a[1:])
# print(info)
result = 21e8
# 선거구 나누기
for i in range(1, (N//2)+1):
    for k in combinations(range(1, N+1), i):
        A = list(k)
        B = [i for i in range(1, N+1) if i not in A]  # A에 속하지 않은 선거구
        visited = [0]*(N+1)
        # print(B, 'B')
        # print(A, 'A')
        a = check(A)
        b = check(B)
        if a != -1 and b != -1:  # 두 선거구 모두 연결되어 있다면 
            result = min(result, abs(a-b))
if result == 21e8:
    print(-1)
else:
    print(result)