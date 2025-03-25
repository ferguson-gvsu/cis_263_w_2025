from collections import deque

class Graph:
  def __init__(self):
    self.nodes = set()
    self.adj_list = {}

  # Add a node with the given name
  def add_node(self, node):
    self.nodes.add(node)
    self.adj_list[node] = set()

  # Add an edge between two nodes, can be directed or undirected
  def add_edge(self, a, b, undirected=False):
    self.adj_list[a].add(b)
    if undirected:
      self.adj_list[b].add(a)

  # Perform breath-first search and return a set of all nodes visited
  def bfs(self, start):
    Q = deque()
    Q.append(start)
    discovered = {start}
    while len(Q) > 0:
      node = Q.popleft()
      for neighbor in self.adj_list[node]:
        if neighbor not in discovered:
          Q.append(neighbor)
          discovered.add(neighbor)
    return discovered
  
  # Perform depth-first search and return a set of all nodes visited
  def dfs(self, start):
    Q = deque()
    Q.append(start)
    discovered = {start}
    while len(Q) > 0:
      node = Q.pop()
      for neighbor in self.adj_list[node]:
        if neighbor not in discovered:
          Q.append(neighbor)
          discovered.add(neighbor)
    return discovered
  
if __name__ == '__main__':
  g = Graph()
  g.add_node('a')
  g.add_node('b')
  g.add_node('c')
  g.add_node('d')
  g.add_node('e')
  g.add_node('f')
  g.add_node('g')
  g.add_node('h')
  g.add_edge('a', 'b', True)
  g.add_edge('c', 'b', True)
  g.add_edge('c', 'd', True)
  g.add_edge('c', 'e', True)
  g.add_edge('d', 'e', True)
  g.add_edge('d', 'f', True)
  g.add_edge('e', 'g', True)
  g.add_edge('e', 'h', True)
  g.add_edge('f', 'g', True)
  print('BFS')
  g.bfs('a')
  print('DFS')
  g.dfs('a')
