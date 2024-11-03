from collections import deque
def bfs(root):
    queue = deque([root])
    dep = 0 # 깊이 카운트

    while queue:
        cur = queue.popleft()  # 현재 노드
        # print('cur', cur, visited)
        # 현재 노드가 루트노드가 아니고, 리프노드일 경우
        if cur != 1 and len(tree[cur]) == 1:
            dep += visited[cur]  # 깊이 갱신
            continue

        # 현재 노드와 연결된 노드 찾기
        for next in tree[cur]:
            if not visited[next]:  # 방문하지 않은 노드라면
                visited[next] = visited[cur] + 1  # 다음 노드까지의 깊이 갱신
                queue.append(next)  # 다음 노드 추가
    return dep

N = int(input())  # 정점 개수
tree = [[] for _ in range(N+1)]  # 연결된 모든 노드 정보 저장
visited = [0] * (N+1)
for _ in range(N-1):
    a, b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)
# print(tree)

# 모든 노드의 깊이 찾기
depth = [[] for _ in range(N+1)]
result = bfs(1)
# print('r', result)
# 모든 리프노드까지의 깊이의 합이 홀수라면 이길 수 있다.
if result % 2 == 0:
    print('No')
else:
    print('Yes')

