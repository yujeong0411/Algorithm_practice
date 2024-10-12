from itertools import permutations

def baseball(lineup):
    score = 0
    player = 0  # 첫번째 player
    for i in range(N):  # 이닝
        out = first = second = third = 0  # 아웃카운트, 1, 2, 3루의 선수 여부
        while out < 3:  # 3아웃 전까지 play
            # i번째 이닝의 player 결과
            if inning[i][lineup[player]] == 0: # 아웃이라면
                out += 1  # 아웃 카운트 증가
            elif inning[i][lineup[player]] == 1: # 안타
                score += third  # 3루 선수가 홈으로 들어옴
                third = second  # 2루 선수가 진루
                second = first  # 1루 선수가 진루
                first = 1  # 타자가 출루 
            elif inning[i][lineup[player]] == 2: # 2루타
                score += third + second
                third = first
                second = 1
                first = 0
            elif inning[i][lineup[player]] == 3: # 3루타
                score += third + second + first
                third = 1
                second = 0
                first = 0
            else:
                score += third + second + first + 1
                third = second = first = 0
            # 다음 타순
            player = (player + 1) % 9
    return score

N = int(input())  # 이닝 수
inning = []  # 전체 이닝 정보
for _ in range(N):
    inning.append(list(map(int, input().split())))

# 타순 순열 구하기 (0번 고정, 1~8번까지 구하기)
result = 0
for players in permutations(range(1, 9), 8):
    lineup = list(players[:3]) + [0] + list(players[3:])
    score = baseball(lineup)
    result = max(result, score)
print(result)