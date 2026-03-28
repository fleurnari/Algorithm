import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]
cycle = 0
components = 0

def union(a, b):
    a = find(a)
    b = find(b)

    if a == b:
        return False
    parent[b] = a
    return True

def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]


for _ in range(m):
    u, v = map(int, input().split())
    if not union(u, v):
        cycle += 1

for i in range(1, n + 1):
    if find(i) == i:
        components += 1

print(cycle + (components - 1))