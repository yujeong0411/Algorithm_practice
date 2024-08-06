# 스위치 바꾸는 함수
def change(idx):
    if switch[idx] == 1:
        switch[idx] = 0
    else:
        switch[idx] = 1
    return

N = int(input())
switch = [-1] + list(map(int, input().split()))
student = int(input())

for _ in range(student):
    s, num = map(int, input().split())
    if s == 1:   # 남자
        for i in range(num, N+1, num):  # 스위치 배수 간격
            change(i)
    else:   # 여자
        change(num)    # 받은 번호 스위치 반전
        for i in range(N//2):  # 검사할 갯수(양쪽)
            if num+i > N or num-i < 1:   # 유효한 스위치 인덱스는 1~N
                break
            if switch[num+i] == switch[num-i]:   # 대칭이 같으면
                change(num+i)
                change(num-i)
            else:
                break

for i in range(1, N+1):
    print(switch[i], end=' ')
    if i % 20 == 0:   # 21개부터 줄바꿈
        print()