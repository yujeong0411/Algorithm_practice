from collections import deque
def check():
    queue = deque()
    for i in range(N+1):
        if num[i] == 0: # 선수과목이 없다면
            queue.append(i)
            semester[i] = 1  # 학기

    while queue:
        cur = queue.popleft() # 선수과목을 이수한 과목들
        for subject in S[cur]:  # 선수과목을 이수한 과목들을 처리
            num[subject] -= 1  # 선수과목 개수 -1 처리
            # subject의 최소 학기 - 선수과목 중 가장 큰 학기 이후에 이수 가능
            semester[subject] = max(semester[subject], semester[cur]+1)
            if num[subject] == 0:
                queue.append(subject)
    return semester[1:]  # 1번 과목부터 최소 학기 반환

N, M = map(int, input().split())  # 과목수, 조건
S = [[] for _ in range(N+1)]
num = [0] * (N+1)  # 선수과목 개수
semester = [0] * (N+1) # 과목을 이수할 수 있는 최소학기
for _ in range(M):
    a, b = map(int, input().split())  # 선수과목, 과목
    S[a].append(b)
    num[b] += 1
result = check()
print(*result)