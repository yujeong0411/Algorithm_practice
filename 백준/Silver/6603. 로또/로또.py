def subset(lst, idx, length, comb):
    if length == 6:  # 6개의 요소가 되면 출력
        print(' '.join(map(str, comb)))
        return

    for i in range(idx, len(lst)):
        comb.append(lst[i])  # 현재 요소 조합에 추가
        subset(lst, i+1, length+1, comb)
        comb.pop()  # 다시 제거

while True:
    S = input().split()
    k = int(S[0])  # 집합의 크기
    sub_lst = list(map(int, S[1:]))  # 요소, 리스트 저장
    if k == 0:
        break

    subset(sub_lst, 0, 0, [])
    print()
