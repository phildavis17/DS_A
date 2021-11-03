from typing import Any

class Stack:
    def __init__(self) -> None:
        self.data = []

    def push(self, item: Any) -> None:
        self.data.append(item)
    
    def pop(self) -> Any:
        return self.data.pop()
    
    def peek(self) -> Any:
        return self.data[-1]
    
    def index_of(self, item) -> int:
        """Returns the number of pops until the specified item is at the end of the stack."""
        for i, entry in enumerate(self.data[::-1]):
            if entry == item:
                return i
        raise ValueError(f"{item} not in stack.")

    def is_empty(self) -> bool:
        return not self.data
    
    def clear(self) -> None:
        self.data = []

    def __contains__(self, item: Any) -> bool:
        return item in self.data

    def __len__(self) -> int:
        return len(self.data)

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        return str(self.data)
