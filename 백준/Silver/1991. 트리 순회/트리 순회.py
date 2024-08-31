def preorder(v):
    global word1
    if v != '.':
        print(v, end='')
        preorder(tree[v][0])
        preorder(tree[v][1])

def inorder(v):
    if v != '.':
        inorder(tree[v][0])
        print(v, end='')
        inorder(tree[v][1])

def postorder(v):
    if v != '.':
        postorder(tree[v][0])
        postorder(tree[v][1])
        print(v, end='')

N = int(input())
tree = {}
for i in range(N):
    root, left, right = input().split()
    tree[root] = left, right


preorder('A')
print()
inorder('A')
print()
postorder('A')