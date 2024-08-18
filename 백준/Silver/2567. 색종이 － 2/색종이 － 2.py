def count(arr):
    cnt = 0
    for lst in arr:
        for i in range(1, len(lst)):
            if lst[i-1]!=lst[i]:  # 현재값과 직전의 값이 다르면 경계선!
                cnt+=1
    return cnt

N = int(input())
arr = [[0]*102 for _ in range(102)]
for _ in range(N):
    # [1] 해당 영역을 1로 표시
    sj, si = map(int, input().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j]=1

arr_t = list(zip(*arr))  # 전치행렬: 수정필요시 list(map(list, zip(*arr)))
ans = count(arr) + count(arr_t)
print(ans)