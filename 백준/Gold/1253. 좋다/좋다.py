import sys

input = sys.stdin.readline

n = int(input())

a = list(map(int, input().split()))

a.sort()

count = 0


for k in range(n):
  
  num = a[k]
  
  i = 0
  
  j = n - 1
  
  while i < j:
    
    if a[i] + a[j] == num:
      
      if i != k and j != k:
        count += 1
        break
        
      elif i == k:
        i += 1
        
      elif j == k:
        j -= 1
        
    elif a[i] + a[j] < num:
      i += 1
      
    else:
      j -= 1

print(count)