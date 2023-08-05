from audiff.module_config import use_simple_core
if use_simple_core:
    from audiff.core_simple.variable import Variable
    from audiff.core_simple.arithmetic_operator import setup_variable   
else:
    from audiff.core.variable import Variable
    from audiff.core.arithmetic_operator import setup_variable   

from audiff.function import Function
from audiff.calc_utils import numerical_diff, allclose
from audiff.analytic_function import square, exp, sin, cos, tanh
from audiff.config import using_config, no_grad
from audiff.utils import get_dot_graph, plot_dot_graph


setup_variable()
__version__ = '0.0.1'