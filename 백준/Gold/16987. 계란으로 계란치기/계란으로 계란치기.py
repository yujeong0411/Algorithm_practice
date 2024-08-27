def backtracking(idx):
    global result
    # 종료 조건
    if idx == N:   # 마지막 계란이면 종료
        cnt = 0
        for lst in eggs:
            for n in lst:
                if n <= 0:
                    cnt += 1
        result = max(result, cnt)
        return

    # 내구도 = 내구도 - 상대 무게, 0이하가 되면 깨진다.
    # 계란이 깨졌거나 깨지지않아도 무조건 넘어간다.
    # 옆에 있는 계란을 깨는 것이 아닌 여러 계란 중 하나를 깨는 것
    if eggs[idx][0] > 0: # 깨지지 않았다면
        check = False  # 계란을 치지 않음.
        for i in range(N): # 다른 계란 치기
            if i != idx and eggs[i][0] > 0: # 계란이 자기 자신이 아니고, 깨지지 않았다면
                check = True # 계란을 침
                eggs[idx][0] -= eggs[i][1]  # 내구도 계산
                eggs[i][0] -= eggs[idx][1]
                backtracking(idx+1)  # 다음 계란 치기
                eggs[idx][0] += eggs[i][1]  # 되돌리기
                eggs[i][0] += eggs[idx][1]
        if not check:  # 어떠한 계란도 치지 않았다면(손에든 계란 제외 모두 깨진 경우)
            backtracking(idx + 1)
    else: # 깨졌다면 가장 최근에 든 계란의 한 칸 오른쪽 계란으로 진행
        backtracking(idx+1)

N = int(input())  # 계란 개수
eggs = []
for _ in range(N):
    S, W = map(int, input().split())  # 내구도, 무게
    eggs.append([S, W])

result = 0  # 최대 계란 개수
backtracking(0)  # 가장 왼쪽 계란부터 시작
print(result)
