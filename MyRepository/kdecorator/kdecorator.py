# ###########################################################################
# Libraries of decorators.
# ###########################################################################
import pandas as pd
import numpy as np
from scipy import stats

from collections.abc import Iterable
from functools import (
    wraps,
)  # Used to set output of type(func. decorated) by your own name.
from collections.abc import (
    Sequence,
)  # Adiciona funcionalidade para isinstance "iterável".
import weakref


def do_have_1d(f):
    """Check if 'f' is 1D colections or 1D unpacked values

    Args:
        f (function or sequence): The object the will be verified

    Returns:
        (function or sequence): The own object functionalized or the proper sequence
    """

    @wraps(f)
    def verificar(*args):
        if len(args) == 1:
            # Verify if the args have only 1 dimension.
            for arg in args[0]:
                if isinstance(arg, Iterable):
                    raise ValueError('The parms must be only 1 dimension.')
                else:
                    pass

            lista = np.array(args[0]).tolist()
            return f(*lista) if callable(f) else lista

            # try:
            #     a, b = args[0].shape
            #     return print("Deve ser repassado valores em 1 dimensão.")
            # except:
            #     pass
            # if isinstance(args[0], pd.DataFrame):
            #     lista = pd.Series(args[0])
            #     return f(*lista) if callable(f) else lista
            # elif isinstance(args[0], (np.ndarray, pd.Series)):
            #     lista = args[0].tolist()
            #     return f(*lista) if callable(f) else lista
            # elif isinstance(args[0], (list, tuple)):
            #     lista = args[0]
            #     return f(*lista) if callable(f) else lista
            # else:
            #     print("Os valores devem ser algo similar a uma lista")
        if len(args) > 1:
            return f(*args)

    if callable(f):
        return verificar
    else:
        return verificar(f)


def lru_cache(maxsize=128, typed=False):
    def decorator(func):
        @wraps(func)
        def wrapped_func(self, *args, **kwargs):
            self_weak = weakref.ref(self)

            @wraps(func)
            @lru_cache(maxsize=maxsize, typed=typed)
            def cached_method(*args, **kwargs):
                return func(self_weak(), *args, **kwargs)

            setattr(self, func.__name__, cached_method)
            return cached_method(*args, **kwargs)

        return wrapped_func

    if callable(maxsize) and isinstance(typed, bool):
        # The user_function was passed in directly via the maxsize argument
        func, maxsize = maxsize, 128
        return decorator(func)

    return decorator
