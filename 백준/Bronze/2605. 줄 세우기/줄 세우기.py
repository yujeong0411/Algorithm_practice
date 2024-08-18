student = int(input())
num = list(map(int, input().split()))
s_lst = [n for n in range(1, student+1)]
for i in range(student):
    s, n = s_lst[i], num[i]   # 학생번호, 뽑은 번호
    for j in range(i, i - n, -1):
        s_lst[j] = s_lst[j-1]
    s_lst[i-n] = s
print(*s_lst)