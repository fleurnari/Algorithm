import sys
input = sys.stdin.readline
n = int(input())
score = [int(input()) for _ in range(n)]
answer = 0

for i in range(n - 1, 0, -1):
    if score[i - 1] >= score[i]:
        diff = score[i - 1] - (score[i] - 1)
        answer += diff
        score[i - 1] = score[i] - 1

print(answer)