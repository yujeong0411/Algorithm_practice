def DFS2(i, j, n):
    # 스택을 이용한 DFS 구현
    stack = [(i, j)]
    
    # 방문 시작 지점 표시
    visited[i][j] = 1
    
    # 방향벡터 설정: 상하좌우 이동
    directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    
    while stack:
        x, y = stack.pop()
        
        # 인접 지역 탐색
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            # 유효한 범위 내에 있고, 아직 방문하지 않았으며, 현재 물 높이보다 높은 경우
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny] and arr[nx][ny] > n:
                visited[nx][ny] = 1  # 방문 표시
                stack.append((nx, ny))  # 스택에 추가하여 나중에 방문

# 입력 받기
N = int(input())  # 행렬의 크기
arr = [list(map(int, input().split())) for _ in range(N)]  # 행렬 데이터 입력받기

# 최대 물 높이 찾기
max_v = max(map(max, arr))  # 지역의 최대 높이 찾기

result = 0  # 최대 안전 영역의 개수 초기화

# 가능한 모든 물 높이에 대해 탐색
for water_level in range(0, max_v + 1):
    visited = [[0] * N for _ in range(N)]  # 방문 배열 초기화 (모든 지점을 방문하지 않은 상태로 시작)
    safe_area = 0  # 현재 물 높이에서의 안전 영역 개수 초기화
    
    for i in range(N):
        for j in range(N):
            # 물에 잠기지 않고, 방문하지 않은 경우
            if arr[i][j] > water_level and not visited[i][j]:
                DFS2(i, j, water_level)  # 스택 기반 DFS를 이용해 인접한 안전 영역 탐색
                safe_area += 1  # 새로운 안전 영역이 발견되었으므로 개수 증가
    
    # 현재 물 높이에서의 최대 안전 영역 개수를 갱신
    result = max(result, safe_area)

# 최종 결과 출력
print(result)
