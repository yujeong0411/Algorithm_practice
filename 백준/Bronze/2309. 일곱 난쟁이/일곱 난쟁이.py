height = []
for _ in range(9):
    k = int(input())
    height.append(k)

for i in range(8):
    for j in range(i+1, 9):
        total = sum(height)
        if total - height[i] - height[j] == 100:
            height.pop(j)
            height.pop(i)
            height.sort()
            print(*height)
            break
    if len(height) == 7:
        break