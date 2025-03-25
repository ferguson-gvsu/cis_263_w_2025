from graph import Graph
from data_loader import GenotypeData

class LandscapeAnalyzer:
    def __init__(self, filename):
        self.data = GenotypeData(filename)

    # Given a genotype, find all genotypes that can be reached via 
    #   beneficial/neutral mutations
    def find_adaptive_genotypes(self, genotype):
        return []
