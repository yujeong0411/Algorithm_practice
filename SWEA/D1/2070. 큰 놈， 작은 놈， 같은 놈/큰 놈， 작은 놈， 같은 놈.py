T = int(input())
for test_case in range(1, T + 1):
    n, m = list(map(int, input().split()))

    if n > m:
        print(f'#{test_case} >')
    elif n < m :
        print(f'#{test_case} <')
    else:
        print(f'#{test_case} =')   
