import os
import subprocess


def _dot_var(v, verbose=False):
    dot_var = '{} [label="{}", color=orange, style=filled]\n'
    name = '' if v.name is None else v.name
    if verbose and v.data is not None:
        if v.name is not None:
            name += ': '
        name += str(v.shape) + ' ' + str(v.dtype)
    
    return dot_var.format(id(v), name)


def _dot_func(f):
    dot_func = '{} [label="{}", color=lightblue, style=filled, shape=box]\n'
    txt = dot_func.format(id(f), f.__class__.__name__)

    dot_edge = '{} -> {}\n'
    for x in f.inputs:
        txt += dot_edge.format(id(x), id(f))
    for y in f.outputs:
        txt += dot_edge.format(id(f), id(y())) # y is weakref
    
    return txt


def get_dot_graph(output, verbose=True):
    """Generates a graphviz DOT text of a computational graph.
    Build a graph of functions and variables backward-reachable from the
    output. To visualize a graphviz DOT text, you need the dot binary from the
    graphviz package (www.graphviz.org).
    Args:
        output (dezero.Variable): Output variable from which the graph is
            constructed.
        verbose (bool): If True the dot graph contains additional information
            such as shapes and dtypes.
    Returns:
        str: A graphviz DOT text consisting of nodes and edges that are
            backward-reachable from the output
    """
    txt = ''
    funcs = []
    seen_set = set()

    txt += _dot_var(output, verbose)

    def add_func(f):
        if f is None:
            return
        if f not in seen_set:
            funcs.append(f)
            seen_set.add(f)

    add_func(output.creator)

    while funcs:
        f = funcs.pop()
        txt += _dot_func(f)
            
        for x in f.inputs:
            txt += _dot_var(x, verbose)

            if x.creator is not None:
                add_func(x.creator)

    return 'digraph g {\n' + txt + '}'


def plot_dot_graph(output, verbose=True, to_file='graph.png'):
    dot_graph = get_dot_graph(output, verbose)
    
    # save dot data to temporary file 
    tmp_dir = os.path.join(os.path.expanduser('~'), '.autodiff')
    if not os.path.exists(tmp_dir):
        os.mkdir(tmp_dir)
    graph_path = os.path.join(tmp_dir, 'tmp_graph.dot')

    with open(graph_path, 'w') as f:
        f.write(dot_graph)

    # call dot command with the temporary file
    extension = os.path.splitext(to_file)[1][1:]
    if extension == '':
        raise RuntimeError('empty extenstion in to_file: {}'.format(to_file))
    
    cmd = 'dot {} -T {} -o {}'.format(graph_path, extension, to_file)
    subprocess.run(cmd, shell=True)

    # return the image as a Jupyter Image object, to be displayed in-line.
    try:
        from IPython import display
        return display.Image(filename=to_file)
    except:
        pass