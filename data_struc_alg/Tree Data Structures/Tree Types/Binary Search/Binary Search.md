A Binary Search Tree (BST) is a type of binary tree data structure where each node carries a unique key (a value), and each key/node has up to two referenced sub-trees, the left and right child. The key feature of a BST is that every node on the right subtree must have a value greater than its parent node, while every node on the left subtree must have a value less than its parent node. This property must be true for all the nodes, not just the root. Due to this property, searching, insertion, and removal of a node in a BST perform quite fast, and the operations can be done in O(log n) time complexity, making it suitable for data-intensive operations.

If key values are repeated, this will waste space, effectively making the tree unbalanced resulting in linear time complexity.

- Skewed trees: If a tree becomes skewed, the time complexity of search, insertion, and deletion operations will be O(n) instead of O(log n), which can make the tree inefficient.
- Additional time required: Self-balancing trees require additional time to maintain balance during insertion and deletion operations.
- Efficiency: BSTs are not efficient for datasets with many duplicates as they will waste space.