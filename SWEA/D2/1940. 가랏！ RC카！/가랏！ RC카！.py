T = int(input())
for test_case in range(1, T + 1):
    N = int(input())

    # 거리와 속도 초기화
    distance = 0
    speed = 0
    for _ in range(N):  # command 수만큼 반복
        command = list(map(int, input().split()))   # 반복할때마다 command를 받아야 함.
        if command[0] == 0:    # 0이면 속도 유지
            pass
        if command[0] == 1:     # 1이면 증가
            speed += command[1]
        elif command[0] == 2:   # 2이면 감소
            speed -= command[1]
            if speed < 0:    # 속도가 음수가 되면 0이 됨.
                speed = 0
        # 반복이 끝날 때마다 거리에 속도 더하기(N개의 커맨드로 N초 동안의 거리를 구하기 때문에 매초 속도만큼 이동함. )
        distance += speed   
    
    print(f'#{test_case} {distance}')