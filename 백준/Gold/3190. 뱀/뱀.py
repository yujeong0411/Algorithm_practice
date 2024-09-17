from collections import deque

def snake(i, j):
    global result
    queue = deque()
    queue.append((i, j))
    idx = 0
    while queue:
        ni, nj = i + di[idx], j + dj[idx]
        if 0 <= ni < N and 0 <= nj < N and (ni, nj) not in queue:
            result += 1
            queue.append((ni, nj))
            i, j = ni, nj
            # print(queue, "q")
            if arr[ni][nj] == 4:
                arr[ni][nj] = 0
            else:
                y, x = queue.popleft()

            if result in time.keys():
                i, j = ni, nj
                if time[result] == 'D':
                    idx = (idx+1) % 4
                else:
                    idx = (idx+3) % 4
                # print(idx, "idx")

        else:
            result +=1
            break

N = int(input())
K = int(input())

arr = [[0]*N for _ in range(N)]
for _ in range(K):
    i, j = map(int, input().split())
    arr[i-1][j-1] = 4  # 사과 표시
# print(arr)
L = int(input())
time = {}
for _ in range(L):
    x, c = input().split()
    time[int(x)] = c
# print(time)
di, dj = [0, 1, 0, -1], [1, 0, -1, 0]  # 우, 하 좌, 상
result = 0
snake(0, 0)
print(result)