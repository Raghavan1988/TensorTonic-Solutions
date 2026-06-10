import numpy as np

def euclidean_distance(x, y):
    """
    Compute the Euclidean (L2) distance between vectors x and y.
    Must return a float.
    """
    X = np.array(x)
    Y = np.array(y)
    euclidean_dist = np.sqrt(np.sum(np.square(X - Y))).item()


    return euclidean_dist