import sys
input = sys.stdin.readline
r, c = map(int, input().split())
board = [input().rstrip() for _ in range(r)]
dist = [c - row.find(str(i)) for i in range(1, 10) for row in board if str(i) in row]
rank = sorted(set(dist))

for i in dist:
    print(rank.index(i) + 1)