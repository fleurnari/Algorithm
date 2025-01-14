import sys
input = sys.stdin.readline
n = int(input())
treeDic = {}

for i in range(n):
  root, left, right = input().split()
  treeDic[root] = [left, right]

def preOrder(nowNode):
  if nowNode == '.':
    return
  print(nowNode, end='')
  preOrder(treeDic[nowNode][0])
  preOrder(treeDic[nowNode][1])

def inOrder(nowNode):
  if nowNode == '.':
    return
  inOrder(treeDic[nowNode][0])
  print(nowNode, end='')
  inOrder(treeDic[nowNode][1])

def postOrder(nowNode):
  if nowNode == '.':
    return
  postOrder(treeDic[nowNode][0])
  postOrder(treeDic[nowNode][1])
  print(nowNode, end='')

preOrder('A')
print()
inOrder('A')
print()
postOrder('A')
