Here’s a breakdown of **sorting**, including definitions of **stable/unstable sorts**, common **types of sorting algorithms**, and their **time and space complexities**:

---

### 📘 **What is Sorting?**
Sorting is the process of arranging elements (typically in a list or array) in a particular order — usually **ascending** or **descending**.

---

### 🧩 **Stable vs Unstable Sort**

| Term | Meaning | Example |
|------|---------|---------|
| **Stable Sort** | Maintains the **relative order** of equal elements | If two items with the same key appear in the input in a certain order, they will appear in the same order in the output |
| **Unstable Sort** | May **change the order** of equal elements | Equal elements can appear in a different order than in the original input |

✅ **Example**:  
Input: `[ (3, 'A'), (3, 'B'), (2, 'C') ]`  
Stable sort by first number → `[ (2, 'C'), (3, 'A'), (3, 'B') ]`  
Unstable sort might give → `[ (2, 'C'), (3, 'B'), (3, 'A') ]`

---

### 📊 **Types of Sorting Algorithms**

| Algorithm        | Best Time     | Avg Time     | Worst Time    | Space     | Stable | Notes |
|------------------|---------------|--------------|---------------|-----------|--------|-------|
| **Bubble Sort**  | O(n)          | O(n²)        | O(n²)         | O(1)      | ✅     | Simple, inefficient |
| **Selection Sort**| O(n²)        | O(n²)        | O(n²)         | O(1)      | ❌     | Not stable by default |
| **Insertion Sort**| O(n)         | O(n²)        | O(n²)         | O(1)      | ✅     | Good for nearly sorted data |
| **Merge Sort**   | O(n log n)    | O(n log n)   | O(n log n)    | O(n)      | ✅     | Divide and conquer |
| **Quick Sort**   | O(n log n)    | O(n log n)   | O(n²)         | O(log n)  | ❌     | Fast, but not stable |
| **Heap Sort**    | O(n log n)    | O(n log n)   | O(n log n)    | O(1)      | ❌     | Based on heap data structure |
| **Counting Sort**| O(n + k)      | O(n + k)     | O(n + k)      | O(k)      | ✅     | Only for integers/small range |
| **Radix Sort**   | O(nk)         | O(nk)        | O(nk)         | O(n + k)  | ✅     | Works for integers/digits |
| **Bucket Sort**  | O(n + k)      | O(n + k)     | O(n²)         | O(n + k)  | ✅     | Good for uniform distribution |
| **Tim Sort**     | O(n)          | O(n log n)   | O(n log n)    | O(n)      | ✅     | Hybrid of merge + insertion, used in Python/Java |

> ✅ Stable sorts are preferred when you want to preserve the original order of equal elements (e.g., when sorting by multiple keys).

---

### 💡 Quick Summary Table

| Algorithm      | Time (Avg) | Space | Stable |
|----------------|------------|-------|--------|
| Bubble Sort    | O(n²)      | O(1)  | ✅     |
| Selection Sort | O(n²)      | O(1)  | ❌     |
| Insertion Sort | O(n²)      | O(1)  | ✅     |
| Merge Sort     | O(n log n) | O(n)  | ✅     |
| Quick Sort     | O(n log n) | O(log n) | ❌ |
| Heap Sort      | O(n log n) | O(1)  | ❌     |
| Counting Sort  | O(n + k)   | O(k)  | ✅     |
| Radix Sort     | O(nk)      | O(n + k) | ✅ |
| Bucket Sort    | O(n + k)   | O(n + k) | ✅ |
| Tim Sort       | O(n log n) | O(n)  | ✅     |

---

If you want, I can give visual examples, code for each sorting algorithm, or real-world use cases. Want to dive deeper into any one?