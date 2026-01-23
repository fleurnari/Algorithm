import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
size = 1

while size < n:
  size <<= 1
seg = [(9999999999, -1)] * (2 * size)
size -= 1

def update(idx, value):
  idx += size
  seg[idx] = value
  idx //= 2
  while idx:
    seg[idx] = min(seg[idx * 2], seg[idx * 2 + 1])
    idx //= 2

for i in range(n):
  update(i + 1, (a[i], i + 1))

def search(l, r):
  l += size
  r += size
  answer = (9999999999, -1)
  while l <= r:
    if l % 2 == 1:
      answer = min(answer, seg[l])
      l += 1
    l //= 2

    if r % 2 == 0:
      answer = min(answer, seg[r])
      r -= 1
    r //= 2
  return answer[1]

for _ in range(m):
  c, i, j = map(int, input().split())
  if c == 1:
    update(i, (j, i))
  else:
    print(search(i, j))