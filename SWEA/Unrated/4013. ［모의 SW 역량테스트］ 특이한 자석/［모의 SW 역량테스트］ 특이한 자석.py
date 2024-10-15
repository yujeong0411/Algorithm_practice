def wheel(num, dir):
    visited[num] = 1
    # 2번-6번 맞물림.
    # 2번 맞물림 처리(1, 2, 3번쨰 자석), 자성이 다르고 확인하지 않았다면
    if num < 3 and info[num][2] != info[num+1][6] and not visited[num+1]:
        wheel(num+1, -dir)  # 옆자석(반대방향)
    if num > 0 and info[num][6] != info[num-1][2] and not visited[num-1]:
        wheel(num-1, -dir)

    if dir == 1:  # 시계방향
        info[num] = [info[num].pop()] + info[num]  # 마지막 요소를 빼서 맨앞으로 보내기
    else:
        info[num] = info[num][1:] + [info[num][0]]  # 맨 앞의 요소를 빼서 맨 뒤로 보내기
    return

T = int(input())
for test_case in range(1, T + 1):
    K = int(input())  # 회전 수
    info = [list(map(int, input().split())) for _ in range(4)]
    # 1:S 0:N
    # 1:시계방향, -1:반시계방향
    for _ in range(K):
        num, dir = map(int, input().split())  # 자석번호, 방향
        visited = [0] * 4
        wheel(num-1, dir)

    result = 0
    for i in range(4):
        result += (info[i][0]) * (2**i)
    print(f'#{test_case} {result}')