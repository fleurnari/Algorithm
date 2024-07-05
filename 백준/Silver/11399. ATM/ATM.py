n = int(input())

p = list(map(int, input().split()))

sumArr = [0] * n

sum = 0


for i in range(1, n):
  insertIdx = i
  insertValue = p[i]

  for j in range(i - 1, -1, -1):
    if p[j] < p[i]:
      insertIdx = j + 1
      break

    if j == 0:
      insertIdx = 0

  for j in range(i, insertIdx, -1):
    p[j] = p[j - 1]
  
  p[insertIdx] = insertValue

sumArr[0] = p[0]

for i in range(1, n):
  sumArr[i] = sumArr[i - 1] + p[i]

for i in range(0, n):
  sum += sumArr[i]

print(sum)