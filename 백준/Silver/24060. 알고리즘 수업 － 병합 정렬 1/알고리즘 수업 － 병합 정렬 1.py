def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2
        merge_sort(A, p, q)      # 전반부 정렬
        merge_sort(A, q + 1, r)  # 후반부 정렬
        merge(A, p, q, r)        # 병합


def merge(A, p, q, r):
    global count, result_k
    i = p
    j = q + 1
    t = 0
    tmp = [0] * (r - p + 1)  # 임시 배열 생성

    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp[t] = A[i]
            i += 1
        else:
            tmp[t] = A[j]
            j += 1
        t += 1
        count += 1
        if count == K:
            result_k = tmp[t-1]

    while i <= q:
        tmp[t] = A[i]
        i += 1
        t += 1
        count += 1
        if count == K:
            result_k = tmp[t-1]

    while j <= r:
        tmp[t] = A[j]
        j += 1
        t += 1
        count += 1
        if count == K:
            result_k = tmp[t-1]

    # 결과를 원본 배열 A에 복사
    for i in range(t):
        A[p + i] = tmp[i]


# 입력 처리
N, K = map(int, input().split())
A = list(map(int, input().split()))

# 전역 변수 초기화
count = 0
result_k = -1

# 병합 정렬 수행
merge_sort(A, 0, N - 1)

# 결과 출력
print(result_k if result_k != -1 else -1)
