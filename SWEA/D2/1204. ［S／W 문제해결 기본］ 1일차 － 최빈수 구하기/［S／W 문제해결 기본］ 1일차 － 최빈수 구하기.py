T = int(input())
for test_case in range(1, T + 1):
    test_case = int(input())
    scores = list(map(int, input().split()))

    # 인덱스 = 점수, 빈도수 카운트
    max_idx = 0
    score_lst = [0] * 101
    for score in scores:
        score_lst[score] += 1

    for i in range(len(score_lst)):
        if score_lst[max_idx] <= score_lst[i] and max_idx <= i:
            max_idx = i

    print(f'#{test_case} {max_idx}')