import sys

input = sys.stdin.readline

n, k = map(int, input().split())

a = list(map(int, input().split()))

def sortDef(start, end, k):
  global a

  if start < end:
    pivot = partionIdx(start, end)

    if k == pivot:
      return
    elif k < pivot:
      sortDef(start, pivot - 1, k)
    else:
      sortDef(pivot + 1, end, k)


def swap(i, j):
  global a
  temp = a[i]
  a[i] = a[j]
  a[j] = temp


def partionIdx(start, end):
 global a

 if start + 1 == end:
    if a[start] > a[end]:
      swap(start, end)
    return end

 middle = (start + end) // 2
 swap(start, middle)
 pivot = a[start]
 i = start + 1
 j = end

 while i <= j:
   while a[i] < pivot and i < len(a) - 1:
     i += 1
   while a[j] > pivot and j > 0:
     j -= 1
   if i <= j:
     swap(i, j)
     i += 1
     j -= 1

 a[start] = a[j]
 a[j] = pivot
 return j

sortDef(0, n - 1, k - 1)

print(a[k - 1])