def helper(options, included, target, indent=0):
  # Have we found a solution?
  if sum(included) == target:
    print('Found solution:', included)
    return 1
  # Stop if we run out of options
  if len(options) == 0: 
    return 0
  # Which value do we need to decide on next? 
  next_val = options.pop()
  # Path where we don't take the val
  res = helper(options, included, target, indent + 1)
  included.add(next_val)
  # Path where we do
  res += helper(options, included, target, indent + 1)
  # Reset the state of our variables to be the same as when we got them!
  included.remove(next_val)
  options.append(next_val)
  return res


options = [5, 10, 12, 13, 15, 18]
target = 30
num_solutions = helper(options, set(), target)
print('Total number of solutions:', num_solutions)
