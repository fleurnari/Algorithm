import sys
from bisect import bisect_right
input = sys.stdin.readline
n, m, k = map(int, input().split())
cardNum = list(map(int, input().split()))
submitCard = list(map(int, input().split()))
visitList = [False] * (len(cardNum))
cardNum.sort()

for card in submitCard:
  right = bisect_right(cardNum, card)
  while True:
    if not visitList[right]:
      visitList[right] = True
      print(cardNum[right])
      break
    else:
      right += 1