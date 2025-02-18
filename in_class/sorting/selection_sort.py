import random
import timeit

def selection_sort(L):
  for idx in range(len(L) - 1):
    swap_idx = idx
    swap_val = L[idx]
    for second_idx in range(swap_idx, len(L)):
      if L[second_idx] < swap_val:
        swap_idx = second_idx
        swap_val = L[second_idx]
    L[swap_idx] = L[idx]
    L[idx] = swap_val
  return L


def time_selection_sort(count):
  L = list(range(count))
  random.shuffle(L)
  return selection_sort(L)

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_selection_sort({size})',setup='from __main__ import time_selection_sort', number=100)
    print(f'{size},{time}')

