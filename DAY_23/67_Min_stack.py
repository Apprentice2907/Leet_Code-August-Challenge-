'''Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
You must implement a solution with O(1) time complexity for each function.

 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2'''







# Simple stack logic common

class MinStack(object):

    def __init__(self):
        self.st = []
        self.minst = []

    def push(self, val):
        self.st.append(val)
        if not self.minst:
            self.minst.append(val)
        else:
            cur = self.minst[-1]
            if val <= cur:
                self.minst.append(val)
            else:
                self.minst.append(cur)

    def pop(self):
        if self.st:
            self.st.pop()
            self.minst.pop()

    def top(self):
        if self.st:
            return self.st[-1]
        return None

    def getMin(self):
        if self.minst:
            return self.minst[-1]
        return None
