
from typing import Callable, List, Set, Tuple
from pydash.objects import get, set_

from graph_parse.enums import ComparitiveOperationEnum
from graph_parse.helpers import iterables_intersect, nested_getattr, camel_to_snake, flatten


class Node:
    __path: List[str]
    
    def __init__(self, path=[], value=None, **kwargs):
        self.__path = path or [self.class_snake_name]
        self.__value = value or self

        globals()[f"node_{self.class_snake_name}"] = self.__class__

        for name in self.__annotations__:
            if name.startswith("_Node__"):
                continue

            new_path = self.__path + [name]
            new_value = kwargs.get(name)
            new_kwargs = new_value.to_dict() if isinstance(new_value, Node) else {}

            private_name = f"_{name}"

            setattr(self, private_name, Node(path=new_path, value=new_value, **new_kwargs))
            setattr(self.__class__, name, property(self.create_getter(private_name)))

    def __call__(self) -> List[str]:
        return self.__path

    def to_dict(self) -> dict:
        result = {}

        for name in self.__annotations__:
            value = getattr(self, name)
            if isinstance(value, Node):
                value = value.to_dict() 
            result[name] = value 

        return result


    def create_getter(self, private_prop_name: str) -> Callable:
        def getter(self):
            return nested_getattr(self, [private_prop_name, "_Node__value"])
        return getter


    @property
    def class_snake_name(self) -> str:
        return camel_to_snake(self.__class__.__name__)

class Edge:
    source: List[str] 
    sink: List[str]
    serialized: Tuple

    def __init__(self, source: List[str], sink: List[str], function: Callable = None):
        self.source = source
        self.sink = sink
        self.function = function

        self.serialized = (tuple(self.source), tuple(self.sink), self.function and self.function.__name__)


class Graph:
    def __init__(self, edges: List[Edge] = []):
        self.edges = edges

    def traverse(self, *args) -> dict:
        state = {arg.class_snake_name: arg.to_dict() for arg in args}

        edges_traversed = set()
        complete = False

        while not complete:
            complete = True
            flattened_state = flatten(state).items()

            for path, value in flattened_state:
                edges = self.find_edges(source=path, exclude=edges_traversed)

                if not edges:
                    continue
                
                complete = False

                for edge in edges:
                    value = get(state, edge.source)
                    
                    if edge.function:
                        if self.find_edges(sink=tuple(edge.source), comparitive_operator=ComparitiveOperationEnum.contain, exclude=edges_traversed.union({edge.serialized})):
                            continue
                        
                        input_model = edge.function.__annotations__[edge.source[-1]]
                        input = input_model(**value) if issubclass(input_model, Node) else value
                        output = edge.function(input)
                        value = output.to_dict() if isinstance(output, Node) else output

                    set_(state, edge.sink, value)
                    edges_traversed.add(edge.serialized)
        
        for name, _dict in state.items():
            if not (model := globals()[f"node_{name}"]):
                continue
            state[name] = model(**_dict)
        return state

    def find_edges(
        self, 
        source: Tuple[str] = None, 
        sink: Tuple[str] = None, 
        exclude: Set[Tuple[str]] = None, 
        comparitive_operator: ComparitiveOperationEnum = ComparitiveOperationEnum.equal
    ) -> List[Edge]:

        def compare(path1, path2):
            if comparitive_operator == ComparitiveOperationEnum.equal:
                return path1 == path2 
            elif comparitive_operator == ComparitiveOperationEnum.contain:
                return iterables_intersect(path1, path2)

        def conditions(edge: Edge):
            if exclude and edge.serialized in exclude:
                return False 
            if source and not compare(tuple(edge.source), source):
                return False 
            if sink and not compare(tuple(edge.sink), sink):
                return False 
            return True

        return [edge for edge in self.edges if conditions(edge)]


