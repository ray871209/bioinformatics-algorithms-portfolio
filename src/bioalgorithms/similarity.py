"""K-mer Jaccard similarity and deterministic bottom-k sketches.

Inspired by Week 04 MinHash; newly written for the portfolio.
"""
from hashlib import blake2b

def kmers(sequence: str, k: int) -> set[str]:
    if k < 1:
        raise ValueError("k must be positive")
    return {sequence[i:i+k] for i in range(max(0, len(sequence)-k+1))}

def jaccard_similarity(a: set, b: set) -> float:
    """For two empty sets, define similarity as 1.0."""
    union = a | b
    return len(a & b) / len(union) if union else 1.0

def reverse_complement(dna: str) -> str:
    return dna.upper().translate(str.maketrans("ACGT", "TGCA"))[::-1]

def bottom_k_sketch(sequence: str, k: int, sketch_size: int) -> set[int]:
    """Deterministic bottom-k hash sketch using canonical DNA k-mers."""
    if sketch_size < 1:
        raise ValueError("sketch_size must be positive")
    hashed = set()
    for word in kmers(sequence.upper(), k):
        if any(base not in "ACGT" for base in word):
            continue
        canonical = min(word, reverse_complement(word))
        digest = blake2b(canonical.encode(), digest_size=8).digest()
        hashed.add(int.from_bytes(digest, "big"))
    return set(sorted(hashed)[:sketch_size])

def sketch_similarity(a: str, b: str, k: int = 5, sketch_size: int = 100) -> float:
    """Jaccard of bottom-k sketches (illustrative, not an unbiased estimator)."""
    return jaccard_similarity(bottom_k_sketch(a,k,sketch_size),
                              bottom_k_sketch(b,k,sketch_size))
