"""Unit tests on synthetic short DNA sequences."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from bioalgorithms import (
    hamming_distance, edit_distance, global_alignment_score,
    kmer_index, find_exact_matches, debruijn_graph, assemble_unambiguous_path
)


class AlignmentTests(unittest.TestCase):
    def test_hamming(self):
        self.assertEqual(hamming_distance("GATTACA", "GACTATA"), 2)
        self.assertEqual(hamming_distance("", ""), 0)
        with self.assertRaises(ValueError):
            hamming_distance("AC", "A")

    def test_edit(self):
        self.assertEqual(edit_distance("kitten", "sitting"), 3)
        self.assertEqual(edit_distance("", "AC"), 2)
        self.assertEqual(edit_distance("AC", "AC"), 0)

    def test_global_score(self):
        self.assertEqual(global_alignment_score("AC", "AC"), 4)
        self.assertEqual(global_alignment_score("", "AC"), -4)
        self.assertEqual(global_alignment_score("A", "G"), -1)


class IndexTests(unittest.TestCase):
    def test_repeated_kmers(self):
        self.assertEqual(kmer_index("ATATA", 2)["AT"], [0, 2])
        self.assertEqual(find_exact_matches("ATATA", "ATA"), [0, 2])
        self.assertEqual(find_exact_matches("AAAA", "TT"), [])

    def test_edge_cases(self):
        self.assertEqual(find_exact_matches("AC", ""), [])
        with self.assertRaises(ValueError):
            kmer_index("AC", 0)


class AssemblyTests(unittest.TestCase):
    def test_path(self):
        graph = debruijn_graph(["ATGCA"], 3)
        self.assertEqual(assemble_unambiguous_path(graph), "ATGCA")

    def test_branch(self):
        graph = debruijn_graph(["ATGA", "ATGC"], 3)
        with self.assertRaises(ValueError):
            assemble_unambiguous_path(graph)

    def test_empty(self):
        self.assertEqual(assemble_unambiguous_path({}), "")


if __name__ == "__main__":
    unittest.main()
