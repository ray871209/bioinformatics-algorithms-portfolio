"""Dependency-free KNN and classification metrics inspired by Week 11."""
from collections import Counter
from math import dist

def knn_predict(train_x: list[tuple[float,...]], train_y: list[str],
                query: tuple[float,...], k: int=3) -> str:
    """Euclidean KNN, with stable vote ties broken by nearest class member."""
    if not 1<=k<=len(train_x) or len(train_x)!=len(train_y):
        raise ValueError("Invalid training data or k")
    if any(len(p)!=len(query) for p in train_x):
        raise ValueError("Dimension mismatch")
    nearest=sorted(range(len(train_x)),key=lambda i:(dist(train_x[i],query),i))[:k]
    counts=Counter(train_y[i] for i in nearest)
    return max(counts,key=lambda label:(counts[label],-next(j for j,i in enumerate(nearest) if train_y[i]==label)))

def classification_accuracy(truth: list[str], prediction: list[str]) -> float:
    if len(truth)!=len(prediction) or not truth:
        raise ValueError("Expected nonempty arrays of equal length")
    return sum(a==b for a,b in zip(truth,prediction))/len(truth)

def confusion_counts(truth: list[str], prediction: list[str]) -> dict[tuple[str,str],int]:
    """Map (actual, predicted) pairs to their frequencies."""
    if len(truth)!=len(prediction):
        raise ValueError("Expected equal lengths")
    return dict(Counter(zip(truth,prediction)))
