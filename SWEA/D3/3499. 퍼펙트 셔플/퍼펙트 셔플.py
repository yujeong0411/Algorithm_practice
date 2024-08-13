T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    card = input().split()

    shuffle = []
    for i in range(N//2):
        shuffle.append(card[i])
        shuffle.append(card[(N+1)//2+i])   # 홀수일 경우 N+1로 인해 먼저 놓는 쪽에 한 장 더 들어간다.
    if N % 2 != 0:
        shuffle.append(card[N//2])  # N이 홀수일 경우 중간 card[N//2]의 숫자가 들어가지 않으므로 추가
    print(f'#{test_case} {" ".join(shuffle)}')