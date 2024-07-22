T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    n_sum = 0
    for i in range(10):
        if n[i] % 2 != 0:
            n_sum += n[i]

    print(f'#{test_case} {n_sum}')

