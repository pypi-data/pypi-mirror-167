from typing import TYPE_CHECKING, Any, Dict, List, Tuple
import enum
import numpy as np
from pydantic import BaseModel
from npe2 import PluginContext
from npe2.types import PathOrPaths

if TYPE_CHECKING:
    import napari.types


def activate(context: PluginContext):
    @context.register_command("napari_demo.hello_world")
    def _hello():
        print("hello")

    context.register_command("napari_demo.another_command", lambda: print("world"))


def about():
    raise RuntimeError("This menu is created by napari-demo")


def hello_world():
    raise RuntimeError("hello world")


def deactivate(context: PluginContext):
    """just here for tests"""
    ...


def get_reader(path: PathOrPaths):
    if isinstance(path, list):

        def read(path):
            assert isinstance(path, list)
            return [(None,)]

        return read
    assert isinstance(path, str)  # please mypy.
    if path.endswith(".fzzy"):

        def read(path):
            assert isinstance(path, str)
            return [(None,)]

        return read
    else:
        raise ValueError("Test plugin should not receive unknown data")


def url_reader(path: str):
    if path.startswith("http"):

        def read(path):
            return [(None,)]

        return read


def writer_function(path: str, layer_data: List[Tuple[Any, Dict, str]]) -> List[str]:
    class Arg(BaseModel):
        data: Any
        meta: Dict
        layer_type: str

    for e in layer_data:
        Arg(data=e[0], meta=e[1], layer_type=e[2])

    return [path]


def writer_function_single(path: str, layer_data: Any, meta: Dict) -> List[str]:
    class Arg(BaseModel):
        data: Any
        meta: Dict

    Arg(data=layer_data, meta=meta)

    return [path]


class SomeWidget:
    ...


def random_data():
    import numpy as np

    return [(np.random.rand(10, 10, 10), {"name": "random", "scale": (1, 1, 1)})]


# Enums are a convenient way to get a dropdown menu
class Operation(enum.Enum):
    """A set of valid arithmetic operations for image_arithmetic."""

    add = np.add
    subtract = np.subtract
    multiply = np.multiply
    divide = np.divide


def image_arithmetic(
    first_layer: 'napari.types.ImageData',
    operation: Operation,
    second_layer: 'napari.types.ImageData',
) -> 'napari.types.ImageData':
    """Adds, subtracts, multiplies, or divides two same-shaped image layers."""
    return operation.value(first_layer, second_layer)
