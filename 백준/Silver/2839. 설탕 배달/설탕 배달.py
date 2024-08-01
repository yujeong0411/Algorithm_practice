N = int(input())

cnt = 0
while N>=0:
    if N % 5 == 0:   # 5kg 봉지로 가능하다면
       cnt += N // 5
       print(cnt)
       break

    N -= 3    # 5kg 봉지가 안되면 3kg 봉지 하나쓰기
    cnt += 1

else:
    print(-1)