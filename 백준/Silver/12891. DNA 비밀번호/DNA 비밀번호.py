nowStatus = [0] * 4
chkPwd = [0] * 4
chkCnt = 0

def chkAdd(c):
  global nowStatus, chkPwd, chkCnt
  if c == 'A':
    nowStatus[0] += 1
    if nowStatus[0] == chkPwd[0]:
      chkCnt += 1
  elif c == 'C':
    nowStatus[1] += 1
    if nowStatus[1] == chkPwd[1]:
      chkCnt += 1
  elif c == 'G':
    nowStatus[2] += 1
    if nowStatus[2] == chkPwd[2]:
      chkCnt += 1
  elif c == 'T':
    nowStatus[3] += 1
    if nowStatus[3] == chkPwd[3]:
      chkCnt += 1


def chkRemove(c):
  global nowStatus, chkPwd, chkCnt
  if c == 'A':
    if nowStatus[0] == chkPwd[0]:
      chkCnt -= 1
    nowStatus[0] -= 1
  elif c == 'C':
    if nowStatus[1] == chkPwd[1]:
      chkCnt -= 1
    nowStatus[1] -= 1
  elif c == 'G':
    if nowStatus[2] == chkPwd[2]:
      chkCnt -= 1
    nowStatus[2] -= 1
  elif c == 'T':
    if nowStatus[3] == chkPwd[3]:
      chkCnt -= 1
    nowStatus[3] -= 1


s, p = map(int, input().split())
str = list(input())
chkPwd = list(map(int, input().split()))
count = 0

for i in range(4):
  if chkPwd[i] == 0:
    chkCnt += 1

for i in range(p):
  chkAdd(str[i])

if chkCnt == 4:
  count += 1

for i in range(p, s):
  j = i - p
  chkAdd(str[i])
  chkRemove(str[j])
  if chkCnt == 4:
    count += 1

print(count)