N, M = map(int, input().split())  # 구멍 개수, 햄스터 부피
hamster = list(map(int, input().split()))

start, end = 0, 0
c_sum = 0
result = 0
while end < N:  # end가 N에 도달할 때까지 반복
    c_sum += hamster[end]  # 끝을 늘리며 크기 더하기

    while c_sum > M:  # M을 초과하면 start를 이동시켜 구간 변경
        c_sum -= hamster[start]  # start 값 빼기
        start += 1  # 오른쪽으로 한 칸 이동
        
    result = max(result, c_sum)  # 합이 M 이하인 경우, 최대값 갱신
    end += 1  # 끝을 오른쪽으로 한 칸 더 늘림.

print(result)


