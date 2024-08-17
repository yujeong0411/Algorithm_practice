T = int(input())
for test_case in range(1, T + 1):
    N = int(input())  # 전선의 개수
    cnt = 0
    wires = []   # 전선 정보
    for _ in range(N):
        A, B = map(int, input().split())
        wires.append((A, B))
        # 교차점 계산
    for i in range(N):  # 첫 번째 전서
        for j in range(i+1, N):  # 두 번째 전선, 겹치지 않게 검사
            A1, B1 = wires[i]
            A2, B2 = wires[j]
            if (A1 < A2 and B1 > B2) or (A1 > A2 and B1 < B2):
                cnt += 1
    print(f'#{test_case} {cnt}')