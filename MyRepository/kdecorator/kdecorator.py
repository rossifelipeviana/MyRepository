# ###########################################################################
# Libraries of decorators.
# ###########################################################################
import pandas as pd
import numpy as np
from time import time
from functools import (
    wraps,
)  # Used to set output of type(func. decorated) by your own name.
from collections.abc import (
    Sequence,
)  # Adiciona funcionalidade para isinstance "iterável".


def do_have_1d(func):
    """Check if 'func' is 1D colections or 1D unpacked values

    Args:
        func (function or sequence): The object the will be verified

    Returns:
        (function or sequence): The own object functionalized or the proper sequence
    """

    @wraps(func)
    def verificar(*args):
        if len(args) == 1:
            if issubclass(list, Sequence):
                # Check issubclass or isinstance, maybe is a mode of simplification all scope.
                pass

            try:
                a, b = args[0].shape
                print(a + b)
                return print("Os valores devem ser algo similar a uma lista.")
            except Exception:
                pass

            if isinstance(args[0], pd.DataFrame):
                lista = pd.Series(args[0])
            elif isinstance(args[0], (np.ndarray, pd.Series)):
                lista = args[0].tolist()
            elif isinstance(args[0], (list, tuple)):
                lista = args[0]
            else:
                print("Os valores devem ser algo similar a uma lista")
        elif len(args) > 1:
            return func(*args)
        else:
            return print(
                "Como que uma função recebeu argumentos negativos ou complexo?"
            )
        return func(*lista) if callable(func) else lista

    return verificar if callable(func) else verificar(func)


def timeit(func):
    @wraps(func)
    def timeit_wrapper(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        end_time = time()
        total_time = end_time - start_time
        print(
            f'Function {func.__name__}{args} {kwargs} Took {total_time:.4f} seconds'
        )
        return result

    return timeit_wrapper
