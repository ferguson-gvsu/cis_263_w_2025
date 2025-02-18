import random
import timeit

def quicksort_helper(L, left, right):
  if left >= right:
    return L
  pivot_val = L[right]
  pivot_idx = left
  for idx in range(left, right):
    if L[idx] < pivot_val:
      tmp = L[idx]
      L[idx] = L[pivot_idx]
      L[pivot_idx] = tmp
      pivot_idx += 1
  tmp = L[right]
  L[right] = L[pivot_idx]
  L[pivot_idx] = tmp

  quicksort_helper(L, left, pivot_idx - 1)
  quicksort_helper(L, pivot_idx + 1, right)
  return L

def quicksort(L):
  result = quicksort_helper(L, 0, len(L) - 1)

def time_quicksort(count):
  L = list(range(count))
  random.shuffle(L)
  return quicksort(L)

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_quicksort({size})',setup='from __main__ import time_quicksort', number=100)
    print(f'{size},{time}')
