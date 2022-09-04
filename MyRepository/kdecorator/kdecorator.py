# ###########################################################################
# Libraries of decorators.
# ###########################################################################
import pandas as pd
import numpy as np
from scipy import stats
from functools import (
    wraps,
)  # Used to set output of type(func. decorated) by your own name.
from collections.abc import (
    Sequence,
)  # Adiciona funcionalidade para isinstance "iterável".


def do_have_1d(f):
    """Check if 'f' is 1D colections or 1D unpacked values

    Args:
        f (function or sequence): The object the will be verified

    Returns:
        _type_: The own object functionalized or the proper sequence
    """

    @wraps(f)
    def verificar(*args):
        if len(args) == 1:
            if issubclass(list, Sequence):
                # Check issubclass or isinstance, maybe is a mode of simplification all scope.
                pass
            try:
                a, b = args[0].shape
                return print("Os valores devem ser algo similar a uma lista.")
            except:
                pass
            if isinstance(args[0], pd.DataFrame):
                lista = pd.Series(args[0])
                return f(*lista) if callable(f) else lista
            elif isinstance(args[0], (np.ndarray, pd.Series)):
                lista = args[0].tolist()
                return f(*lista) if callable(f) else lista
            elif isinstance(args[0], (list, tuple)):
                lista = args[0]
                return f(*lista) if callable(f) else lista
            else:
                print("Os valores devem ser algo similar a uma lista")
        if len(args) > 1:
            return f(*args)

    if callable(f):
        return verificar
    else:
        return verificar(f)
