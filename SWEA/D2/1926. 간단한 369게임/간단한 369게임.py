N = int(input())
for num in range(1, N+1):
    if '3' in str(num) or '6' in str(num) or '9' in str(num):   # 숫자 안에 369가 있는지 검사
        clap = str(num).count('3') + str(num).count('6') + str(num).count('9')  # 369 숫자 갯수를 count 해서 출력 
        print('-' * clap, end=' ')
    else:
        print(num, end=' ')