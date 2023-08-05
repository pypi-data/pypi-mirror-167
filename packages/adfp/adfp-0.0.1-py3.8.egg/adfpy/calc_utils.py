import numpy as np

from adfpy.module_config import use_simple_core
if use_simple_core:
    from adfpy.core_simple.variable import Variable, as_variable
else:
    from adfpy.core.variable import Variable, as_variable
from adfpy.function import as_array


def numerical_diff(f, x, eps=1e-4):
    x0 = Variable(as_array(x.data - eps))
    x1 = Variable(as_array(x.data + eps))
    y0 = f(x0)
    y1 = f(x1)
    return (y1.data - y0.data) / (2 * eps)


def allclose(lhs, rhs):
    return np.allclose(lhs.data, rhs.data)