# Binary Search Tree
## Description

A binary search tree is a special case of a binary tree, which is in turn a special case of a generic tree. A generic tree is a graph-like data structure with a single root node, and no cycles. Nodes in the tree may or may not have children. A binary tree is a tree in which all nodes have at most 2 children. A binary search tree is a binary tree in which the value of a node's left child is always less than that node's value, and the node's right child is greater than that node. For instance:
`##        0`
`#  /   \ `
`#-1    1`

Implementations differ on what to do with equal values. Sometimes they will be on the right, sometimes on the left, and sometimes all the values must be unique.

## Key Characteristics
Binary search trees allow for fast searching because of the consequences of their organization. *Every* value in the left subtree is less than the root node, and *every* value in the right subtree is greater than the root node (equal values, again, may vary). This allows a search to completely ignore a bunch of nodes at once based on a single evaluation.

## Special Conditions
There are a bunch of special conditions that may or may not occur in a any given BST.

**Complete** - A binary tree is "complete" if every level of the tree except the last one is full, and any nodes in the last level are as far to the left as possible.

**Full** - A binary tree is "full" if every node has either zero or two children.

**Perfect** - A binary tree is "perfect" if every level is full, and all the leaf nodes are on the same level. Basically, this is like a little idealized diagram you might draw of a binary tree. To be perfect, a tree must have exactly 2**(k-1) nodes, where k is the depth of the tree. This is a rare condition. 

**Balanced** - What constitutes a "balanced" tree varies from situation to situation. Broadly, the intention is to determine whether the nodes are evenly distributed among the subtrees. This better this distribution is, the more effective a BST is, so this is a good thing to be able to check. As a rough guideline, let's say a tree is balanced if the depth of the two subtrees from any node vary by no more than 1.

## Navigating Trees
There are 3 major methods for moving through a tree data structure, including BSTs. These are generally recursive.

**In-Order Traversal** - Visit the left subtree, then the root node, then the right subtree. 
**Pre-Order Traversal** - Visit the root node, then the subtrees. Usually left then right, but the important part is root first.
**Post-Order Traversal** - Visit the subtrees first, then the root node. Again, left then right is common, but the important part is the bottom up approach. The root node of the tree is always the last node visited by this approach.

Note: These traversal methods are related to the Depth First and Breadth First search approaches. They are also aided by using stacks and queues 


## Reference Material
- [Wikipedia](https://en.wikipedia.org/wiki/Binary_search_tree)
- [geeksforgeeks](https://www.geeksforgeeks.org/binary-search-tree-data-structure/)

## Big O Performance
**Access:** O(long(n))
**Search:** O(log(n))
**Insertion:** O(log(n))
**Deletion:** O(log(n))
**Space Complexity:** O(n)

**NOTE:** These time complexities are average values. A poorly arranged BST gets O(n) performance on all operations.
