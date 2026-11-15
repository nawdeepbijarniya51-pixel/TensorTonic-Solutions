import numpy as np

def relu(x) -> np.ndarray:
    """
    Returns a NumPy array with the same shape as x.
    """
    # Write code here
    arr = np.array(x)
    arr2 = arr<0
    arr[arr2] = 0
    return arr