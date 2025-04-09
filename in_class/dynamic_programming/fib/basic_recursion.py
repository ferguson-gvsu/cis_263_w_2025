import sys

def fib(n):
  if n < 2:
    return 1
  return fib(n-1) + fib(n-2)


if len(sys.argv) != 2:
  print('Expected one command line argument!')
  exit(1)
# Grab first command line arg
n = int(sys.argv[1])
print(n, fib(n))
