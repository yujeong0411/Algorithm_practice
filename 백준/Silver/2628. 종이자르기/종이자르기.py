length, height = map(int, input().split())  # 가로, 세로
N = int(input())  # 잘라야 하는 갯수
l_lst = [0, length]  # 가로 점선 리스트
h_lst = [0, height]  # 세로 점선 리스트
for _ in range(N):
    dr, num = map(int, input().split())   # 가로0, 세로1, 점선 번호
    if dr == 1:   
        l_lst.append(num)
    else:
        h_lst.append(num)

l_lst.sort()
h_lst.sort()

# 넓이 구하기, 가로*세로
result = 0
for i in range(1, len(l_lst)):
    for j in range(1, len(h_lst)):
        l = l_lst[i] - l_lst[i-1]
        h = h_lst[j] - h_lst[j-1]
        result = max(h*l, result)

print(result)