# Bioinformatics Algorithms — Portfolio Edition

A curated, **independently rewritten** Python collection inspired by algorithms studied in bioinformatics coursework. This folder is intended to be extractable into a **new, clean public repository**, separate from the original private coursework archive.

## What this demonstrates

| Area | Implementation | Coursework connection |
|---|---|---|
| Sequence alignment | Hamming distance, Levenshtein edit distance and global alignment scoring | Week 03: Alignment |
| Sequence indexing | K-mer positions and exact-match seed hits | Week 02: Indexing; Assignment 1 |
| Genome assembly | De Bruijn adjacency, unambiguous path reconstruction | Week 07: De Bruijn Graphs; Assignment 3 |

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

## Public-release note

**Do not turn the parent private repository Public.** This directory can be copied into a **new clean repository** after final inspection; assessment PDFs, instructor text, identifiable outputs, serialized objects and unreviewed third-party datasets must not be carried across.
