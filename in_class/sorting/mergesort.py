import random
import timeit

def mergesort(L):
  if len(L) > 1:
    midpoint = len(L) // 2
    left = mergesort(L[:midpoint])
    right = mergesort(L[midpoint:])
    result = [0] * len(L)
    idx_left = 0
    idx_right = 0
    for i in range(len(L)):
      if idx_right >= len(right) or (idx_left < len(left) and left[idx_left] < right[idx_right]):
        result[i] = left[idx_left]
        idx_left += 1
      else:
        result[i] = right[idx_right]
        idx_right += 1
    return result
  else:
    return L


def time_mergesort(count):
  L = list(range(count))
  random.shuffle(L)
  return mergesort(L)

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_mergesort({size})',setup='from __main__ import time_mergesort', number=100)
    print(f'{size},{time}')
