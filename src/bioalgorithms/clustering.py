"""Educational DBSCAN clustering inspired by Week 09."""
from collections import deque
from math import dist

def dbscan(points: list[tuple[float,...]], eps: float, min_samples: int) -> list[int]:
    """Return cluster labels; -1 denotes noise. Core count includes the point itself."""
    if eps < 0 or min_samples < 1:
        raise ValueError("eps must be nonnegative and min_samples >= 1")
    if points and any(len(p)!=len(points[0]) for p in points):
        raise ValueError("All points must have equal dimensions")
    n=len(points)
    neighbours=[[j for j in range(n) if dist(p,points[j])<=eps]
                for p in points]
    labels=[-1]*n
    seen=set()
    cluster_id=0
    for start in range(n):
        if start in seen:
            continue
        seen.add(start)
        if len(neighbours[start]) < min_samples:
            continue
        labels[start]=cluster_id
        queue=deque(neighbours[start])
        enqueued=set(neighbours[start])
        while queue:
            index=queue.popleft()
            if index not in seen:
                seen.add(index)
                if len(neighbours[index])>=min_samples:
                    for j in neighbours[index]:
                        if j not in enqueued:
                            queue.append(j)
                            enqueued.add(j)
            if labels[index] == -1:
                labels[index]=cluster_id
        cluster_id+=1
    return labels
