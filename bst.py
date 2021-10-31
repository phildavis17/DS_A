class BSTNode:
    def __init__(self, data = None) -> None:
        self.data = data
        self.left = None
        self.right = None
    
    def __repr__(self) -> str:
        return(f"BSTNode({self.data})")       

    def __str__(self) -> str:
        return str(self.data)
    
    def __eq__(self, o: object) -> bool:
        pass

    def __hash__(self) -> int:
        pass


class BST:
    def __init__(self) -> None:
        pass

    def insert(self, item: int) -> None:
        pass

    def remove(self, item: int) -> int:
        pass

    def swap_nodes(self, item_a: int, item_b: int) -> None:
        pass
    
    def rebalance(self) -> None:
        pass

    def get_min_value(self) -> int:
        pass

    def get_max_value(self) -> int:
        pass
    
    def clear(self) -> None:
        pass

    def get_dept(self) -> int:
        """Returns the current depth of the tree."""
        pass

    def is_bst(self) -> bool:
        """Returns True if the tree is properly configured bst."""
        pass

    def is_balanced(self) -> bool:
        """
        Returns True if the tree is balanced
        """
        pass

    def is_perfect(self) -> bool:
        """
        Returns True if the tree is perfect
        """
        pass

    def in_order(self):
        """Returns an iterable of the nodes in the tree."""
        pass

    def pre_order(self):
        """Returns an iterable of the nodes in the tree."""
        pass

    def post_order(self):
        """Returns an iterable of the nodes in the tree."""
        pass
