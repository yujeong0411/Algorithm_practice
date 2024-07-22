T = int(input())
for test_case in range(1, T + 1):
    n = list(map(int, input().split()))
    n_sum = 0
    for i in n:
        n_sum += i

    average = round(n_sum/10)
    
    print(f'#{test_case} {average}')
