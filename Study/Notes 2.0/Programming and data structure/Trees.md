## 🌳 What is a Tree?

A **Tree** is a non-linear hierarchical data structure made up of **nodes**.  
- It starts with a **root node**.
- Each node can have **zero or more children**.
- Unlike graphs, trees do **not contain cycles**.

Think of it like an **upside-down family tree** or a **folder structure** in your computer.

---

## 🔑 Key Terms

| Term        | Meaning                                                                 |
|-------------|-------------------------------------------------------------------------|
| **Node**    | Basic unit of a tree that stores data                                    |
| **Root**    | Top node of the tree                                                     |
| **Child**   | A node directly connected to another node when moving away from the root |
| **Parent**  | A node with children                                                     |
| **Leaf**    | A node with no children                                                  |
| **Edge**    | A connection between one node and another                                |
| **Subtree** | A tree formed by a node and its descendants                              |
| **Depth**   | Number of edges from root to the node                                    |
| **Height**  | Number of edges from node to the deepest leaf                            |

---

## 🌲 Tree Example (Simple)

```
        A        <- Root
       / \
      B   C
     / \   \
    D   E   F   <- Leaf nodes
```

---

## 👨‍💻 Tree in Code (Basic Node Structure in Python)

```python
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child_node):
        self.children.append(child_node)
```

---

## 🧠 Types of Trees

| Tree Type           | Description |
|---------------------|-------------|
| **Binary Tree**     | Each node has at most 2 children (left and right) |
| **Binary Search Tree (BST)** | A binary tree where left child < parent < right child |
| **Balanced Tree**   | Height difference between left and right subtree is minimal |
| **AVL Tree**        | A self-balancing binary search tree |
| **B-Trees**         | Used in databases and file systems |
| **Trie (Prefix Tree)** | Used for searching words or strings efficiently |

---

## ⏱️ Time Complexity (for Binary Search Tree)

| Operation     | Average Case | Worst Case (unbalanced) |
|---------------|--------------|--------------------------|
| Search        | O(log n)     | O(n)                     |
| Insertion     | O(log n)     | O(n)                     |
| Deletion      | O(log n)     | O(n)                     |

---

Perfect! Let's go over these terms with **simple definitions**, **diagrams**, and **examples**, so it's super clear.

---

## 🌳 1. **Sibling Node**
- Nodes that **share the same parent**.
- Think of them like brothers/sisters in a family tree.

**Example:**
```
       A
     /   \
    B     C
   / \   / \
  D   E F   G
```
- B and C are **siblings** (same parent A).
- D and E are **siblings** (same parent B).
- F and G are **siblings** (same parent C).

---

## 🧱 2. **Level**
- **Level** of a node = number of edges from the **root to the node**.
- Root node is at **level 0**.

**Example:**
```
Level 0:        A
Level 1:      /   \
             B     C
Level 2:     / \   / \
           D   E F   G
```

| Node | Level |
|------|-------|
| A    | 0     |
| B, C | 1     |
| D-G  | 2     |

---

## 🔗 3. **Edge**
- An **edge** is the **connection between two nodes**.
- If a tree has `n` nodes, it has exactly **n - 1 edges**.

**Example:**
```
A
|
B
```
- One edge connects A and B.

---

## 🏔️ 4. **Height**
- Height of a node = **longest path (in edges) from that node to a leaf**.
- Height of the **tree** = height of the **root**.

**Example:**
```
        A
       / \
      B   C
     /
    D
```

- Height of D = 0 (it’s a leaf).
- Height of B = 1 (B → D).
- Height of A = 2 (A → B → D).

---

## 📏 5. **Depth**
- Depth of a node = **number of edges from the root to that node**.
- Root has **depth 0**.

**Same Example:**
```
        A        -> Depth 0
       / \
      B   C      -> Depth 1
     /
    D            -> Depth 2
```

---

## ✅ Summary Table

| Term     | Meaning                                            |
|----------|----------------------------------------------------|
| Sibling  | Nodes with the same parent                         |
| Level    | Number of edges from the root (starting from 0)    |
| Edge     | Link between two nodes                             |
| Height   | Max edges from node to a leaf                      |
| Depth    | Edges from root to that node                       |

---
Great! Let’s dive into the **types of trees** in data structures. Each type has its own use case and structure. I’ll explain the most important ones with examples so you can remember them easily.

---

## 🌳 **1. General Tree**
- A tree where **any node can have any number of children**.
- No specific rule on the number of children.
  
**Example:**
```
         A
       / | \
      B  C  D
         |
         E
```

---

## 🌲 **2. Binary Tree**
- Each node has **at most 2 children**: usually called **left** and **right**.

**Example:**
```
       A
      / \
     B   C
```

---

## 🔍 **3. Binary Search Tree (BST)**
- A **binary tree** with a special property:
  - **Left child < Parent < Right child**
- Used in searching and sorting.

**Example:**
```
       10
      /  \
     5    20
```

---

## ⚖️ **4. Balanced Tree**
- A tree where the **height difference** between left and right subtrees of any node is **at most 1**.
- Helps keep operations efficient.

---

## 🔄 **5. AVL Tree** (Adelson-Velsky and Landis)
- A **self-balancing BST**.
- Balances itself after insertions and deletions.

---

## 🌉 **6. Red-Black Tree**
- Another self-balancing BST.
- Follows color rules (nodes are either red or black).
- Used in many libraries (like TreeMap in Java, `map` in C++ STL).

---

## 📁 **7. B-Tree**
- A **self-balancing search tree** designed for **disk storage**.
- Used in databases and file systems.
- Each node can have **multiple keys and children**.

---

## 🔠 **8. Trie (Prefix Tree)**
- Specialized tree used to **store strings**, especially useful for **autocomplete** and **spell checking**.
- Each level represents a character.

**Example (storing "cat", "cap"):**
```
        (root)
         |
         c
         |
         a
       /   \
      t     p
```

---

## 🌐 **9. N-ary Tree**
- A tree where nodes can have **at most N children**.
- Generalized form of binary tree (Binary Tree = N-ary with N = 2).

---

## 🎭 Summary Table

| Tree Type        | Description                                    | Max Children |
|------------------|------------------------------------------------|--------------|
| General Tree     | No restriction                                 | Any          |
| Binary Tree      | Max 2 children per node                        | 2            |
| BST              | Left < Root < Right                            | 2            |
| AVL Tree         | Self-balancing BST                             | 2            |
| Red-Black Tree   | BST with color properties for balance          | 2            |
| B-Tree           | Balanced tree used in databases                | Many         |
| Trie             | Stores strings character by character          | 26 (for a-z) |
| N-ary Tree       | At most N children                             | N            |

---

Great question! These are **special types of binary trees**: **Full**, **Perfect**, and **Complete**.  
They look similar at first, but there are **key differences**.

Let’s break them down with **definitions**, **diagrams**, and **differences**. 👇

---

## ✅ 1. **Full Binary Tree**
- Every node has **0 or 2 children** — never just 1 child.
- Leaf nodes have 0 children, internal nodes have exactly 2.

**Example:**
```
       A
      / \
     B   C
    / \
   D   E
```

✔ A Full Binary Tree  
❌ Not full if a node has only one child.

---

## ✅ 2. **Perfect Binary Tree**
- A Full Binary Tree with **all leaf nodes at the same level**.
- Every internal node has **exactly 2 children**, and the tree is **completely filled**.

**Example (Height = 2):**
```
       A
      / \
     B   C
    / \ / \
   D  E F  G
```

✔ Full + All levels filled  
✔ Height = 2, Total nodes = 2³ - 1 = 7

---

## ✅ 3. **Complete Binary Tree**
- All levels are completely filled **except possibly the last**,  
- The last level has **all nodes as far left as possible**.

**Example:**
```
       A
      / \
     B   C
    / \  /
   D  E F
```

✔ Not perfect (last level not full)  
✔ But all nodes are as left as possible → ✅ Complete

---

## 🧠 Summary Table

| Type      | Every node has 0 or 2 children? | All levels full? | Last level filled left to right? |
|-----------|----------------------------------|------------------|------------------------------|
| Full      | ✅ Yes                          | ❌ Not required   | ❌ Not required              |
| Perfect   | ✅ Yes                          | ✅ Yes           | ✅ Yes                       |
| Complete  | ❌ Not always                   | ✅ Except last    | ✅ Yes                       |

---

## 📌 Quick Check:
- **Perfect** ⊂ **Complete**
- **Perfect** is the strictest.
- **Complete** is most flexible (used in heaps).

---
