import random
import timeit
import heapq

def heapsort(L):
  result = [0] * len(L)
  heapq.heapify(L)
  for i in range(len(L)):
    result[i] = heapq.heappop(L)
  return result


def time_heapsort(count):
  L = list(range(count))
  random.shuffle(L)
  return heapsort(L)

if __name__ == '__main__':
  print('num_items,time')
  sizes = list(range(3,11)) \
      + list(range(10, 110, 10)) \
      + list(range(150, 1050, 50)) \
      + list(range(1250, 2250, 250))
  for size in sizes:
    time = timeit.timeit(f'time_heapsort({size})',setup='from __main__ import time_heapsort', number=100)
    print(f'{size},{time}')
