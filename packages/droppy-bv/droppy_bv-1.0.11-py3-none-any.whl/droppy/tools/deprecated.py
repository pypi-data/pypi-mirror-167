from deprecated.classic import ClassicAdapter
from deprecated import deprecated
from typing import Callable, Dict, Any
import functools
import warnings



class ClassicAdapterNoDefaultMessage(ClassicAdapter):
    def get_deprecated_msg(self, *args, **kwargs):
        return self.reason



def renamed_function( fun, old_name="" ):
    """Copy the function and emit a deprecation warning


    Parameters
    ----------
    fun : fun
        The new function
    old_name : str, optional
        The name of the old function. The default is "".

    Returns
    -------
    fun
        The decorated function

    Example
    -------

    >>> test_old = renamed_function(test_new, "test_old")
    >>> test_old()
    DeprecationWarning: test_old has been renamed test_new

    """
    return deprecated( fun, reason = f"{old_name:} has been renamed {fun.__name__:}" , adapter_cls = ClassicAdapterNoDefaultMessage)




# Code from https://stackoverflow.com/questions/49802412/how-to-implement-deprecation-in-python-with-argument-alias
def deprecated_alias(**aliases: str) -> Callable:
    """Decorator for deprecated function and method arguments.

    Example
    -------
    @deprecated_alias(old_arg='new_arg')
    def myfunc(new_arg):
        ...

    """

    def deco(f: Callable):
        @functools.wraps(f)
        def wrapper(*args, **kwargs):
            rename_kwargs(f.__name__, kwargs, aliases)
            return f(*args, **kwargs)

        return wrapper

    return deco


def rename_kwargs(func_name: str, kwargs: Dict[str, Any], aliases: Dict[str, str]):
    """Helper function for deprecating function arguments."""
    for alias, new in aliases.items():
        if alias in kwargs:
            if new in kwargs:
                raise TypeError(
                    f"{func_name} received both {alias} and {new} as arguments!"
                    f" {alias} is deprecated, use {new} instead."
                )
            warnings.warn(
                message=(
                    f"`{alias}` is deprecated as an argument to `{func_name}`; use"
                    f" `{new}` instead."
                ),
                category=DeprecationWarning,
                stacklevel=3,
            )
            kwargs[new] = kwargs.pop(alias)



# Code from https://stackoverflow.com/questions/9008444/how-to-warn-about-class-name-deprecation
class RenamedClass(object):
    def __init__(self, new_target, old_name):
        """Use old class name and emit a warning.

        Parameters
        ----------
        new_target : class
            New class
        old_name : str
            Old class name

        Example
        -------
        >>> OldClass = RenamedClass(NewClass, old_name = "OldClass")
        >>> o = OldClass()
        DeprecationWarning: `OldClass` has been renamed `NewClass`.
        >>>
        """
        self.new_target = new_target
        self.old_name = old_name

    def _warn(self):
        warnings.warn(
            message= f"`{self.old_name:}` has been renamed `{self.new_target.__name__:}`.",
            category=DeprecationWarning,
            stacklevel=3 )

    def __call__(self, *args, **kwargs):
        self._warn()
        return self.new_target(*args, **kwargs)

    def __getattr__(self, attr):
        self._warn()
        return getattr(self.new_target, attr)




if __name__ == "__main__":


    #---- Test function renaming
    def test_new():
        return "1"

    test_old = renamed_function(test_new, "test_old")
    test_old()


    #---- Test method renaming
    class TestClass():
        def new_method_name(self, i) :
            print (i)

    TestClass.oldMethodName = renamed_function(TestClass.new_method_name, "oldMethodName")
    a = TestClass()
    a.oldMethodName(2)


    #---- Test argument renaming
    class MyClass(object):
        @deprecated_alias(object_id='id_object')
        def __init__(self, id_object):
            self.id = id_object

    a = MyClass(  object_id = 1 )



    #---- Test class renaming
    class NewClass() :
        def __init__(self):
            self.test = 1.0

    OldClass = RenamedClass(NewClass, old_name = "OldClass")
    a = OldClass()





