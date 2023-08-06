from typing import Any, Callable, Iterable, Iterator, Tuple, List, TypeVar, Union, overload, ModuleType
import drjit
import drjit as dr

class ADScope:
    """
    Members:
    
      Suspend
    
      Resume
    
      Isolate
    """

    def __init__(self: drjit.detail.ADScope, value: int) -> None: ...
    name = ...
    "name(self: handle) -> str"
    value = ...

    Isolate = 3
    """
      Isolate
    """
    Resume = 2
    """
      Resume
    """
    Suspend = 1
    """
      Suspend
    """

    ...

def _loop_process_state(value: type, in_state: list, out_state: list, write: bool, in_struct: bool = False):
    """
    
    This helper function is used by ``drjit.*.Loop`` to collect the set of loop
    state variables and ensure that their types stay consistent over time. It
    traverses a python object tree in ``value`` and writes state variable
    indices to ``out_state``. If provided, it performs a consistency check
    against the output of a prior call provided via ``in_state``. If ``write``
    is set to ``True``, it mutates the input value based on the information in
    ``in_state``.
    
    """
    ...

def array_configure(cls, shape, type_, value):
    """
    Populates an Dr.Jit array class with extra type trait fields
    """
    ...

def array_from_dlpack(t, capsule): ...
def array_init(self, args):
    """
    
    This generic initialization routine initializes an arbitrary Dr.Jit array
    from a variable-length argument list (which could be a scalar broadcast, a
    component list, or a NumPy/PyTorch/Tensorflow array..)
    
    """
    ...

def array_name(prefix, vt, shape, scalar):
    """
    
    Determines the name of an array (e.g. Float32, ArrayXf32, etc.). This
    function is used when arrays are created during initialization of the Dr.Jit
    extension module, and during implicit type promotion where array types are
    determined dynamically.
    
    Parameter ``prefix`` (``str``):
    Array flavor prefix (Array/Matrix/Complex/Quaternion)
    
    Parameter ``vt`` (``drjit.VarType``):
    Underlying scalar type (e.g. ``VarType.Int32``) of the desired array
    
    Parameter ``shape`` (``Tuple[int]``):
    Size per dimension
    
    Parameter ``scalar`` (``bool``):
    Arrays in the ``drjit.scalar.*`` module use a different depth
    convention, which is indicated via this parameter.
    
    """
    ...

def device(arg0: int) -> int: ...
def diff_vars(o, indices, check_grad_enabled=True):
    """
    
    Extract indices of differentiable variables, returns
    the type of the underlying differentiable array
    
    """
    ...

@overload
def eval(arg0: int) -> int: ...
@overload
def eval() -> None: ...
def fmadd_scalar(arg0: float, arg1: float, arg2: float) -> float: ...
def from_dlpack(arg0: capsule) -> dict: ...
def get_args_values(f, *args, **kwargs):
    """
    
    Given a function, a tuple of positional arguments and a dict of keyword
    arguments, return the full tuple of positional arguments, including default
    values and keyword arguments at the right position.
    
    Here is a simple example:
    
    def f(a, b, c=1, d=2):
    pass
    get_args_values(f, 6, 5, d=4) # returns (4, 5, 1, 4)
    
    """
    ...

def graphviz() -> str: ...
def graphviz_ad() -> str: ...
def idiv(arg0: drjit.VarType, arg1: object) -> object: ...
def loop_process_state(loop, funcs, state, write): ...
def printf_async(arg0: bool, arg1: int, arg2: str, arg3: List[int]) -> None: ...
class reinterpret_flag:
    def __init__(self: drjit.detail.reinterpret_flag) -> None: ...
    ...

def reinterpret_scalar(arg0: object, arg1: drjit.VarType, arg2: drjit.VarType) -> object: ...
def schedule(arg0: int) -> int: ...
def slice_tensor(shape, indices, uint32):
    """
    
    This function takes an array shape (integer tuple) and a tuple containing
    slice indices. It returns the resulting array shape and a flattened 32-bit
    unsigned integer array containing element indices.
    
    """
    ...

def sub_len(o): ...
def tensor_getitem(tensor, slice_arg): ...
def tensor_init(tensor_type, obj): ...
def tensor_setitem(tensor, slice_arg, value): ...
def to_dlpack(owner: object, data: int, type: drjit.VarType, device: int, shape: tuple, strides: tuple) -> capsule: ...
