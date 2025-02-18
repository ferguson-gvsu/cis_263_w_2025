import random
import timeit

def time_sort(count):
  L = list(range(count))
  random.shuffle(L)
  L.sort()
  return L

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_sort({size})',setup='from __main__ import time_sort', number=100)
    print(f'{size},{time}')
