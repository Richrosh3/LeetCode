"""
[MEDIUM]

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

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
minStack.getMin(); // return -2


Constraints:
-2^31 <= val <= 2^31 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
"""
class MinStack:

    def __init__(self):
        self.stack = []
        self.mins = []

    def push(self, val: int) -> None:
        if not self.mins or val <= self.mins[-1]:
            self.mins.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        if self.stack[-1] == self.mins[-1]:
            self.mins.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.mins[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

"""
Time Complexity: O(1) for each operation
Space Complexity: O(n)

Explanation: 
    To keep track of our incoming push's and pop's we initialize a regular stack called "stack"
    
    Now to keep track of our minimum numbers, we could've just initialized a integer variable that is the smallest number
    in the stack. However, what if that number got popped from the stack, then we would have to perform a search through
    our stack to find the new smallest number. The search would be a O(n) operation, but we want a method that is bound 
    to be O(1). 
    
    To do this, we create another stack that will keep track of our minimum value in the stack. Each time we push to stack, 
    we check to see the if the new value being pushed is less than the last value in the stack. If it is, we push it to
    the mins stack. The last value in the mins stack will always correspond to the minimum value among the actual stack. 
    If the minimum value gets popped from the actual stack, we know the new minimum value is the last value of mins. 
    
    Only thing to be careful of is when pushing and popping, we have to do a check to see if we are appending to both stacks, 
    or popping from both stacks. 
    
    Time Complexity will always be O(1) since we are basically only looking at the last values of each stack at all times. 
    For Space Complexity, the worst case would be O(n) + O(n) for both stack and mins, which means that every new value that 
    was pushed was a minimum value. O(n) + O(n) --> O(2n) which simplifies to O(n). 
"""