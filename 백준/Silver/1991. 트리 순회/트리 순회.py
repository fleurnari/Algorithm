import sys
input = sys.stdin.readline
n = int(input())
tree = {}

for _ in range(n):
  root, left, right = input().split()
  tree[root] = [left, right]

def preOrder(v):
  if v == '.':
    return
  print(v, end = '')
  preOrder(tree[v][0])
  preOrder(tree[v][1])

def inOrder(v):
  if v == '.':
    return
  inOrder(tree[v][0])
  print(v, end = '')
  inOrder(tree[v][1])

def postOrder(v):
  if v == '.':
    return
  postOrder(tree[v][0])
  postOrder(tree[v][1])
  print(v, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')