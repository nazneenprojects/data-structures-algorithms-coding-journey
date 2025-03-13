Trees are a subset of graphs.
Trees are made of nodes and edges.
Rooted trees have one node that leads to all the other nodes.
The only node with no parents is the root. 
Nodes with no children are called leaf nodes.


Breadth-first search and depth-first search are closely related, 

Depth-first search cannot be used for finding the shortest path!
only breadth-first search works for finding the shortest path. 
Depth-first search has other uses. It can be used to find the topological sort.

A tree is a connected, acyclic graph.

we are working exclusively with rooted trees, so our trees all have a root as well. And we are working exclusively with connected graphs. So the most important thing to remember is trees cannot have cycles.

A binary tree is a special type of tree where nodes can have at most two children (hence the name binary, meaning two). These are traditionally called left child and right child.
An ancestry tree is an example of a binary tree since everyone has two biological parents.

The important thing is you never have more than two children. 

Sometimes people refer to the left subtree or right subtree.

Huffman coding is a neat example of using binary trees.

https://en.wikipedia.org/wiki/Huffman_coding#:~:text=Once%20the%20Huffman%20tree%20has,the%20right%20child%20as%201.