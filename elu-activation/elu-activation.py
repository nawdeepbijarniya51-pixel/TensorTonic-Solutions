import math
import numpy as np

def elu(x: list, alpha: float = 1.0) -> list:
    """
    Returns ELU applied elementwise to the input values.
    """
    # Write code here
    arr = np.array(x,dtype = float)
    arr2 = arr<0
    arr[arr2] = alpha*(np.exp(arr[arr2])-1)
    return list(arr)