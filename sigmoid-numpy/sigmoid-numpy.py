import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    x = np.asarray(x, dtype=np.float64)
    pos = x >= 0
    z = np.empty_like(x)
    z[pos] = 1.0 / (1.0 + np.exp(-x[pos]))
    ex = np.exp(x[~pos])
    z[~pos] = ex / (1.0 + ex)
    return z