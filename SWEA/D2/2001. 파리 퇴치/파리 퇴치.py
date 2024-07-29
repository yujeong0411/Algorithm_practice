T = int(input())	
for test_case in range(1, T + 1):
	N, M = list(map(int, input().split()))
	n_arr = [list(map(int,input().split())) for _ in range(N)]
	max_n = 0

	for i in range(N-M+1):  # M*M배열의 시작점은 N-M+1까지
		for j in range(N-M+1):
			cnt = 0  # 파리수 카운트
			for si in range(i, i+M):  # M*M배열은 시작점부터 (i+M)까지
				for sj in range(j, j+M):
					cnt += n_arr[si][sj]   # 파리수 더하기
			if cnt > max_n:
				max_n = cnt
                
	print(f'#{test_case} {max_n}')
