class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def inorder_traversal_recursive(node):
    if node is None:
        return
    inorder_traversal_recursive(node.left)
    print(node.value, end=' ')  # Visit the node
    inorder_traversal_recursive(node.right)


def inorder_traversal_iterative(root):
    stack = []
    current = root

    while current is not None or stack:
        while current is not None:
            stack.append(current)
            #print("\n append", current.value)
            current = current.left

        current = stack.pop()

        print(current.value, end=' ')  # Visit the node

        current = current.right


# Example usage:
if __name__ == "__main__":
    # Creating a sample tree
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')
    root.right.right = TreeNode('G')

    # Performing in-order traversal
    print("\n Recursive Approach")
    inorder_traversal_recursive(root)
    print("\n Iterative Approach")
    inorder_traversal_iterative(root)