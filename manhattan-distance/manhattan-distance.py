import numpy as np

def manhattan_distance(x, y):
    """
    Compute the Manhattan (L1) distance between vectors x and y.
    Must return a float.
    """
    X = np.array(x)
    Y = np.array(y)
    manhattan_dist = np.sum(np.abs(X - Y))

    return manhattan_dist.item()

    