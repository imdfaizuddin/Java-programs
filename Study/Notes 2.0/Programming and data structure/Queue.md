Awesome! Let's dive into **queues**, one of the most fundamental data structures in computer science.

---

## 🧠 What is a Queue?

A **queue** is a **linear data structure** that follows the **FIFO** principle:

> **FIFO** = First In, First Out  
> The first element added to the queue is the first one to be removed.

Think of a queue like a line of people waiting at a ticket counter – the person who gets in line first is served first.

---

## ⚙️ Basic Operations

| Operation      | Description                            |
|----------------|----------------------------------------|
| `enqueue(x)`   | Add element `x` to the **rear** of the queue |
| `dequeue()`    | Remove and return the element at the **front** |
| `peek()` / `front()` | Return the front element without removing it |
| `isEmpty()`    | Check if the queue is empty            |
| `size()`       | Return the number of elements in the queue |

---

## 🧱 Implementation Methods

### 1. **Using Arrays / Lists (fixed size or dynamic)**
- Simple and easy for small queues.
- But can be inefficient due to shifting elements when dequeuing.

### 2. **Using Linked List**
- Efficient, no shifting required.
- Dynamic size.

### 3. **Using Python's `collections.deque`**
- Highly optimized for queues.

---

## 🧪 Example in Python

```python
from collections import deque

# Create a queue
queue = deque()

# Enqueue elements
queue.append('A')
queue.append('B')
queue.append('C')

print("Queue:", list(queue))

# Dequeue elements
print("Dequeued:", queue.popleft())
print("Front element:", queue[0])
print("Is queue empty?", len(queue) == 0)
```

---

## ⏱️ Time Complexity

| Operation   | Time Complexity |
|-------------|-----------------|
| Enqueue     | O(1)            |
| Dequeue     | O(1)            |
| Peek/Front  | O(1)            |
| isEmpty     | O(1)            |

---

## 🧊 Variations of Queue

1. **Circular Queue** – Connects rear to front to efficiently use space.
2. **Deque (Double-ended queue)** – You can add/remove from both ends.
3. **Priority Queue** – Elements are dequeued based on priority, not just order.

---