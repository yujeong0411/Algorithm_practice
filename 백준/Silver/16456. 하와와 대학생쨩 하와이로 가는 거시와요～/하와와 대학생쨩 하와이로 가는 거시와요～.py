N = int(input())  # 섬 개수 입력
island = [0] * 50001  

# 초기 값 설정
island[0], island[1] = 1, 1  # 첫 번째 섬까지 가는 방법은 1가지
if N >= 2:
    island[2] = 1  # 두 번째 섬까지 가는 방법은 1가지
if N >= 3:
    island[3] = 2  # 세 번째 섬까지 가는 방법은 2가지

for i in range(4, N + 1):
    island[i] = (island[i - 1] + island[i - 3]) % 1000000009
print(island[N])
