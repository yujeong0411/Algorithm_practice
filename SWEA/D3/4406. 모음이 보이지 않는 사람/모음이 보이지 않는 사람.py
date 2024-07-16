T = int(input())
for test_case in range(1, T + 1):
    word = input()    # 단어 받기
    vowel = ['a', 'e', 'i', 'o', 'u']   # 모음 리스트
    
    result = ''                                # 결과 변수 초기화
    for i in word:                           # 
        if i in vowel:
            continue
        else:
            result += i
    
    print(f'#{test_case}', result)