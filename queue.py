
from functools import wraps
from typing import Any, Callable


class Queue:

    def __init__(self) -> None:
        self.data = []
    
    def enqueue(self, item: Any) -> None:
        self.data.append(item)
    
    def dequeue(self) -> Any:
        return self.data.pop(0)
    
    def peek(self) -> Any:
        return self.data[0]
    
    def index_of(self, item: Any) -> int:
        pass

    def clear(self) -> None:
        self.data = []

    def __contains__(self, item: Any) -> int:
        pass

    def __len__(self) -> int:
        return len(self.data)
    
    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass
    
    def raise_if_empty(self, func: Callable) -> Callable:
        def raise_wrapper(*args, **kwargs):
            if not self.data:
                raise EmptyQueueError()
            else:
                return func(*args, **kwargs)
        return raise_wrapper

class EmptyQueueError(Exception):
    pass
