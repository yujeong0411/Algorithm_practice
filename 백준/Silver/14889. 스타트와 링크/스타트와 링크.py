def member(num, start, link):
    global result
    if num == N:  # N명이 모두 팀을 나누었을 때
        if len(start) == N//2:  # 스타트팀의 멤버가 N//2명일때
            s_stat = l_stat = 0  # 스타트, 링크 팀의 능력치 초기화
            # 능력치 구하기
            for i in range(N//2):
                for j in range(N//2):
                    s_stat += synergy[start[i]][start[j]]
                    l_stat += synergy[link[i]][link[j]]
            # 팀 별 능력치 차이 최소값 구하기
            result = min(result, abs(s_stat-l_stat))
        return
    # 멤버 추가하기기    member(num+1, start+[num], link)
    member(num+1, start+[num], link)
    member(num+1, start, link+[num])


N = int(input())
synergy = [list(map(int, input().split())) for _ in range(N)]
# N은 짝수, 팀은 N//2
result = 21e8
member(0, [], [])
print(result)