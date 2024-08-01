N = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

def new_sort(N, lst1, lst2):
# 오름차순으로 정렬하면서, 중간에 배열 A가 배열 B와 같은지 확인
    for i in range(N-1, 0, -1):

        # 리스트 비교
        if lst1 == lst2:
            return print(1)
    
    # 최대값을 찾아서 맨 뒤로 이동
        max_idx = 0
        for j in range(1, i + 1):
            if lst1[j] > lst1[max_idx]:
                max_idx = j
        lst1[i], lst1[max_idx] = lst1[max_idx], lst1[i]

        if lst1 == lst2:
            return print(1)
    return print(0)

new_sort(N, A, B)