from collections import deque
def bright(y, x):
    cnt = 0
    queue = deque()
    queue.append((y, x))
    visited[y][x] = 1
    while queue:
        (cy, cx) = queue.popleft()  # 현재 좌표 꺼내기
        if cy % 2 == 0:  # 짝수라면
            for k in even:  # 인접 건물 탐색
                ny, nx = cy+k[0], cx+k[1]
                # 범위 내에 있고, 건물과 인접했다면
                if 0 <= ny < H+2 and 0 <= nx < W+2:
                    if data[ny][nx] == 1:
                        cnt += 1  # 벽 카운트
                    elif data[ny][nx] == 0 and not visited[ny][nx]:  # 건물이 아니고 방문한 적 없을 때
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
        else:  # 홀수라면
            for k in odd:  # 인접 건물 탐색
                ny, nx = cy+k[0], cx+k[1]
                # 범위 내에 있고, 건물과 인접했다면
                if 0 <= ny < H+2 and 0 <= nx < W+2:
                    if data[ny][nx] == 1:
                        cnt += 1  # 벽 카운트
                    elif data[ny][nx] == 0 and not visited[ny][nx]:  # 건물이 아니고 방문한 적 없을 때
                        visited[ny][nx] = 1
                        queue.append((ny, nx))
    return cnt

# def bright2(y, x):
#     cnt = 0
#     queue = deque()
#     queue.append((y, x))
#     visited[y][x] = 1
#     directions = [even, odd]
#     while queue:
#         (cy, cx) = queue.popleft()  # 현재 좌표 꺼내기
#         dir = directions[cy % 2]  # 짝수, 홀수 결정
#         for dy, dx in dir:
#             ny, nx = cy+dy, cx+dx
#             # 범위 내에 있고, 건물과 인접했다면
#             if 0 <= ny < H+2 and 0 <= nx < W+2:
#                 if data[ny][nx] == 1:
#                     cnt += 1  # 벽 카운트
#                 elif data[ny][nx] == 0 and not visited[ny][nx]:  # 건물이 아니고 방문한 적 없을 때
#                     visited[ny][nx] = 1
#                     queue.append((ny, nx))
#     return cnt

W, H = map(int, input().split())  # 너비, 높이
arr = [list(map(int, input().split())) for _ in range(H)]
# 상하좌우 padding 처리
data = [[0]*(W+2) for _ in range(H+2)]
for i in range(H):
    for j in range(W):
        data[i+1][j+1] = arr[i][j]
even = [(-1,-1), (-1,0),(1,-1),(0,1),(1,0),(0,-1)]
odd = [(0,-1), (-1,0),(0,1),(1,1),(1,0),(-1,1)]
visited = [[0] * (W + 2) for _ in range(H + 2)]
print(bright(0,0))
# print(bright2(1, 1))