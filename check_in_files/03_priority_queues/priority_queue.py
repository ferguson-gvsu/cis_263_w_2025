# A class implementing a priority queue
#   Remember that priority queues are an abstract data type
class MaxPriorityQueue:
  # Do whatever setup you need here (this is not directly autograded)
  def __init__(self):
    pass
 
  # Insert the given key into the priority queue
  #   This isn't directly autograded, but will vary depending on your implementation
  #   Does not need to return anything
  #   You may assume key is always an integer 
  def insert(self, key):
    pass

  # Return the value of the largest item in the PQ
    # However, do NOT remove this item. Peek should not modify your PQ at all, it is readonly
    # If your PQ is empty, return None
  def peek_max(self):
    return None

  # Return the value of the largest item in the PQ AND remove it
    # If your PQ is empty, return None
  def pop_max(self):
    return None

  # Should return the number of items in the PQ as an integer
  def __len__(self):
    return 0

  # This is not required. 
  # Returns a pretty string of your PQ. 
  #   If you implement this, it may help with debugging. 
  #   This will get called by the print(pq) lines below
  def __str__(self):
    return '{{ Implement the __str__ method if you want easier debugging }}'

if __name__ == '__main__':
  pq = MaxPriorityQueue()
  # Give the user the instructions
  print('Command options:')
  print('  "peek" to peek the maximum value in the priority queue')
  print('  "pop" to remote the maximum value and return it')
  print('  "len" to get the number of items in the priority queue')
  print('  "quit" to exit')
  print('  Any integer to add that integer into the priority queue')
  print('')
  print('Initial state:', pq)
  # Continue to take commands one at a time
  while True:
    print('Command: ', end = '')
    s = input().strip()
    if s == 'pop':
      print('Popped:', pq.pop_max())
    elif s == 'peek':
      print('Peeked:', pq.peek_max())
    elif s == 'len':
      print('Current length:', len(pq))
    elif s == 'quit':
      break
    else:
      pq.insert(int(s))
    print('Current state:', pq)
