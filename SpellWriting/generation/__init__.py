#
import inspect


_get_functions = lambda module: [
    (name.capitalize(), func) 
    for name, func in inspect.getmembers(module, inspect.isfunction)]

Nodes = Enum('Nodes', dict(_get_functions(bases)))


# TODO SpellGeneration IterEnum