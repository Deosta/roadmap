class TreeNode:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
        self.content = None

    def insert(self, value, content=None):
        if value == self.value:
            print(f'{value} already exits, chose a unique key.')
            return None
        if value < self.value:
            if self.left is None:
                self.left = TreeNode(value)
                self.left.content = content
            else:
                self.left.insert(value, content)

        else:
            if self.right is None:
                self.right = TreeNode(value)
                self.right.content = content
            else:
                self.right.insert(value, content)

    def postorder_traversal(self):
        if self.left:
            self.left.postorder_traversal()
        if self.right:
            self.right.postorder_traversal()
        print(self.value)
    
tree = TreeNode(6)
tree.insert(5)
tree.insert(2)
tree.insert(4)
tree.insert(1)
tree.insert(19)
tree.insert(29)
tree.insert(11)

tree.postorder_traversal()