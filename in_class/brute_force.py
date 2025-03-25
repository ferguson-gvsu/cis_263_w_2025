import copy

def helper(options, included, target):
  # Have we found a solution?
  if sum(included) == target:
    print('Found solution:', included)
    return 1
  # Stop if we run out of options
  if len(options) == 0: 
    return 0
  # Create deep copies of both containers so we don't 
  #   change other instances
  new_options = copy.deepcopy(options)
  next_included = copy.deepcopy(included)
  # Which value do we need to decide on next? 
  next_val = new_options.pop()
  # Path where we don't take the val
  res = helper(new_options, included, target)
  next_included.add(next_val)
  # Path where we do
  res += helper(new_options, next_included, target)
  return res


options = [5, 10, 12, 13, 15, 18]
target = 30
num_solutions = helper(options, set(), target)
print('Total number of solutions:', num_solutions)
