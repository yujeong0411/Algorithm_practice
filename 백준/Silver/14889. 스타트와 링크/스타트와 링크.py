from itertools import combinations
# N은 항상 짝수이며, 두 팀은 각각 N//2명으로 구성
N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]
result = 21e8

#팀 조합
for start in combinations(range(N), N//2): # range(N)에서 N//2명의 멤보 조합 생성
    # print(start) -> start 리스트를 만들지 않아도 for문을 통해 변수로 바로 전달된다.
    # link = [i for i in range(N) if i not in start]
    link = []
    # 스타트 팀이 아닌 경우 링크 팀에 추가
    for i in range(N):
        if i not in start:
            link.append(i)

    # 능력치 구하기
    s_stat = l_stat = 0  # 스타트, 링크 팀의 능력치 초기화
    for i in range(N//2):
        for j in range(N//2):
            s_stat += synergy[start[i]][start[j]]
            l_stat += synergy[link[i]][link[j]]
    # 팀 별 능력치 차이 최소값 구하기
    result = min(result, abs(s_stat-l_stat))
print(result)
