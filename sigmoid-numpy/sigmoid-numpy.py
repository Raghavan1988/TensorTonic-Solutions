import numpy as np

def sigmoid(x):
    """
    Vectorized sigmoid function.
    """
    
    X = np.asarray(x, dtype=np.float64) # 
    pos = X >= 0 ## creates a masked array
    neg = X < 0 ## creates 
    
    z = np.empty_like(X) ## intitializing the tensor shapes
    #catch (do the calculation separately for positive values and negative values)
    z[pos] = 1.0 / (1.0 + np.exp(-X[pos]))
    ## if the input itself is negative ( e^x / (1 + e^x))
    Y = np.exp(X[neg])
    z[neg] = Y / (1.0 + Y)
    return z