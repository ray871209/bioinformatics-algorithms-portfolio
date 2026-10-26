# Bioinformatics Algorithms — Portfolio Edition

A curated, **independently rewritten** Python collection inspired by algorithms studied in bioinformatics coursework. It provides runnable examples and a mapped record of the topics studied. This is a standalone public repository of independently rewritten, educational implementations. Historical coursework is maintained separately in a private archive.

## What this demonstrates

| Area | Implementation | Coursework connection |
|---|---|---|
| Sequence alignment | Hamming distance, Levenshtein edit distance and global alignment scoring | Week 03: Alignment |
| Sequence indexing | K-mer positions and exact-match seed hits | Week 02: Indexing; Assignment 1 |
| Genome assembly | De Bruijn adjacency, unambiguous path reconstruction | Week 07: De Bruijn Graphs; Assignment 3 |
| Sequence similarity | Jaccard similarity, canonical k-mers, deterministic bottom-k hashing | Week 04: MinHash |
| Biological networks | Degree distribution, clustering coefficient, BFS | Week 05: Networks |
| Phylogenetics | Sankoff dynamic programming on rooted binary trees | Week 06: Trees and parsimony |
| Clustering | Educational DBSCAN implementation | Week 09: Clustering |
| Optimisation | Seeded simulated annealing for generic objectives | Week 10: Optimisation |
| Supervised learning | K-nearest neighbours, accuracy and confusion counts | Week 11: Classification |

The functions below are newly written, self-contained examples, **not copies of assessed submissions**. The historical notebooks and `week*_sol.py` remain untouched elsewhere in the private archive. See [provenance](docs/provenance.md) for links to original material.

## Run

Requires Python 3.10+; core examples use only Python's standard library.

```bash
cd portfolio
python -m unittest discover -s tests -v
python examples/demo.py
```

These commands are documented usage instructions; check [verification status](docs/verification.md) for what has actually been run.

## What is *not* claimed

This repository does not demonstrate a production aligner, a reference-grade genome assembler, or a validated clinical bioinformatics pipeline. K-mer indexing is exact matching only; graph reconstruction is intentionally restricted to non-branching paths. Data in the examples are short, synthetic DNA sequences.

## Publication and provenance

This repository contains only curated, newly rewritten example implementations and synthetic demonstration inputs. It does not include graded submissions, instructor-supplied coursework, original datasets, or the Git history of the private source archive. See [provenance](docs/provenance.md) and [verification status](docs/verification.md).
