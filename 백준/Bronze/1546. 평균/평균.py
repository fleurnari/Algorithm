n = input()

scoreList = list(map(int, input().split()))

maxScore = max(scoreList)

sum = sum(scoreList)

print(sum * 100 / maxScore / int(n))