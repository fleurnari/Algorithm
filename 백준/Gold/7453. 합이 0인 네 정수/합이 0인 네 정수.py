import sys
input = sys.stdin.readline
n = int(input())
A, B, C, D = [], [], [], []
AB, CD = [], []
start = 0
end = n ** 2 - 1
cnt = 0

for _ in range(n):
  a, b, c, d = map(int, input().split())
  A.append(a)
  B.append(b)
  C.append(c)
  D.append(d)

for i in range(n):
  for j in range(n):
    AB.append(A[i] + B[j])
    CD.append(C[i] + D[j])

AB.sort()
CD.sort()

while start < len(AB) and end >= 0:
  if AB[start] + CD[end] == 0:
    cntStart = start + 1
    cntEnd = end - 1
    while cntStart < len(AB) and AB[start] == AB[cntStart]:
      cntStart += 1
    while cntEnd >= 0 and CD[end] == CD[cntEnd]:
      cntEnd -= 1
    cnt += (cntStart - start) * (end - cntEnd)
    start, end = cntStart, cntEnd
  elif AB[start] + CD[end] > 0:
    end -= 1
  else:
    start += 1

print(cnt)