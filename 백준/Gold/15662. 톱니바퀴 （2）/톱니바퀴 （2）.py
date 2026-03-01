import sys
input = sys.stdin.readline
t = int(input())
cogWheel = [input().rstrip() for _ in range(t)]
k = int(input())

for _ in range(k):
   num, dir = map(int, input().split())
   num -= 1
   d = [0] * t
   d[num] = dir
   for i in range(num - 1, -1, -1):
      if cogWheel[i][2] != cogWheel[i + 1][6]:
         d[i] = -d[i + 1]
      else:
         break
   for i in range(num + 1, t):
      if cogWheel[i - 1][2] != cogWheel[i][6]:
         d[i] = -d[i - 1]
      else:
         break
   for i in range(t):
     if d[i] == 1:
       cogWheel[i] = cogWheel[i][-1] + cogWheel[i][:-1]
     elif d[i] == -1:
       cogWheel[i] = cogWheel[i][1:] + cogWheel[i][0]

answer = 0
for i in range(t):
  if cogWheel[i][0] == '1':
    answer += 1

print(answer)