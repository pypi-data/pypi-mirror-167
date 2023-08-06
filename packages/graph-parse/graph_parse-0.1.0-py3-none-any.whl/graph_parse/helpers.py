from typing import Any, Iterable, List, Type
import re


def camel_to_snake(s: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', s).lower()

def snake_to_camel(s: str) -> str:
    return ''.join([chunk.capitalize for chunk in s.split("_")])

def nested_getattr(obj: Type, attrs: List[str]) -> Any:
    return nested_getattr(obj := getattr(obj, attrs.pop(0)), attrs) if attrs else obj

def flatten(d: dict, path: List[str] = []) -> dict:
    result = {}
    for k, v in d.items():
        new_path = path + [k]
        
        if isinstance(v, dict):
            result.update(flatten(v, path=new_path))
        
        result[tuple(new_path)] = v
    return result

def instantiate_many(models: Iterable[Type], *args, **kwargs) -> Any:
    return (model(*args, **kwargs) for model in models)

def iterables_intersect(a: Iterable, b: Iterable) -> bool:
    return bool(set(a).intersection(set(b)))