N = int(input())
a = [0] * (N+1)
for i in range(2, N+1):
    a[i] = a[i-1] + 1

    if i % 2 == 0:
        a[i] = min(a[i//2] + 1 , a[i])

    if i % 3 == 0:
        a[i] = min(a[i//3] + 1, a[i])
print(a[N])