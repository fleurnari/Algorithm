import sys
from queue import PriorityQueue
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v, e = map(int, input().split())
pq = PriorityQueue()
parent = [0] * (v + 1)
useEdge = 0
result = 0
lastEdge = 0

for i in range(v + 1):
  parent[i] = i

for _ in range(e):
  a, b, c = map(int, input().split())
  pq.put((c, a, b))

def find(a):
  if a == parent[a]:
    return a
  else:
    parent[a] = find(parent[a])
    return parent[a]

def union(a, b):
  a = find(a)
  b = find(b)
  if a != b:
    parent[b] = a

while useEdge < v - 1:
  c, a, b = pq.get()
  if find(a) != find(b):
    union(a, b)
    useEdge += 1
    result += c
    lastEdge = c

print(result - lastEdge)