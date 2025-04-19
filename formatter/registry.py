from typing import Dict

from formatter.formatters.base_formatter import BaseFormatter

FORMATTER_REGISTRY: Dict[str, BaseFormatter] = {}

def register_formatter(name: str):
    def decorator(cls: BaseFormatter):
        FORMATTER_REGISTRY[name.lower()] = cls
        return cls 
    
    return decorator

def get_formatter(name: str)->BaseFormatter|None:
    formatter_class = FORMATTER_REGISTRY.get(name.lower())
    if not formatter_class:
        return None
    
    return formatter_class