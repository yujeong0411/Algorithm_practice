def find(x):
    if parents[x] == x:  # x 자기자신이 x 를 바라본다 == 해당 집합의 대표자
        return x
    parents[x] = find(parents[x])
    # print(parents, 'find')
    return parents[x]

def union(x, y):
    # x 와 y 의 대표자를 찾자.
    root_x = find(x)
    root_y = find(y)

    if root_x == root_y:  # 이미 같은 집합이면 끝
        return

    # 다른 집합이라면 더 작은 루트노드에 합친다.
    if root_x < root_y:
        parents[root_y] = root_x
    else:
        parents[root_x] = root_y
    # print(parents, 'union')

N = int(input())
M = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
parents = [i for i in range(N)]
for i in range(N):
    for j in range(N):
        # 도시가 연결되어 있다면 
        if arr[i][j] == 1:
            union(i, j)

plan = list(map(int, input().split()))
result = 'YES'
for i in range(1, M):
    if parents[plan[i]-1] != parents[plan[0]-1]:
        result = 'NO'
        break
print(result)
