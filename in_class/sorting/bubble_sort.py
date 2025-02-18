import random
import timeit

def bubble_sort(L):
  while True:
    is_sorted = True
    for idx in range(len(L) - 1):
      if L[idx] > L[idx + 1]:
        tmp = L[idx]
        L[idx] = L[idx + 1]
        L[idx + 1] = tmp
        is_sorted = False
    if is_sorted:
      break
  return L


def time_bubble_sort(count):
  L = list(range(count))
  random.shuffle(L)
  return bubble_sort(L)

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_bubble_sort({size})',setup='from __main__ import time_bubble_sort', number=100)
    print(f'{size},{time}')

