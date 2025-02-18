import random
import timeit

def insertion_sort(L):
  for idx in range(1, len(L)):
    val_to_insert = L[idx]
    new_idx = idx
    for i in range(1, idx + 1):
      if val_to_insert < L[idx - i] and (idx - i == 0 or L[idx - i - 1] < val_to_insert):
        new_idx = idx - i 
        break
    L.pop(idx)
    L.insert(new_idx, val_to_insert)
  return L


def time_insertion_sort(count):
  L = list(range(count))
  random.shuffle(L)
  return insertion_sort(L)

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_insertion_sort({size})',setup='from __main__ import time_insertion_sort', number=100)
    print(f'{size},{time}')

