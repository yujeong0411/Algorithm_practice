import sys

N = int(input())
arr = []
result = 0
for i in range(N):
    lst = list(map(int, sys.stdin.readline().split()))
    
    if lst and lst != [0]:  
        lst[2] -= 1
        if lst[2] == 0:
            result += lst[1]
        else:
            arr.append(lst)
    elif arr:  # arr이 비어있지 않은 경우에만 pop 시도
        cool = arr.pop()
        cool[2] -= 1
        if cool[2] == 0:
            result += cool[1]
        else:
            arr.append(cool)

print(result)
