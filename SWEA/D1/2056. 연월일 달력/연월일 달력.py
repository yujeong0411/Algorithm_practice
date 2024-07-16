T = int(input())
for test_case in range(1, T + 1):
    num = str(input())                 # str으로 날짜 받기
    year = num[0:4]                    # 0000/00/00 날짜 단위로 인덱스 끊기
    month = num[4:6]
    day = num[6:]
    end_day = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # 월의 마지막일 

   
    if 0 < int(month) < 13 and 0 < int(day) <= end_day[int(month)]:   # str을 int로 변환하여 1~12월 제외 가리기
        print(f'#{test_case} {year}/{month}/{day}')
    else:
        print(f'#{test_case} -1')


