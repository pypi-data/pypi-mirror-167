def method_verbosity(method):
    def wrapper(self, *args, **kwargs):
        if self.verbose:
            print(f'Running {method.__name__}')
        return method(self, *args, **kwargs)
    return wrapper


def func_verbosity(func):
    def wrapper(*args, **kwargs):
        verbose = kwargs.get('verbose')
        if verbose:
            print(f'Running {func.__name__}')
        return func(*args, **kwargs)
    return wrapper
