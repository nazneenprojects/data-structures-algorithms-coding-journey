# Recursion
Every recursive function has two parts: 
1. the base case and the recursive case. 
2. The recursive case is when the function calls itself. 

The base case is when the function doesn’t call itself again, so it doesn’t go into an infinite loop.


The “pile of boxes” is saved on the stack! 
This is a stack of half-completed function calls, each with its own half-complete list of boxes to look through. 
Using the stack is convenient because you don’t have to keep track of a pile of boxes yourself—the stack does it for you.

Using the stack is convenient, but there’s a cost: saving all that info can take up a lot of memory. 
Each of those function calls takes up some memory, 
and when your stack is too tall, that means your computer is saving information for many function calls. 
At that point, you have two options:

You can rewrite your code to use a loop instead.

You can use something called tail recursion. That’s an advanced recursion topic that is out of the scope of this book. 
It’s also only supported by some languages, not all.



Q.  Suppose you accidentally write a recursive function that runs forever. As you saw, your computer allocates memory 
on the stack for each function call. What happens to the stack when your recursive function runs forever?

Answer: The stack grows forever. Each program has a limited amount of space on the call stack. 
When your program runs out of space (which it eventually will), it will exit with a stack-overflow error.


Recursion is when a function calls itself.

Every recursive function has two cases: the base case and the recursive case.

A stack has two operations: push and pop.

All function calls go onto the call stack.

The call stack can get very large, which takes up a lot of memory.