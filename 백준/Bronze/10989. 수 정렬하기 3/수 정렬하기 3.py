import sys
input = sys.stdin.readline

N = int(input())   # 수의 갯수
data = [0] * (10001)  # 최대 자연수
for _ in range(N):
    a = int(input())
    data[a] += 1   # 인덱스 값으로 해당 숫자의 갯수 카운트

for i in range(10001):  # 숫자를 뽑는데
    if data[i] != 0:   # 0인 값 건너뛰기
        for j in range(data[i]):  # 저장한 갯수만큼 해당 숫자 반복 출력
            print(i)

