class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def postorder_traversal(node):
    if node is None:
        return
    postorder_traversal(node.left)
    postorder_traversal(node.right)
    print(node.value, end=' ')  # Visit the node


def postorder_traversal_iterative(root):
    if root is None:
        return
    stack = []
    output = []
    stack.append(root)

    while stack:
        node = stack.pop()
        output.append(node.value)

        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    while output:
        print(output.pop(), end=' ')  # Reverse output for correct order


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


    # Performing recursive post-order traversal
    postorder_traversal(root)
    print()  # Newline for clarity

    # Performing iterative post-order traversal
    postorder_traversal_iterative(root)
