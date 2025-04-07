Here's a solid breakdown of **Algorithm Analysis**, **Time-Space Tradeoff**, and **Asymptotic Notations**, perfect for your DSA notes:

---

## 🧠 Algorithm Analysis

**Goal:**  
To evaluate the **efficiency** of an algorithm, mainly in terms of:
- **Time Complexity** – how fast it runs
- **Space Complexity** – how much memory it uses

**Why it matters:**  
We want to choose the best algorithm for a given problem, especially when inputs grow large.

---

## ⚖️ Time-Space Tradeoff

This is a balancing act between **time** and **space** used by an algorithm.

> **Definition:**  
An algorithm can be made to run faster by using more memory, or it can use less memory but may take more time.

### 📌 Example:

| Problem | Time Optimized | Space Optimized |
|--------|----------------|-----------------|
| Searching | Use a hash table (O(1) lookup, more space) | Use linear search (O(n) time, minimal space) |
| Fibonacci | Use DP with memoization (faster, more space) | Use recursion (slower, less space) |

> ✅ **Tradeoff Use Case:**  
Choose based on constraints. If memory is limited, prioritize space. If speed is critical, optimize time.

---

## 📈 Asymptotic Notations

Used to describe the **growth rate** of an algorithm as input size `n` approaches infinity.

### 1. **Big-O Notation (O)** – **Worst-case**

- Upper bound on time/space
- Tells us the *maximum* time the algorithm can take.

📌 Example:
```plaintext
Linear search: O(n)
Binary search: O(log n)
Bubble sort: O(n^2)
```

### 2. **Omega (Ω)** – **Best-case**

- Lower bound
- Tells us the *minimum* time it might take.

📌 Example:
```plaintext
Linear search best case (item at start): Ω(1)
```

### 3. **Theta (Θ)** – **Average-case / Tight bound**

- Exact bound if best and worst case are the same.
- Describes the actual runtime if behavior is consistent.

📌 Example:
```plaintext
Merge Sort: Θ(n log n)
```

---

## 🧮 Common Time Complexities (in increasing order):

| Complexity | Name |
|-----------|------|
| O(1) | Constant |
| O(log n) | Logarithmic |
| O(n) | Linear |
| O(n log n) | Linearithmic |
| O(n²) | Quadratic |
| O(2ⁿ) | Exponential |
| O(n!) | Factorial |

---
