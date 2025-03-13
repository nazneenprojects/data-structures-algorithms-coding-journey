"""

n = number of nodes
Time: O(n)
Space: O(n)

"""

def depth_first_values(root):
    if not root:
        return []

    stack = [root]
    values = []

    while stack:
        node = stack.pop()
        values.append(node.val)
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)
    return values


"""
n = number of nodes
Time: O(n^2)
Space: O(n)
"""

def depth_first_values_rec(root):
    if not root:
        return []

    left_values = depth_first_values(root.left)
    right_values = depth_first_values(root.right)
    return [root.val, *left_values, *right_values]


if __name__ == "__main__":
    depth_first_values()
    depth_first_values_rec()