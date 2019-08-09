'''We would like to register functions. The first way is to make them append themselves to a list when they are called. We use a dictionary registry to store these lists.'''

#A function registry

import functools

registry = {}
def register_at_call(name):
    """Register the decorated function at call time."""
    def _register(func):
        """Takes the function.
        """
        @functools.wraps(func)
        def __register(*args, **kwargs):
            """Takes the arguments.
            """
            registry.setdefault(name, []).append(func)
            return func(*args, **kwargs)
        return __register
    return _register

def register_at_def(name):
    """Register the decorated function at definition time."""
    def _register(func):
        """Takes the function."""
        registry.setdefault(name, []).append(func)
        return func
    return _register
