"""Minimal de Bruijn graph construction and a deliberately constrained walk."""
from collections import defaultdict


def debruijn_graph(reads: list[str], k: int) -> dict[str, set[str]]:
    """Build a directed graph from unique k-mers; multiplicities are not retained."""
    if k < 2:
        raise ValueError("k must be at least two")
    graph: dict[str, set[str]] = defaultdict(set)
    for read in reads:
        for start in range(max(0, len(read) - k + 1)):
            kmer = read[start:start + k]
            left, right = kmer[:-1], kmer[1:]
            graph[left].add(right)
            graph.setdefault(right, set())
    return dict(graph)


def assemble_unambiguous_path(graph: dict[str, set[str]]) -> str:
    """Recover sequence only when graph is exactly one non-branching path.

    A ValueError is raised for disconnected, branched, or cyclic graphs.
    """
    if not graph:
        return ""
    lengths = {len(node) for node in graph}
    if len(lengths) != 1 or next(iter(lengths)) == 0:
        raise ValueError("All graph nodes must have equal non-zero length")
    indegree = {node: 0 for node in graph}
    for node, successors in graph.items():
        if len(successors) > 1:
            raise ValueError("Branching graph: ambiguous assembly")
        for next_node in successors:
            if next_node not in indegree:
                raise ValueError("Graph references an unknown node")
            if node[1:] != next_node[:-1]:
                raise ValueError("Successive nodes do not overlap")
            indegree[next_node] += 1
            if indegree[next_node] > 1:
                raise ValueError("Merging graph: ambiguous assembly")
    starts = [node for node in graph if indegree[node] == 0]
    if len(starts) != 1:
        raise ValueError("Graph is cyclic or disconnected")
    current = starts[0]
    visited = set()
    sequence = current
    while True:
        if current in visited:
            raise ValueError("Cycle encountered")
        visited.add(current)
        next_nodes = graph[current]
        if not next_nodes:
            break
        current = next(iter(next_nodes))
        sequence += current[-1]
    if len(visited) != len(graph):
        raise ValueError("Graph contains disconnected components")
    return sequence
