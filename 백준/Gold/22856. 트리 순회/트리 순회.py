import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)

def inorder(v):
    global cnt
    # 현재 노드의 왼쪽 자식이 존재하고 방문하지 않았다면
    if tree[v][0] != -1 and not visited[tree[v][0]]:
        cnt += 1  # 이동 횟수 증가
        inorder(tree[v][0])  # 왼쪽 자식 노드로 재귀 호출하여 이동

    visited[v] = True  # 현재 노드 방문 처리

    # 현재 노드가 마지막 노드라면 종료
    if v == last:
        print(cnt)  # 이동 횟수 출력
        return

    # 현재 노드의 오른쪽 자식이 존재하고 방문하지 않았다면
    if tree[v][1] != -1 and not visited[tree[v][1]]:
        cnt += 1  # 이동 횟수 증가
        inorder(tree[v][1])  # 오른쪽 자식 노드로 재귀 호출하여 이동
    
    cnt += 1  # 자식 노드가 없고 부모 노드로 돌아가는 경우 이동 횟수 증가

# 입력 받기
N  = int(input())  # 트리의 노드 개수 입력
tree = [[] for _ in range(N+1)]  # 트리 정보를 저장할 리스트 초기화
visited = [False] * (N+1)  # 노드의 방문 여부를 저장할 리스트 초기화
cnt = 0  # 이동 횟수 초기화

# 트리 정보 입력 받기
for _ in range(N):
    a, b, c = map(int, input().split())  # 현재 노드 a, 왼쪽 자식 b, 오른쪽 자식 c
    tree[a] = [b, c]  # 노드 a의 왼쪽, 오른쪽 자식 정보 저장

# 중위 순회의 마지막 노드를 찾기
i = 1  # 루트 노드부터 시작
last = 1  # 마지막 노드를 저장할 변수 초기화
while True:
    if tree[i][1] == -1:  # 오른쪽 자식이 없는 경우
        last = i  # 현재 노드가 마지막 노드
        break
    i = tree[i][1]  # 오른쪽 자식이 있는 경우 계속 탐색

# 유사 중위 순회 시작
inorder(1)  # 루트 노드(1번 노드)부터 시작
