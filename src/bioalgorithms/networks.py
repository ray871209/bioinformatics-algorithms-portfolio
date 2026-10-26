"""Small undirected-graph algorithms inspired by Week 05."""
from collections import Counter, deque

def degree_distribution(graph: dict[str,set[str]]) -> dict[int,int]:
    """Histogram of degrees in an undirected adjacency map."""
    return dict(sorted(Counter(len(v) for v in graph.values()).items()))

def clustering_coefficient(graph: dict[str,set[str]], node: str) -> float:
    """Local clustering coefficient, zero for vertices with degree < 2."""
    if node not in graph:
        raise KeyError(node)
    neighbours = sorted(graph[node])
    n = len(neighbours)
    if n < 2:
        return 0.0
    edges = sum(v in graph.get(u, set()) for i,u in enumerate(neighbours)
                for v in neighbours[i+1:])
    return 2 * edges / (n*(n-1))

def reachable_bfs(graph: dict[str,set[str]], source: str, target: str) -> bool:
    """Reachability by breadth-first search in O(V+E)."""
    if source not in graph or target not in graph:
        return False
    queue = deque([source])
    seen = {source}
    while queue:
        u = queue.popleft()
        if u == target:
            return True
        for v in graph.get(u,set()):
            if v not in seen:
                seen.add(v)
                queue.append(v)
    return False
