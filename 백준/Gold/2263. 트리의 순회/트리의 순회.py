import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n = int(input())
inOrder = list(map(int, input().split()))
postOrder = list(map(int, input().split()))
inOrderIdx = {value : idx for idx, value in enumerate(inOrder)}

def preOrder(inLeft, inRight, postLeft, postRight):
  if inLeft > inRight:
    return
  root = postOrder[postRight]
  print(root, end = " ")
  rootIdx = inOrderIdx[root]
  offset = rootIdx - inLeft
  preOrder(inLeft, rootIdx - 1, postLeft, postLeft + offset - 1)
  preOrder(rootIdx + 1, inRight, postLeft + offset, postRight - 1)

preOrder(0, n - 1, 0, n - 1)