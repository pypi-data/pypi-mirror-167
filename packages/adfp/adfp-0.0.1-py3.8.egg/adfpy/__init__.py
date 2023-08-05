from adfpy.module_config import use_simple_core
if use_simple_core:
    from adfpy.core_simple.variable import Variable
    from adfpy.core_simple.arithmetic_operator import setup_variable   
else:
    from adfpy.core.variable import Variable
    from adfpy.core.arithmetic_operator import setup_variable   

from adfpy.function import Function
from adfpy.calc_utils import numerical_diff, allclose
from adfpy.analytic_function import square, exp, sin, cos, tanh
from adfpy.config import using_config, no_grad
from adfpy.utils import get_dot_graph, plot_dot_graph


setup_variable()
__version__ = '0.0.1'