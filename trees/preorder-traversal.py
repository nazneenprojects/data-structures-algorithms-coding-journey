class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def preorder_traversal(node):
    if node is None:
        return
    print(node.value, end=' ')  # Visit the node
    preorder_traversal(node.left)
    preorder_traversal(node.right)


def preorder_traversal_iterative(root):
    if root is None:
        return
    stack = [root]

    while stack:
        node = stack.pop()
        print(node.value, end=' ')  # Visit the node

        if node.right:
            stack.append(node.right)  # Push right child first
        if node.left:
            stack.append(node.left)  # Push left child last (so it's processed first)


# Example usage:
if __name__ == "__main__":
    # Creating a sample tree based on the provided image
    root = TreeNode('A')
    root.left = TreeNode('B')
    root.right = TreeNode('C')
    root.left.left = TreeNode('D')
    root.left.right = TreeNode('E')
    root.right.left = TreeNode('F')
    root.right.right = TreeNode('G')

    # Performing recursive in-order traversal
    preorder_traversal(root)
    print()  # Newline for clarity

    # Performing iterative in-order traversal
    preorder_traversal_iterative(root)
    print()  # Newline for clarity

