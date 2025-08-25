import sys
input = sys.stdin.readline
n, m = map(int, input().split())
noListen = set()
noWatch = set()

for i in range(n):
  noListen.add(input().rstrip())

for i in range(m):
  noWatch.add(input().rstrip())

noListenWatch = sorted(list(noListen & noWatch))

print(len(noListenWatch))
for i in noListenWatch:
    print(i)