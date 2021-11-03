
from typing import Any


class LLNode:
    
    def __init__(self, data: Any = None) -> None:
        self.data = data
        self.next = None

    def __repr__(self) -> str:
        return f"LLNode({self.data})"
    
    def __str__(self) -> str:
        return str(self.data)

    def __eq__(self, o: object) -> bool:
        return self.data == o
    
    def __hash__(self) -> int:
        return hash(self.data)

class LinkedList:
    def __init__(self) -> None:
        self.head = None
    
    def append(self, item: Any) -> None:
        new_node = LLNode(item)
    
    def get_nth(self, index: int) -> Any:
        pass

    def get_nth_from_end(self, index: int) -> Any:
        pass

    def clear(self) -> None:
        self.head = None
    
    def __bool__(self) -> bool:
        return not self.head == None
    
    def __len__(self) -> int:
        pass

    def __contains__(self, item: Any) -> bool:
        pass

    def __repr__(self) -> str:
        pass

    def __str__(self) -> str:
        pass
    