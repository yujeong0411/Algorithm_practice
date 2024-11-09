def cal(person):
    # print(visited)
    # 목표에 도달했다면 종료
    if person == p2:
        return

    # 현재노드와 관계 있는 노드 검사
    for i in relations[person]:
        if visited[i] == -1:  # 방문하지 않았다면
            visited[i] = visited[person]+1  # i번 노드의 촌수 = 현재 노드의 촌수 + 1
            cal(i)

n = int(input())  # 사람 수
p1, p2 = map(int, input().split())  # 계산해야 하는 사람들
m = int(input())  # 부모-자식 관계 수
visited = [-1 for _ in range(n+1)]
relations = [[] for _ in range(n+1)]
# 1촌 관계 연결하기
for _ in range(m):
    parents, child = map(int, input().split())
    # 촌수를 계산해야 하는 사람들이 꼭 부모-자식관계가 아니기 때문에 양방향 저장
    relations[parents].append(child)
    relations[child].append(parents)
# print("관계도 : ", relations)
# 관계도 [[], [2, 3], [1, 7, 8, 9], [1], [5, 6], [4], [4], [2], [2], [2]]

visited[p1] = 0   # 시작점 촌수를 0으로 설정
cal(p1)
print(visited[p2])
