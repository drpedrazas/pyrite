from typing import NamedTuple
import numpy as np

class StandardScalerParams(NamedTuple):
    mean: np.ndarray
    std: np.ndarray

class MinMaxScalerParams(NamedTuple):
    min_val: np.ndarray
    max_val: np.ndarray

class RobustScalerParams(NamedTuple):
    median: np.ndarray
    iqr: np.ndarray

class LinearParams(NamedTuple):
    weights: np.ndarray
    bias: float

class SVMParams(NamedTuple):
    weights: np.ndarray
    bias: float

class LogisticParams(NamedTuple):
    weights: np.ndarray
    bias: float