## **Linked Lists: Explanation, Types, and Time Complexity**  

### **What is a Linked List?**  
A **Linked List** is a linear data structure where elements (nodes) are stored in memory **non-contiguously**/randomly. Each node contains:  
1. **Data** – The actual value.  
2. **Pointer** – A reference to the next node in the sequence.  

Unlike arrays, linked lists **do not require contiguous memory allocation**, making them efficient for insertions and deletions.

---

## **Types of Linked Lists**  

### **1. Singly Linked List (SLL)**  
- Each node contains **data** and a **next pointer** pointing to the next node.  
- The last node points to **NULL**, indicating the end.  

#### **Operations & Time Complexity**
| **Operation**  | **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** |
|---------------|-------------|-------------|-------------|----------------|
| Access (Search) | O(1) | O(n) | O(n) | O(n) |
| Insert at Head | O(1) | O(1) | O(1) | O(1) |
| Insert at Tail | O(1) (if tail pointer exists) | O(n) | O(n) | O(1) |
| Insert at Middle | O(1) | O(n) | O(n) | O(1) |
| Delete from Head | O(1) | O(1) | O(1) | O(1) |
| Delete from Tail | O(1) (if tail pointer exists) | O(n) | O(n) | O(1) |
| Delete from Middle | O(1) | O(n) | O(n) | O(1) |

---

### **2. Doubly Linked List (DLL)**  
- Each node has **two pointers**:  
  - **next** (points to the next node)  
  - **prev** (points to the previous node)  
- Allows **bidirectional traversal**.  

#### **Operations & Time Complexity**
| **Operation**  | **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** |
|---------------|-------------|-------------|-------------|----------------|
| Access (Search) | O(1) | O(n) | O(n) | O(n) |
| Insert at Head | O(1) | O(1) | O(1) | O(1) |
| Insert at Tail | O(1) | O(1) | O(1) | O(1) |
| Insert at Middle | O(1) | O(n) | O(n) | O(1) |
| Delete from Head | O(1) | O(1) | O(1) | O(1) |
| Delete from Tail | O(1) | O(1) | O(1) | O(1) |
| Delete from Middle | O(1) | O(n) | O(n) | O(1) |

> **DLL vs. SLL:** DLL allows **backward traversal** and **faster deletion**, but requires **extra space (O(n))** due to the `prev` pointer.

---

### **3. Circular Linked List (CLL)**  
- **Singly Circular Linked List**: Last node points to the first node instead of `NULL`.  
- **Doubly Circular Linked List**: Both **next** and **prev** pointers form a loop.  
- No `NULL`, so **traversing requires a stopping condition**.  

#### **Operations & Time Complexity** (Same as SLL/DLL but looping is handled differently)
| **Operation**  | **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** |
|---------------|-------------|-------------|-------------|----------------|
| Access (Search) | O(1) | O(n) | O(n) | O(n) |
| Insert at Head | O(1) | O(1) | O(1) | O(1) |
| Insert at Tail | O(1) (if tail pointer exists) | O(n) | O(n) | O(1) |
| Insert at Middle | O(1) | O(n) | O(n) | O(1) |
| Delete from Head | O(1) | O(1) | O(1) | O(1) |
| Delete from Tail | O(1) (if tail pointer exists) | O(n) | O(n) | O(1) |
| Delete from Middle | O(1) | O(n) | O(n) | O(1) |

---

## **Comparison of Linked Lists**
| Feature | **Singly Linked List** | **Doubly Linked List** | **Circular Linked List** |
|---------|----------------------|----------------------|----------------------|
| **Memory Usage** | Less (1 pointer per node) | More (2 pointers per node) | Same as SLL/DLL |
| **Insertion at Head** | O(1) | O(1) | O(1) |
| **Insertion at Tail** | O(n) (without tail pointer) | O(1) | O(1) |
| **Deletion at Head** | O(1) | O(1) | O(1) |
| **Deletion at Tail** | O(n) (without tail pointer) | O(1) | O(1) |
| **Bidirectional Traversal** | ❌ No | ✅ Yes | ✅ Yes (DLL Type) |
| **Loop Handling** | Not required | Not required | Required |

---

## **When to Use Which Linked List?**
- **Singly Linked List (SLL)** → If memory efficiency is a priority.  
- **Doubly Linked List (DLL)** → If **bidirectional traversal** is required.  
- **Circular Linked List (CLL)** → When a **continuous looped structure** is needed (e.g., round-robin scheduling).  

---