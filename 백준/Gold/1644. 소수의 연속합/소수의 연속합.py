import sys
input = sys.stdin.readline
n = int(input())
a = [False, False] + [True] * (n - 1)
prime = []
answer = 0
start = 0
end = 0

for i in range(2, n + 1):
  if a[i]:
    prime.append(i)
    for j in range(2 * i, n + 1, i):
      a[j] = False

while end <= len(prime):
  tmp = sum(prime[start:end])
  if tmp == n:
    answer += 1
    end += 1
  elif tmp < n:
    end += 1
  else:
    start += 1

print(answer)