"""
n = number of nodes
Time: O(n)
Space: O(n)
"""

from collections import deque


def breadth_first_values(root):
    if not root:
        return []

    queue = deque([root])
    values = []

    while queue:
        node = queue.popleft()

        values.append(node.val)

        if node.left:
            queue.append(node.left)

        if node.right:
            queue.append(node.right)

    return values


if __name__ == "__main__":
    breadth_first_values()
  