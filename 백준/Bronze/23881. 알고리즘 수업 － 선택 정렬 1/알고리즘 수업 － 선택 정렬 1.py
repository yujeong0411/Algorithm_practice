N, K = map(int, input().split())  # 배열 크기, 교환 횟수
a = list(map(int, input().split()))

cnt = 0  # 교환 횟수 카운트
for i in range(N - 1, 0, -1):
    max_idx = i
    for j in range(i):
        if a[j] > a[max_idx]:
            max_idx = j
    # 같을 때는 교환이 되지 않게 설정
    if max_idx != i:
        a[i], a[max_idx] = a[max_idx], a[i]
        cnt += 1
    if cnt == K:
        result = (a[max_idx], a[i])
        print(*result)
        break
if cnt < K:
    print(-1)