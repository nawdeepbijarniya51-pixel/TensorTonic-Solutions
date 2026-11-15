import numpy as np

def leaky_relu(x: list | float, alpha: float = 0.01) -> np.ndarray:
    """
    Returns elementwise Leaky ReLU values as a NumPy array matching the input shape.
    """
    # Write code here
    arr = np.array(x,dtype = float)
    arr2 = arr<0
    arr[arr2] = alpha*arr[arr2]
    return arr