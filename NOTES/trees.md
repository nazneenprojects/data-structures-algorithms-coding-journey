## Pseudo Code - In order

function inorderTraversal(node):
    if node is null:
        return
    inorderTraversal(node.left)
    visit(node)  // Process the current node (e.g., print its value)
    inorderTraversal(node.right)

function inorderTraversalIterative(root):
    stack = empty stack
    current = root
    
    while current is not null OR stack is not empty:
        // Reach the leftmost node
        while current is not null:
            stack.push(current)
            current = current.left
            
        // Current is now null, pop from stack
        current = stack.pop()
        
        // Visit the node
        visit(current)
        
        // Move to the right subtree
        current = current.right


## Pseudo Code - PreOrder

function preorderTraversal(node):
    if node is null:
        return
    visit(node)  // Process the current node (e.g., print its value)
    preorderTraversal(node.left)
    preorderTraversal(node.right)


function preorderTraversalIterative(root):
    if root is null:
        return
    
    stack = empty stack
    stack.push(root)
    
    while stack is not empty:
        current = stack.pop()
        
        visit(current)  // Process the current node (e.g., print its value)
        
        // Push right child first, then left child to stack (so left is processed first)
        if current.right is not null:
            stack.push(current.right)
        if current.left is not null:
            stack.push(current.left)



## Pseudo Code - PostOrder

function postorderTraversal(node):
    if node is null:
        return
    postorderTraversal(node.left)
    postorderTraversal(node.right)
    visit(node)  // Process the current node (e.g., print its value)


function postorderTraversalIterative(root):
    if root is null:
        return
    
    stack1 = empty stack
    stack2 = empty stack
    stack1.push(root)
    
    while stack1 is not empty:
        current = stack1.pop()
        stack2.push(current)
        
        // Push left child first, then right child to stack1
        if current.left is not null:
            stack1.push(current.left)
        if current.right is not null:
            stack1.push(current.right)
    
    // Process nodes in stack2
    while stack2 is not empty:
        current = stack2.pop()
        visit(current)  // Process the current node (e.g., print its value)
