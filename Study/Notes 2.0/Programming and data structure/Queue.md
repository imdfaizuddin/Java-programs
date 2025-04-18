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

Absolutely! Let’s take a deeper dive into each type of **queue**, how they work internally, and when to use them. I’ll include visual examples and descriptions to help you fully understand.

---

## 1. 🌱 **Simple Queue (Linear Queue)**

### 🧠 Concept:
A basic FIFO queue. You add elements at the **rear**, and remove them from the **front**.

### 🧱 How it works (array example):

```plaintext
Initial: [ ]        # empty queue
Enqueue A: [A]      # rear = 0, front = 0
Enqueue B: [A, B]   # rear = 1
Dequeue(): [B]      # front = 1, A is removed
```

- Implemented with an array or list.
- After a few dequeues, the front keeps moving forward and wastes space.

### ⛔ Limitation:
In arrays, once the rear reaches the end, no more insertions even if space is available at the front.

---

## 2. 🔁 **Circular Queue**

### 🧠 Concept:
Same FIFO logic, but treats the array as **circular** – connects the end of the array back to the beginning.

### 🧱 How it works (array of size 5):

```plaintext
Initial: [_, _, _, _, _] (front = -1, rear = -1)
Enqueue A: front = 0, rear = 0 → [A, _, _, _, _]
Enqueue B: rear = 1 → [A, B, _, _, _]
Dequeue A: front = 1 → [_, B, _, _, _]
Enqueue C, D, E: rear = 2, 3, 4 → [_, B, C, D, E]
Enqueue F: rear = 0 (wrap around!) → [F, B, C, D, E]
```

### ✅ Advantage:
- No wasted space after dequeuing.
- Better for **fixed-size buffers**, like CPU scheduling or streaming.

---

## 3. 🥇 **Priority Queue**

### 🧠 Concept:
Each element has a **priority**. The element with the **highest priority** is served first.

### 🧱 How it works:

- Instead of dequeuing the front, it dequeues the element with the highest priority.
- Can be **min-priority** (smallest value comes first) or **max-priority** (largest value comes first).

### 🛠️ Implementation:
- Using **heaps** (binary heap – min or max).
- Using **sorted list/array** (less efficient).

### Example:
```plaintext
Enqueue(3), Enqueue(5), Enqueue(1)
Queue: [1, 3, 5]  (min-heap)
Dequeue(): 1 (highest priority)
```

### 🧠 Use Cases:
- Job/task scheduling
- Pathfinding algorithms (like Dijkstra’s)

---

## 4. 🔁🔄 **Deque (Double-Ended Queue)**

### 🧠 Concept:
You can **insert and delete** from **both front and rear**.

### Operations:
- `insertFront(x)`
- `insertRear(x)`
- `deleteFront()`
- `deleteRear()`

### 🧱 How it works:

```plaintext
Initial: [ ]
insertRear(A): [A]
insertFront(B): [B, A]
deleteRear(): [B]
```

### Use Cases:
- Undo operations (like in editors)
- Sliding window algorithms (like in max in subarray)
- Palindrome checking

---

## 5. 🔄⚙️ **Circular Deque**

### 🧠 Concept:
Like deque, but uses circular logic for fixed-size arrays.

### ✅ Benefit:
- Combines the flexibility of a deque with the space-efficiency of a circular queue.
- Useful in problems where memory limits are tight and both-end access is needed.

---

## 🧮 Summary Table Again (Now with Use Cases)

| Queue Type         | Key Feature                  | Use Case Example                         |
|--------------------|------------------------------|-------------------------------------------|
| Simple Queue       | FIFO                         | Task queues, printer spooling             |
| Circular Queue     | FIFO + memory-efficient      | CPU scheduling, streaming buffers         |
| Priority Queue     | Based on priority             | OS process management, Dijkstra’s algo    |
| Deque              | Insert/delete both ends      | Undo/redo, palindrome check, sliding window |
| Circular Deque     | Circular + Deque behavior    | LRU cache, history navigation             |

---

Great! You're diving deeper now 😎  
Let’s explore **Input Restricted Deque** and **Output Restricted Deque**, which are special types of **Deques (Double-Ended Queues)**.

---

## 🔄 What is a Deque Again?

A **Deque** (Double-Ended Queue) allows **insertion and deletion from both ends** — front and rear.

But in **restricted deques**, we limit **either insertion or deletion** to one end only.

---

## 1. 🔐 **Input Restricted Deque**

### 🧠 Definition:
- **Insertions allowed only at one end** (typically the **rear**)
- **Deletions allowed at both ends** (front and rear)

### 📥 Operations:

| Operation        | Allowed? |
|------------------|----------|
| `insertRear(x)`  | ✅ Yes   |
| `insertFront(x)` | ❌ No    |
| `deleteFront()`  | ✅ Yes   |
| `deleteRear()`   | ✅ Yes   |

### 📊 Use Case:
Used when data comes from a single source (one input point), but needs flexible deletion (like managing queues in priority order manually).

### 💡 Visual:

```plaintext
Deque: [B, C, D]

insertRear(E) → [B, C, D, E] ✅
deleteFront() → [C, D, E] ✅
deleteRear() → [C, D] ✅
insertFront(A) → ❌ Not allowed
```

---

## 2. 🔐 **Output Restricted Deque**

### 🧠 Definition:
- **Insertions allowed at both ends**
- **Deletion allowed only at one end** (typically the **front**)

### 📥 Operations:

| Operation        | Allowed? |
|------------------|----------|
| `insertRear(x)`  | ✅ Yes   |
| `insertFront(x)` | ✅ Yes   |
| `deleteFront()`  | ✅ Yes   |
| `deleteRear()`   | ❌ No    |

### 📊 Use Case:
Useful when you want to insert from multiple sources but process output in strict order (FIFO at front).

### 💡 Visual:

```plaintext
Deque: [B, C, D]

insertFront(A) → [A, B, C, D] ✅
insertRear(E) → [A, B, C, D, E] ✅
deleteFront() → [B, C, D, E] ✅
deleteRear() → ❌ Not allowed
```

---

## 🧠 Summary Table

| Type                    | Insertion           | Deletion           | Use Case Example                  |
|-------------------------|---------------------|---------------------|-----------------------------------|
| Input Restricted Deque  | Only rear           | Both ends           | Task management with strict input |
| Output Restricted Deque | Both ends           | Only front          | FIFO processing with flexible input |

---