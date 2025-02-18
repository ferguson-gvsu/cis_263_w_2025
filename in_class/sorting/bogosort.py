import random
import timeit

def bogosort(L):
  while True:
    is_sorted = True
    max_val = None
    random.shuffle(L)
    for x in L:
      if max_val is None or x > max_val:
        max_val = x
      else:
        is_sorted = False
        break
    if is_sorted:
      break
  return L


def time_bogosort(count):
  L = list(range(count))
  random.shuffle(L)
  return bogosort(L)

if __name__ == '__main__':
  print('num_items,time')
  for i in range(3, 9):
    time = timeit.timeit(f'time_bogosort({i})',setup='from __main__ import time_bogosort', number=100)
    print(f'{i},{time}')

