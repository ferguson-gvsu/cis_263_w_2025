# Simple class to solve partition problem while counting the number of recursive calls
class PartitionSolver:
  def __init__(self):
    self.counter = 0 # DO NOT CHANGE THIS LINE

  # Recursive function to solve the partition function
  # L is the list of remaining numbers
  # set_1 and set_2 are the two subset we are building (they are lists, though)
  def find_partition(self, L, set_1, set_2):
    self.counter += 1 # DO NOT CHANGE THIS LINE

    # Base case: No items left
    if len(L) == 0:
      res = sum(set_1) == sum(set_2)
      ## Uncomment if you want to see what solutions we're finding
      #if res:
      #  print('Found:', set_1, set_2)
      return res
  
    # Typical case: Try two possibilities
    next_item = L.pop()
    # 1. Include next item in left partition
    set_1.append(next_item)
    res_1 = self.find_partition(L, set_1, set_2)
    set_1.pop()
    # 2. Include next item in right partition
    set_2.append(next_item)
    res_2 = self.find_partition(L, set_1, set_2)
    set_2.pop()
    # Reset
    L.append(next_item)
    # Return the or, because we are only looking for *if a solution exists*
    return res_1 or res_2

if __name__ == '__main__':
  all_lists = []
  all_lists.append([1,2,1])
  all_lists.append([1,2,1,1])
  all_lists.append([1,2,3,4])
  all_lists.append(list(range(10)))
  all_lists.append([5, 5, 5, 5, 5, 5, 50, 5, 5, 5, 5])
  all_lists.append([1,1,1,1,1,1000000])
  for L in all_lists:
    print('Evaluating:', L)
    counter = PartitionSolver()
    result = counter.find_partition(L, [], [])
    print('Found subset?:', result)
    print('Recursive calls:', counter.counter)
