class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def print_tree_unicode(root, prefix="", is_left=True):
    if root is not None:
        print_tree_unicode(root.right, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + root.value)
        print_tree_unicode(root.left, prefix + ("    " if is_left else "│   "), True)


if __name__ == "__main__":
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')
    root.right.right = TreeNode('G')

    print_tree_unicode(root)
