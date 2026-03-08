#
import inspect

from SpellWriting.generation import edge, node, necklace
from SpellWriting.abstract import IterEnum

_get_functions = lambda module: [
    (name.capitalize(), func) 
    for name, func in inspect.getmembers(module, inspect.isfunction)]


ordering = {}
for mod in [node, edge, necklace]:
    print(mod.__name__)
# TODO SpellGeneration IterEnum
SpellGeneration = IterEnum('SpellGeneration', names=tuple())