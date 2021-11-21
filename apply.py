from functools import partial


class Applicator:
    def __init__(self, value=None):
        self.value = value

    def __rmatmul__(self, other):
        return Applicator(other)
    
    def __or__(self, function):
        return Applicator(function(self.value))

    def __gt__(self, function):
        return function(self.value)
    
    def __repr__(self):
        return f"{self.__class__.__name__}({self.value!r})"



apply = Applicator()


class Partial:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs

    def __rmatmul__(self, function):
        return partial(function, *self.args, **self.kwargs)


part = Partial
