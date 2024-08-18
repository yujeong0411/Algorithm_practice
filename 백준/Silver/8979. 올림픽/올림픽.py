n, k = map(int, input().split())
rank = []									# 순서를 위한 배열

for _ in range(n):
    c, g, s, b = map(int, input().split())	# 나라, 금, 은, 동 순 입력
    rank.append((g, s, b))					# 메달만 rank 배열에 추가

    if c == k:								# 확인할 나라의 등수를 체크하기 위해
        tmp = (g, s, b)						# tmp에 해당 나라의 메달 수 저장

rank.sort(reverse=True)						# rank배열 내림차순으로 정렬

for i in range(n):
    if rank[i] == tmp:						# 순차적으로 rank를 탐색하며 찾아야 할 나라의 메달 수를 찾고
        print(i + 1)						# 해당 인덱스 + 1(순위)를 출력
        break