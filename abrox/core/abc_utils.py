import numpy as np
from itertools import chain

# ABC utility functions


def euclideanDistance(a,b,axis=1):
    """
    Compute euclidean distance either for each row (default)
    or for a and b being one-element arrays (axis=0)
    :param a: Simulated summary statistics
    :param b: observed summary statistics
    :param axis: row (1) or col(0)
    :return: euclidean distance
    """
    return np.linalg.norm(a-b,axis=axis)


def toArray(df, name):
    """
    Convert pandas column to numpy array.
    :param df: the pandas dataframe
    :param name: the column name
    :return: a multidimensional numpy array
    """
    aList = list(df[name].values)
    if isinstance(aList[0], list):
        return np.array(aList)
    else:
        return np.array(aList).reshape(-1, 1)
