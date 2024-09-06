def egg(i, d):
    global cnt

    if i == N or data_V.count(0) == 1:
        cnt = max(sum(data_V), cnt)
        return

    if not data_V[i]:
        for j in range(N):
            if i != j and not data_V[j]:
                a = d[i][0]
                b = d[j][0]
                d[i][0] = d[i][0] - d[j][1]
                d[j][0] = d[j][0] - d[i][1]
                if d[i][0] < 1:
                    data_V[i] = 1
                if d[j][0] < 1:
                    data_V[j] = 1
                egg(i+1, d)
                d[i][0] = a
                d[j][0] = b
                data_V[i] = 0
                data_V[j] = 0
    else:
        egg(i+1, d)


N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]
data_V = [0]*N
cnt = 0
egg(0, data)
print(cnt)