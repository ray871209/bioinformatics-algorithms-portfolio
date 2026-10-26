"""Additional synthetic tests for coursework-inspired implementations."""
import sys
import unittest
from pathlib import Path
sys.path.insert(0,str(Path(__file__).resolve().parents[1]/"src"))
from bioalgorithms.similarity import kmers,jaccard_similarity,bottom_k_sketch
from bioalgorithms.phylogenetics import sankoff_score
from bioalgorithms.networks import clustering_coefficient,reachable_bfs,degree_distribution
from bioalgorithms.clustering import dbscan
from bioalgorithms.optimization import simulated_annealing
from bioalgorithms.classification import knn_predict,classification_accuracy,confusion_counts

class SimilarityTests(unittest.TestCase):
    def test_kmers(self):
        self.assertEqual(kmers("ATATA",2),{"AT","TA"})
        self.assertEqual(jaccard_similarity({"A","B"},{"B","C"}),1/3)
        self.assertEqual(jaccard_similarity(set(),set()),1)
    def test_sketch(self):
        self.assertEqual(bottom_k_sketch("ACGTAC",3,10),bottom_k_sketch("ACGTAC",3,10))
        with self.assertRaises(ValueError):
            kmers("AC",0)

class TreeTests(unittest.TestCase):
    def test_sankoff(self):
        cost,table=sankoff_score({"root":("a","b")},{"a":"A","b":"G"})
        self.assertEqual(cost,1)
        self.assertIn("root",table)
    def test_bad_leaf(self):
        with self.assertRaises(ValueError):
            sankoff_score({"root":("a","b")},{"a":"A","b":"N"})

class NetworkTests(unittest.TestCase):
    def test_graph(self):
        g={"a":{"b","c"},"b":{"a","c"},"c":{"a","b"},"d":set()}
        self.assertEqual(clustering_coefficient(g,"a"),1.0)
        self.assertTrue(reachable_bfs(g,"a","c"))
        self.assertFalse(reachable_bfs(g,"a","d"))
        self.assertEqual(degree_distribution(g),{0:1,2:3})

class ClusterTests(unittest.TestCase):
    def test_groups_and_noise(self):
        groups=dbscan([(0.,0.),(.1,0.),(10.,10.),(10.1,10.),(100.,100.)],eps=.2,min_samples=2)
        self.assertEqual(groups,[0,0,1,1,-1])
    def test_empty(self):
        self.assertEqual(dbscan([],1,2),[])

class OptimizationTests(unittest.TestCase):
    def test_annealing(self):
        best,score=simulated_annealing(5,lambda x: abs(x),lambda x,rng:x-1,steps=8)
        self.assertEqual((best,score),(0,0))
    def test_invalid_config(self):
        with self.assertRaises(ValueError):
            simulated_annealing(1,abs,lambda x,rng:x,initial_temperature=0)

class ClassificationTests(unittest.TestCase):
    def test_knn(self):
        self.assertEqual(knn_predict([(0.,0.),(1.,1.),(10.,10.)],["a","a","b"],(.3,.3),k=3),"a")
        self.assertEqual(classification_accuracy(["a","b"],["a","a"]),0.5)
        self.assertEqual(confusion_counts(["a","b"],["a","a"]),{("a","a"):1,("b","a"):1})

if __name__=="__main__":
    unittest.main()
