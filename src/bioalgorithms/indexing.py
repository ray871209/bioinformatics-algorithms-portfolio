"""Small exact k-mer index for synthetic DNA demonstration."""
from collections import defaultdict


def kmer_index(sequence: str, k: int) -> dict[str, list[int]]:
    """Map each length-k substring to its 0-based positions, including repeats."""
    if k < 1:
        raise ValueError("k must be positive")
    positions: dict[str, list[int]] = defaultdict(list)
    for i in range(max(0, len(sequence) - k + 1)):
        positions[sequence[i:i + k]].append(i)
    return dict(positions)


def find_exact_matches(reference: str, query: str) -> list[int]:
    """Return all 0-based starts of an exact query in the reference.

    Returns no positions for an empty query by design.
    """
    if not query:
        return []
    index = kmer_index(reference, len(query))
    return index.get(query, [])
