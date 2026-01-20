import sys
import math
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]
height = math.ceil(math.log2(n)) + 1
nodeN = 1 << height
seg = [0 for _ in range(nodeN)]

def segment(idx, s, e):
  if s == e:
    seg[idx] = (arr[s], arr[s])
    return seg[idx]
  mid = (s + e) // 2
  l = segment(idx * 2, s, mid)
  r = segment(idx * 2 + 1, mid + 1, e)
  seg[idx] = (min(l[0], r[0]), max(l[1], r[1]))
  return seg[idx]

def find(s, e, idx):
  if e < a or b < s:
    return (1000000000, 0)
  mid = (s + e) // 2
  if a <= s and e <= b:
    return seg[idx]
  else:
    l = find(s, mid, idx * 2)
    r = find(mid + 1, e, idx * 2 + 1)
    return (min(l[0], r[0]), max(l[1], r[1]))

segment(1, 0, len(arr) - 1)

for _ in range(m):
  a, b = map(int, input().split())
  a -= 1
  b -= 1
  answer = find(0, len(arr) - 1, 1)
  print(answer[0], answer[1])