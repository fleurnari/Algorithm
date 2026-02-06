import sys
input = sys.stdin.readline
n = int(input())

if n == 1:
  print("*")
  exit()

if n == 2:
  print("** **")
  print(" ***")
  print("** **")
  exit()

print("*" * n + " " * (2 * n - 3) + "*" * n)

for i in range(1, n - 1):
  print(
    " " * i +
    "*" +
    " " * (n - 2) +
    "*" +
    " " * (2 * (n - i) - 3) +
    "*" +
    " " * (n - 2) +
    "*"
  )

print(" " * (n - 1) + "*" + " " * (n - 2) + "*" + " " * (n - 2) + "*")

for i in range(n - 2, 0, -1):
  print(
    " " * i +
    "*" +
    " " * (n - 2) +
    "*" +
    " " * (2 * (n - i) - 3) +
    "*" +
    " " * (n - 2) +
    "*"
  )

print("*" * n + " " * (2 * n - 3) + "*" * n)