def travel(start, j, cost):
    global result
    # 모두 방문 했다면 종료
    if all(visited):
        # 마지막 도시에서 첫번째 도시로 갈 수 있다면, 최소비용 갱신
        if costs[j][start] > 0:
            result = min(result, cost + costs[j][start])  
        return  

    # 다음 도시 찾기
    for next in range(N):
        # 방문하지 않은 도시이며, 이동할 수 있는 도시인 경우
        if not visited[next] and costs[j][next] > 0:
            visited[next] = 1
            travel(start, next, cost + costs[j][next])
            visited[next] = 0

N = int(input())  # 도시 수
costs = [list(map(int, input().split())) for _ in range(N)]  # 비용
result = 21e8  # 최소 비용 초기화
# 출발 도시
for i in range(N):
    visited = [0] * N  # 방문 표시 배열
    visited[i] = 1
    travel(i, i, 0)

print(result)