from typing import Dict, Type

FORMATTER_REGISTRY: Dict[str, Type] = {}

def register_formatter(name: str):
    def decorator(cls: Type):
        FORMATTER_REGISTRY[name.lower()] = cls
        return cls 
    
    return decorator

def get_formatter(name: str):
    formatter_class = FORMATTER_REGISTRY.get(name.lower())
    if not formatter_class:
        return None
    
    return formatter_class