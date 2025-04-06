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

Here’s a clear and complete comparison between **Array** and **Linked List**:

---

## 🔍 **Difference Between Array and Linked List**

| Feature                     | **Array**                                                                 | **Linked List**                                                            |
|----------------------------|---------------------------------------------------------------------------|----------------------------------------------------------------------------|
| **Memory Allocation**       | Contiguous (allocated at once)                                           | Non-contiguous (allocated node by node)                                   |
| **Size**                    | Fixed (defined at creation, unless dynamic array is used)                | Dynamic (can grow/shrink as needed)                                       |
| **Access Time**             | O(1) (random access using index)                                         | O(n) (need to traverse from head)                                         |
| **Insertion (At Middle)**   | O(n) (shift elements to make space)                                      | O(1) (if pointer to node is known)                                        |
| **Deletion (At Middle)**    | O(n) (shift elements)                                                    | O(1) (if pointer to node is known)                                        |
| **Insertion/Deletion at End**| O(1) (amortized in dynamic arrays)                                      | O(n) (in singly linked list without tail pointer)                         |
| **Insertion/Deletion at Start**| O(n) (shift all elements)                                           | O(1) (just change head pointer)                                           |
| **Wastage of Memory**       | Possible (pre-allocated unused memory in static arrays)                  | Less wastage (allocates only what is needed)                              |
| **Cache Friendliness**      | High (due to contiguous memory)                                          | Low (nodes scattered in memory)                                           |
| **Pointer Overhead**        | None                                                                     | Extra memory for storing pointers (`next`, and `prev` in DLL)             |
| **Traversal Direction**     | Only forward using index                                                 | Forward (SLL), Forward & backward (DLL)                                   |
| **Implementation Simplicity**| Simple                                                                  | Slightly more complex (due to pointers)                                   |
| **Use Case**                | Best for frequent access and small insertions/deletions                 | Best for frequent insertions/deletions                                    |
| **Use Case**                | Memory is allocated from stack                 | Memory is allocated from heap                                    |
| **Use Case**                | it is necessary to specify the number of elements during declaration (i.e during compile time).                 | it is not necessary to specify the number of elements during declaration (i.e memory is allocated during run time.)                                    |
| **Use Case**                | it occupies less memory than a linked list for the same number of elements.             | it occupies more memory.                                    |
| **Use Case**                | Inserting new elements at the front is potentially expensive because existing elements need to be shifted over to make room.                  | Inserting a new element at any position can be carried out easily.                                    |
| **Use Case**                | Deleting an element from an array is not possible                  | Deleting an element is possible                                     |

---

## 📌 **Key Takeaways**
- **Use Arrays** when:
  - You need **fast access** to elements.
  - The size is known ahead of time.
  - Memory should be tightly packed.
- **Use Linked Lists** when:
  - The size changes frequently.
  - You perform a lot of **insertions/deletions**.
  - You don’t need random access.

---