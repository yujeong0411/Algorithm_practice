def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])  # 경로 압축
    return parents[x]

def union(x, y):
    root_x = find(x)
    root_y = find(y)
    if root_x != root_y:  # 같은 집합이 아니면 합치기
        parents[root_y] = root_x

N = int(input())  # 도시 수
M = int(input())  # 여행계획에 포함된 도시 수
arr = [list(map(int, input().split())) for _ in range(N)]  # 도시간 연결 정보
parents = list(range(N))  # 부모 테이블 초기화

# 연결된 도시들을 같은 집합으로 묶기
for i in range(N):
    for j in range(i + 1, N):  # 대칭 행렬이므로 절반만 확인
        if arr[i][j] == 1:
            union(i, j)

plan = list(map(int, input().split()))  # 여행 계획
root = find(plan[0] - 1)  # 첫 번째 도시의 루트
result = all(find(city - 1) == root for city in plan[1:])  # 모든 도시가 같은 루트인지 확인

print("YES" if result else "NO")