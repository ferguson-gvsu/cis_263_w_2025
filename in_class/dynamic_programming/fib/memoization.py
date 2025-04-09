import sys

D = {}
def fib(n):
  if n < 2:
    return 1
  if n-1 not in D:
    D[n-1] = fib(n-1)
  if n-2 not in D:
    D[n-2] = fib(n-2)
  return D[n-1] + D[n-2]


if len(sys.argv) != 2:
  print('Expected one command line argument!')
  exit(1)
# Grab first command line arg
n = int(sys.argv[1])
print(n, fib(n))
