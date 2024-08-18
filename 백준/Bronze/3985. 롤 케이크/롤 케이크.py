L = int(input())
N = int(input()) # 방청객수
cake = [1] * (L+1)  # 방청객이 받는 케이크 카운트
cake_max = people = 0
real_max = real_people = 0
for i in range(1, N+1):
    P, K = map(int, input().split())  # 원하는 조각 번호
    if cake_max < K-P+1:  # 기대한 방청객
        cake_max, people = K-P+1, i

    cnt = sum(cake[P:K+1])   #실제로 가져간 케이크 수
    if real_max < cnt:
        real_max, real_people = cnt, i
    cake[P:K+1] = [0]*(K-P+1)

print(people)
print(real_people)
