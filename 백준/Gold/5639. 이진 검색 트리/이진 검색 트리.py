import sys

sys.setrecursionlimit(10 ** 6)

preorder = []

while True:
    try:
        preorder.append(int(sys.stdin.readline()))

    except:
        break


def postorder(start, end):
    mid = 0

    if start > end:
        return

    for i in range(start + 1, end + 1):
        if preorder[start] < preorder[i]:
            mid = i
            break

    else:
        mid = end + 1

    postorder(start + 1, mid - 1)
    postorder(mid, end)
    print(preorder[start])


postorder(0, len(preorder) - 1)