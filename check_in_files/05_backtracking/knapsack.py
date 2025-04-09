# Helper class to name our items' attributes
class KnapsackItem:
  def __init__(self, weight, val):
    self.weight = weight
    self.value = val

  # Generate an easy-to-read string
  def __str__(self):
    return f'({self.weight},{self.value})'

# Class to solve the knapsack problem with useful helper functions
class KnapsackSolver:
  def __init__(self):
    self.items = []
    self.included_items = set()

  def add_item(self, weight, val):
    self.items.append(KnapsackItem(weight, val))
  
  # Calculate sum of values for all included items
  def get_included_value(self):
    res = 0
    for item in self.included_items:
      res += item.value
    return res
  
  # Calculate sum of weights for all included items
  def get_included_weight(self):
    res = 0
    for item in self.included_items:
      res += item.weight
    return res

  # Print all included items in a pretty way
  def print_included(self):
    for item in self.included_items:
      print(item, end = ' ')
    print('')


  # THIS IS THE ONE YOU SHOULD BE EDITING
  # Recursive helper function
  def solve_helper(self, weight_limit):
    self.recursion_counter += 1 # DO NOT CHANGE THIS LINE!
  
    # Base case: no items left! Do subsets match?
    if len(self.items) == 0:
      total_weight = self.get_included_weight()
      if total_weight <= weight_limit:
        return self.get_included_value()
      return -1 # No match

    # Typical case: Try two options
    next_item = self.items.pop()
    # 1. Exclude next item 
    res_1 = self.solve_helper(weight_limit)
    # 2. Include next item
    self.included_items.add(next_item) 
    res_2 = self.solve_helper(weight_limit) 
    # Reset the variables to how we found them
    self.included_items.remove(next_item)
    self.items.append(next_item)
    return max(res_1, res_2)
  
  # Solve the knapsack problem via brute force
  # You should not need to edit this one, but you are welcome to if you'd like.
  def solve(self, weight_limit):
    self.recursion_counter = 0 # DO NOT CHANGE THIS LINE!
    return self.solve_helper(weight_limit)


if __name__ == '__main__':

  # Concise way to store test cases
  # Index 0 of each list is the max weight
  # The other elements are tuples, each representing an item as (weight, val)
  all_lists = []
  all_lists.append([1, (1,1), (2,2), (3,3), (4,4)])
  all_lists.append([2, (1,1), (2,2), (3,3), (4,4)])
  all_lists.append([3, (1,1), (2,2), (3,3), (4,4)])
  all_lists.append([1, (1,4), (2,3), (3,2), (4,1)])
  all_lists.append([2, (1,4), (2,3), (3,2), (4,1)])
  all_lists.append([3, (1,4), (2,3), (3,2), (4,1)])
  all_lists.append([2, (1.2, 3), (1.3333, 6), (1.75, 2), (1.75, 2), (3.75, 12), (0.75, 1)])
  all_lists.append([4, (1.2, 3), (1.3333, 6), (1.75, 2), (1.75, 2), (3.75, 12), (0.75, 1)])
  all_lists.append([6, (1.2, 3), (1.3333, 6), (1.75, 2), (1.75, 2), (3.75, 12), (0.75, 1)])
  all_lists.append([8, (1.2, 3), (1.3333, 6), (1.75, 2), (1.75, 2), (3.75, 12), (0.75, 1)])
  all_lists.append([1, (10, 3), (9, 3), (8, 3), (7, 3), (6, 3), (1, 1)])
  for L in all_lists:
    weight_limit = L[0]
    items = L[1:]
    print(f'weight limit: {weight_limit}')
    print(f'items: {items}')
    solver = KnapsackSolver()
    for item in items:
      solver.add_item(item[0], item[1])
    print(f'  result: {solver.solve(weight_limit)}')
    print(f'  recursive calls: {solver.recursion_counter}')
