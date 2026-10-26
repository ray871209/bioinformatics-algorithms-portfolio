"""Run a short, dependency-free demonstration."""
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from bioalgorithms import edit_distance, find_exact_matches, debruijn_graph, assemble_unambiguous_path

print("Edit distance:", edit_distance("GATTACA", "GACTATA"))
print("Exact hits:", find_exact_matches("ATATATA", "ATA"))
print("Unambiguous contig:", assemble_unambiguous_path(debruijn_graph(["ATGCA"], 3)))
