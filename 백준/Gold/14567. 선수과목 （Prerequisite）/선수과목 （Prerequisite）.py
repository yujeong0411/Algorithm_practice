from collections import deque


def find_min_semesters():
    queue = deque()
    # 선수 과목이 없는 과목들을 먼저 큐에 넣고, 1학기부터 시작
    for i in range(1, N + 1):
        if num[i] == 0:  # 진입 차수가 0 = 선수 과목이 없다는 의미
            queue.append(i)
            semester[i] = 1  # 선수 과목이 없으면 1학기에 이수 가능
    # 위상 정렬
    while queue:
        curr = queue.popleft()  # 큐에서 과목을 하나씩 꺼냄
        # 현재 과목(curr)의 다음에 들을 수 있는 과목들을 처리
        for next_sub in graph[curr]:
            num[next_sub] -= 1 # 선수 과목(curr)을 이수했으니 진입 차수를 1 줄임
            # next_sub 과목의 최소 학기를 갱신, 선수 과목 중 가장 큰 학기 이후에 이수 가능
            semester[next_sub] = max(semester[next_sub], semester[curr] + 1)
            # 선수 과목을 모두 이수한 과목은 큐에 추가
            if num[next_sub] == 0:
                queue.append(next_sub)

    return semester[1:]  # 1번 과목부터 N번 과목까지의 최소 학기 반환

# 입력 처리
N, M = map(int, input().split())  # 과목 수, 선수 조건 수
graph = [[] for _ in range(N + 1)]
num = [0] * (N + 1)  # 진입차수(선수 과목 개수)
semester = [0] * (N + 1)  # 과목을 이수할 수 있는 최소 학기

for _ in range(M):
    A, B = map(int, input().split())
    graph[A].append(B)  # A -> B (A는 B의 선수 과목)
    num[B] += 1

result = find_min_semesters()
print(" ".join(map(str, result)))
