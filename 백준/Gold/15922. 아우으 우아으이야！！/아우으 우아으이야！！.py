N = int(input())  # 선분 개수
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort()  # 시작점 기준으로 정렬
total = 0  # 전체 합계
start = arr[0][0]  # 처음 기준점
end = arr[0][1]

for i in range(1, N):
    x, y = arr[i][0], arr[i][1]
    if x <= end: # 선분이 겹치면
        if end < y:
            end = y
    else:  # 겹치지 않는다면
        total += end - start # 이전 선분길이 추가
        start, end = x, y  # start, end 값 갱신
total += end - start # 마지막 선분 더하기
print(total)



