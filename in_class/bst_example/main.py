
# Class for an individual node in the tree. 
# Stores data and various recursive functions
class BST_Node:
  def __init__(self, key):
    self.key = key
    self.left_node = None
    self.right_node = None
  
  # Prints the subtree in a pretty, indented format
  def print_indent(self, tabs = 0, prefix = ''):
    print('  ' * tabs, end = '')
    print('[' + prefix + ']', end = '')
    print(str(self.key)) 
    if self.left_node is not None:
      self.left_node.print_indent(tabs + 1, prefix + 'L')
    if self.right_node is not None:
      self.right_node.print_indent(tabs + 1, prefix + 'R')

  def insert(self, key):
    if key < self.key:
      if self.left_node is None:
        self.left_node = BST_Node(key)
      else: 
        self.left_node.insert(key)
    else: 
      if self.right_node is None:
        self.right_node = BST_Node(key)
      else:
        self.right_node.insert(key)

  def traverse_in_order(self):
    if self.left_node is not None:
      self.left_node.traverse_in_order()
    # print this node's value
    print(self.key, end = ' ')
    if self.right_node is not None:
      self.right_node.traverse_in_order()
  
  def traverse_pre_order(self):
    # print this node's value
    print(self.key, end = ' ')
    if self.left_node is not None:
      self.left_node.traverse_pre_order()
    if self.right_node is not None:
      self.right_node.traverse_pre_order()
  
  def traverse_post_order(self):
    if self.left_node is not None:
      self.left_node.traverse_post_order()
    if self.right_node is not None:
      self.right_node.traverse_post_order()
    # print this node's value
    print(self.key, end = ' ')

# Class for an entire binary search tree
# Mainly operates via recursive functions on the root node
class BST:
  def __init__(self):
    self.root = None

  def insert(self, key):
    if self.root is None:
      self.root = BST_Node(key)
    else:
      self.root.insert(key)
  
  def print_indent(self):
    if self.root is None:
      print('Tree is empty!')
    else:
      self.root.print_indent()

  def traverse_in_order(self):
    print('In order traversal: ', end = '')
    if self.root is not None:
      self.root.traverse_in_order()
    print('') # Add a newline
  
  def traverse_pre_order(self):
    print('Pre order traversal: ', end = '')
    if self.root is not None:
      self.root.traverse_pre_order()
    print('') # Add a newline
  
  def traverse_post_order(self):
    print('Post order traversal: ', end = '')
    if self.root is not None:
      self.root.traverse_post_order()
    print('') # Add a newline

if __name__ == '__main__':
  bst = BST()
  while True:
    print('What key would you like to add (ctrl+C to quit):')
    key = input()
    bst.insert(int(key))
    bst.print_indent()
    bst.traverse_in_order()
    bst.traverse_pre_order()
    bst.traverse_post_order()
