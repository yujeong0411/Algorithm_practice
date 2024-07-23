T = int(input())
for test_case in range(1, T + 1):
    str_1 = input()
    str_list = list(str_1)

    str_list.reverse()
    re_str = ''.join(str_list)
    if re_str == str_1:
        result = 1
    else:
        result = 0
    print(f'#{test_case} {result}')