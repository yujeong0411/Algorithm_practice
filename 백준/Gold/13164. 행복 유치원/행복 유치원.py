N, K = map(int, input().split())
student = list(map(int, input().split()))  # 원생 키
price = []  # 서로 인접한 원생들끼리 조일 때
for i in range(N-1):
    a = student[i+1] - student[i]
    price.append(a)
price.sort()   # 가장 큰 비용인 경우 제거하기
# N-1-x = K-1
print(sum(price[:N-K]))