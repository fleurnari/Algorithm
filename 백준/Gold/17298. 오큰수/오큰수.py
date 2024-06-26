import sys

n = int(input())

a = list(map(int, input().split()))

answerList = [0] * n

st = []


for i in range(n):
  while st and a[st[-1]] < a[i]:
    answerList[st.pop()] = a[i]
  st.append(i)

while st:
  answerList[st.pop()] = -1

for i in range(n):
  sys.stdout.write(str(answerList[i]) + " ")