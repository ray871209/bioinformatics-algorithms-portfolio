"""Sankoff dynamic programming for a rooted binary phylogenetic tree.

Inspired by Week 06. Each internal node maps to a pair of child names.
"""
from math import inf

def sankoff_score(children: dict[str, tuple[str,str]],
                  observations: dict[str,str],
                  alphabet: str = "ACGT",
                  mismatch_cost: int = 1) -> tuple[int, dict[str,dict[str,int]]]:
    """Return minimum root cost and per-node state-cost tables.

    The function requires exactly one rooted binary tree and a leaf observation
    for each tip. Missing/cyclic subtrees raise ValueError.
    """
    if mismatch_cost < 0 or not alphabet or len(set(alphabet)) != len(alphabet):
        raise ValueError("Invalid alphabet or mismatch cost")
    if not children and len(observations) == 1:
        name, state = next(iter(observations.items()))
        if state not in alphabet:
            raise ValueError("Unknown tip character")
        return 0, {name: {c: 0 if c == state else inf for c in alphabet}}
    referenced = {node for pair in children.values() for node in pair}
    roots = set(children) - referenced
    if len(roots) != 1:
        raise ValueError("Expected one root")
    root = next(iter(roots))
    scores = {}
    visiting = set()
    def visit(node):
        if node in scores:
            return scores[node]
        if node in visiting:
            raise ValueError("Cycle in tree")
        visiting.add(node)
        if node in children:
            left,right = children[node]
            l, r = visit(left), visit(right)
            score = {a: min(l[b]+(mismatch_cost if a!=b else 0) for b in alphabet)
                       + min(r[b]+(mismatch_cost if a!=b else 0) for b in alphabet)
                     for a in alphabet}
        elif node in observations:
            observed = observations[node]
            if observed not in alphabet:
                raise ValueError("Unknown tip character")
            score = {a: 0 if a==observed else inf for a in alphabet}
        else:
            raise ValueError("Leaf without observation")
        visiting.remove(node)
        scores[node] = score
        return score
    result = visit(root)
    if set(scores) != set(children)|set(observations):
        raise ValueError("Disconnected or unused tree nodes")
    return int(min(result.values())), scores
