"""Sequence distance and dynamic-programming alignment scores.

Rewritten independently for public demonstration. Not an original assignment submission.
"""
def hamming_distance(a: str, b: str) -> int:
    """Number of substitutions between equal-length sequences; O(n)."""
    if len(a) != len(b):
        raise ValueError("Hamming distance requires equal-length sequences")
    return sum(x != y for x, y in zip(a, b))


def edit_distance(a: str, b: str) -> int:
    """Levenshtein distance with O(len(a)*len(b)) time and O(len(b)) memory."""
    previous = list(range(len(b) + 1))
    for i, character in enumerate(a, 1):
        current = [i]
        for j, other in enumerate(b, 1):
            current.append(min(
                previous[j] + 1,
                current[j - 1] + 1,
                previous[j - 1] + (character != other),
            ))
        previous = current
    return previous[-1]


def global_alignment_score(
    a: str, b: str, match: int = 2, mismatch: int = -1, gap: int = -2
) -> int:
    """Needleman-Wunsch-style score with a linear gap penalty, no traceback."""
    previous = [j * gap for j in range(len(b) + 1)]
    for i, character in enumerate(a, 1):
        current = [i * gap]
        for j, other in enumerate(b, 1):
            current.append(max(
                previous[j] + gap,
                current[-1] + gap,
                previous[j - 1] + (match if character == other else mismatch),
            ))
        previous = current
    return previous[-1]
