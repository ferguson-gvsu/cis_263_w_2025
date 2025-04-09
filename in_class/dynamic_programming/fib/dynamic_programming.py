import sys

def fib(n):
  table = [0] * (n + 1)
  if n < 2:
    return 1
  table[0] = 1
  table[1] = 1
  for i in range(2, n + 1):
    table[i] = table[i-1] + table[i-2]
  return table[n]

if len(sys.argv) != 2:
  print('Expected one command line argument!')
  exit(1)
# Grab first command line arg
n = int(sys.argv[1])
print(n, fib(n))
