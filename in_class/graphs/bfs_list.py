from collections import deque

class Graph:
  def __init__(self):
    self.nodes = set()
    self.adj_list = {}

  def add_node(self, node):
    self.nodes.add(node)
    self.adj_list[node] = set()

  def add_edge(self, a, b, undirected=False):
    self.adj_list[a].add(b)
    if undirected:
      self.adj_list[b].add(a)

  def bfs(self, start):
    Q = deque()
    Q.append(start)
    discovered = {start}
    while len(Q) > 0:
      node = Q.popleft()
      print(node)
      for neighbor in self.adj_list[node]:
        if neighbor not in discovered:
          Q.append(neighbor)
          discovered.add(neighbor)
  
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
