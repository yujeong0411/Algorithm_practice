N = input()
light = [0] + list(N)   # 전구 번호 = 인덱스 번호
cnt = 0
for i in range(1, len(light)):
    if light[i] == 'Y':   # 전구가 켜져있다면
        cnt += 1
        for j in range(i, len(light), i):  # 배수만큼 바꾸기
            if light[j] == 'Y':
                light[j] = 'N'
            else:
                light[j] = 'Y'

if 'Y' not in light:   # 켜진 전구가 없다면
    print(cnt)
else:       # 켜진 전구가 있다면
    print(-1)