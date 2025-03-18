from collections import deque

class Graph:
  def __init__(self):
    self.matrix = []
    self.nodes = {}

  def add_node(self, n):
    index = len(self.matrix)
    self.nodes[n] = index
    self.matrix.append([0] * (index))
    for key, val in self.nodes.items():
      #val = self.nodes[key]
      self.matrix[val].append(0)
    print(self.matrix)

  def add_edge(self, a, b):
    idx_a = self.nodes[a]
    idx_b = self.nodes[b]
    self.matrix[idx_a][idx_b] = 1
    self.matrix[idx_b][idx_a] = 1
    print(self.matrix)

  def bfs(self, start):
    Q = deque()
    Q.append(start)
    discovered = set()
    discovered.add(start)
    while len(Q) > 0:
      node = Q.popleft()
      print(node)
      node_idx = self.nodes[node]
      for neighbor in self.nodes:
        neighbor_idx = self.nodes[neighbor]
        if self.matrix[node_idx][neighbor_idx] == 1:
          if neighbor not in discovered:
            Q.append(neighbor)
            discovered.add(neighbor)



if __name__ == '__main__':
  G = Graph()
  G.add_node('a')
  G.add_node('b')
  G.add_node('c')
  G.add_node('d')
  G.add_edge('a', 'b')
  G.add_edge('b', 'c')
  G.add_edge('c', 'd')
  G.add_edge('a', 'd')
  G.bfs('a')
