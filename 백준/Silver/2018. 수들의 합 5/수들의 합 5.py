n = int(input())

count = 1

startIdx = 1

endIdx = 1

sum = 1


while endIdx != n:
  if sum == n:
    count += 1
    endIdx += 1
    sum += endIdx
  elif sum > n:
    sum -= startIdx
    startIdx += 1
  else:
    endIdx += 1
    sum += endIdx

print(count)