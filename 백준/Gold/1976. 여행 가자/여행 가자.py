def find(x):
    # x의 부모 노드가 자기 자신이면 해당 집합의 대표자이므로 x 반환
    if parents[x] == x:
        return x
    # x의 부모 노드를 재귀적으로 찾아 부모 테이블을 갱신하여 경로 압축
    parents[x] = find(parents[x])
    # print(parents, 'find')
    return parents[x]

def union(x, y):
    # x 와 y 의 대표자를 찾자.
    root_x = find(x)
    root_y = find(y)
    # 이미 같은 집합이라면 더 이상 할 필요 없음
    if root_x == root_y:
        return

    # 다른 집합이라면 더 작은 루트노드에 합친다.
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
    # print(parents, 'union')

N = int(input())  # 도시 수
M = int(input())  # 여행계획에 포함된 도시 수
arr = [list(map(int, input().split())) for _ in range(N)]  # 도시간 연결정보
parents = [i for i in range(N)]   # 부모 테이블
for i in range(N):
    for j in range(N):
        # 도시가 연결되어 있다면 같은 집합으로 묶기
        if arr[i][j] == 1:
            union(i, j)

plan = list(map(int, input().split()))  # 여행 계획
root = find(plan[0] - 1)  # 첫 번째 도시의 루트
# 첫 번째 도시와 다른 도시들이 같은 집합에 속하는지 확인
result = all(find(city - 1) == root for city in plan[1:])
# True면 YES, False면 NO
print('YES' if result else 'NO')

