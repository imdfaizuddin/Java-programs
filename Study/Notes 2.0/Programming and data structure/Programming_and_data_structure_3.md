# **Stacks - Data Structures & Algorithms (DSA) Notes**  

## **1. Introduction to Stacks**  
- A **stack** is a **linear data structure** that follows the **Last In, First Out (LIFO)** principle.  
- The last element inserted is the first one to be removed.  
- Operations are performed at **one end** called the **top**.  

## **2. Basic Operations on Stack**  
1. **Push(x)** → Inserts an element `x` at the top of the stack.  
2. **Pop()** → Removes and returns the top element.  
3. **Peek() / Top()** → Returns the top element without removing it.  
4. **isEmpty()** → Checks if the stack is empty.  
5. **isFull()** → Checks if the stack is full (for fixed-size implementations).  

## **3. Stack Implementation**  
Stacks can be implemented using:  
1. **Arrays** (Static size)  
2. **Linked Lists** (Dynamic size)  

### **3.1 Stack Implementation Using Array**  
```python
class Stack:
    def __init__(self, size):
        self.size = size
        self.stack = [None] * size
        self.top = -1  # Indicates empty stack

    def push(self, item):
        if self.top == self.size - 1:
            print("Stack Overflow!")
            return
        self.top += 1
        self.stack[self.top] = item

    def pop(self):
        if self.top == -1:
            print("Stack Underflow!")
            return None
        item = self.stack[self.top]
        self.top -= 1
        return item

    def peek(self):
        if self.top == -1:
            return None
        return self.stack[self.top]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1
```

### **3.2 Stack Implementation Using Linked List**  
```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Stack Underflow!")
            return None
        item = self.top.data
        self.top = self.top.next
        return item

    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    def is_empty(self):
        return self.top is None
```

## **4. Time Complexity of Stack Operations**  
| Operation | Time Complexity |
|-----------|-----------------|
| Push      | O(1)            |
| Pop       | O(1)            |
| Peek      | O(1)            |
| isEmpty   | O(1)            |
| isFull    | O(1)            |

## **5. Applications of Stack**  
1. **Function Calls & Recursion** (Call Stack)  
2. **Expression Evaluation & Syntax Parsing**  
   - Infix to Postfix/Prefix conversion  
   - Balanced Parentheses Check `(()), {}, []`  
3. **Undo/Redo Operations** (e.g., in text editors)  
4. **Backtracking Algorithms** (e.g., Maze solving)  
5. **Browser History Management** (LIFO order)  
6. **Memory Management** (Stack memory allocation)  

## **6. Stack vs. Queue**  
| Feature  | Stack (LIFO)         | Queue (FIFO)        |
|----------|---------------------|---------------------|
| Order    | Last In, First Out  | First In, First Out |
| Insert   | `push()` at top     | `enqueue()` at rear |
| Delete   | `pop()` from top    | `dequeue()` from front |
| Uses     | Recursion, Parsing  | BFS, Scheduling     |

## **7. Important Problems on Stack**  
1. **Balanced Parentheses Check**  
2. **Infix to Postfix Conversion**  
3. **Evaluation of Postfix Expression**  
4. **Next Greater Element (NGE) Problem**  
5. **Implement Queue using Stacks**  
6. **Implement Stack using Queues**  
7. **Minimum Stack (O(1) time for getMin)**  

## **8. Practice Questions**  
- **Easy:**  
  - Valid Parentheses (LeetCode #20)  
  - Implement Stack using Queues (LeetCode #225)  
- **Medium:**  
  - Min Stack (LeetCode #155)  
  - Next Greater Element II (LeetCode #503)  
- **Hard:**  
  - Largest Rectangle in Histogram (LeetCode #84)  

---

### **Summary**  
✅ **LIFO Principle** – Last In, First Out  
✅ **Operations:** `push()`, `pop()`, `peek()`, `isEmpty()`  
✅ **Implementation:** Arrays (fixed size) or Linked Lists (dynamic)  
✅ **Applications:** Recursion, Parsing, Undo/Redo, Backtracking  

Would you like a deeper explanation on any specific topic? 😊