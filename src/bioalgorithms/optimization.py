"""General simulated annealing, related to Week 10 network optimisation."""
from math import exp
from random import Random
from typing import Callable, TypeVar
T = TypeVar("T")

def simulated_annealing(initial: T, objective: Callable[[T],float],
                        neighbour: Callable[[T,Random],T],
                        steps: int=1000, initial_temperature: float=1.0,
                        cooling: float=0.995, seed: int=42) -> tuple[T,float]:
    """Minimise objective while tracking the best state; deterministic given seed."""
    if steps < 0 or initial_temperature<=0 or not 0<cooling<=1:
        raise ValueError("Invalid annealing configuration")
    rng=Random(seed)
    state=initial
    value=objective(state)
    best,best_value=state,value
    temperature=initial_temperature
    for _ in range(steps):
        candidate=neighbour(state,rng)
        candidate_value=objective(candidate)
        delta=candidate_value-value
        if delta<=0 or rng.random()<exp(-delta/temperature):
            state,value=candidate,candidate_value
            if value<best_value:
                best,best_value=state,value
        temperature*=cooling
        temperature=max(temperature,1e-300)
    return best,best_value
