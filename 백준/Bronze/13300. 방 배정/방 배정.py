# 성별 구분, 학년 구분
N, K = map(int, input().split())  # 총 학생 수, 한 방 최대 인원 수
arr = [[0, 0] for _ in range(7)]  # 학년별, 성별 따로 저장
for _ in range(N):
    s, grade = map(int, input().split())  # 성별(0여,1남), 학년
    arr[grade][s] += 1

cnt = 0
for lst in arr:
    for student in lst:
        # 학생수를 최대 인원수로 나누어 방 카운트
        if student % K == 0:  # 인원수로 나누어 떨어지면 
            cnt += student//K
        else:                # 인원수로 나누어 떨어지지 않는다면
            cnt += student//K + 1
print(cnt)
