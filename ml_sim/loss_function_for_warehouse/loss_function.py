import numpy as np


def turnover_error(y_true: np.array, y_pred: np.array) -> float:
    """
    Calculate Root Mean Squared Logarithmic Error between two numpy arrays

    We use the log1p function instead of the log function to avoid errors 
    when taking the logarithm of values close to zero. 
    The log1p function returns the natural logarithm of 1 plus the input value,
    which is mathematically equivalent to log(1 + x) but more numerically
    stable.

    """
    assert len(y_true) == len(
        y_pred), "The length of y_true and y_pred should be the same."
    assert (y_true >= 0).all() and (
        y_pred >= 0).all(), "Both y_true and y_pred should be non-negative."

    # Compute the RMSLE
    error = np.sqrt(np.mean(np.power(np.log1p(y_pred) - np.log1p(y_true), 2)))

    return error
