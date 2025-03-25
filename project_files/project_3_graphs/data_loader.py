class GenotypeData:
  def __init__(self, filename):
    self.data = {}
    self.filename = filename
    self.load_file(self.filename)

  def load_file(self, filename):
    self.data = {}
    self.N = 0
    int_data = {}
    with open(filename, 'r') as fp:
      for line in fp:
        line = line.strip()
        if line == '':
          continue
        if 'genotype' in line: 
          continue
        line_parts = line.split(',')
        if len(line_parts) != 2:
          print('Error loading line: ', line)
          exit(1)
        genotype_str = line_parts[0]
        fitness = float(line_parts[1])
        # It's actually more efficient to just store the ints, but this is more intuitive
        self.data[genotype_str] = fitness

  # Return a list of all one-step mutational neighbors (all strings)
  def get_neighbors(self, genotype):
    res = []
    for bit_idx in range(len(genotype)):
      if genotype[bit_idx] == '0':
        res.append(genotype[:bit_idx] + '1' + genotype[bit_idx+1:])
      else:  
        res.append(genotype[:bit_idx] + '0' + genotype[bit_idx+1:])
    return res

  # Lookup fitness of the given genotype
  def get_fitness(self, genotype):
    return self.data[genotype]

  # Return a list of all genotypes (as strings) that we know about
  def get_all_genotypes(self):
    return list(self.data.keys())
