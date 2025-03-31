### **What is a Data Structure?**  
A **data structure** is a way of organizing, storing, and managing data efficiently so that it can be accessed and modified easily. It provides a systematic way to handle large amounts of data for various applications such as databases, operating systems, and software development.

### **Types of Data Structures**  
Data structures are mainly classified into two types:  

#### **1. Linear Data Structures**  
In **linear data structures**, elements are arranged sequentially, and each element is connected to its previous and next element. Examples include:  

- **Array** – A collection of elements stored at contiguous memory locations.  
- **Linked List** – A sequence of nodes where each node contains data and a pointer to the next node.  
- **Stack** – A Last-In-First-Out (LIFO) data structure where elements are added and removed from the same end.  
- **Queue** – A First-In-First-Out (FIFO) data structure where elements are added at one end (rear) and removed from the other end (front).  
- **Deque (Double-Ended Queue)** – A generalized form of queue where insertion and deletion can be performed from both ends.  

#### **2. Non-Linear Data Structures**  
In **non-linear data structures**, elements are not arranged in a sequence but are connected in a hierarchical or networked manner. Examples include:  

- **Tree** – A hierarchical data structure consisting of nodes, where each node has a value and child nodes (e.g., Binary Tree, Binary Search Tree, AVL Tree, etc.).  
- **Graph** – A set of nodes (vertices) connected by edges, used to represent networks like social media connections, maps, etc.  
- **Hash Table** – A structure that maps keys to values using a hash function, allowing fast data retrieval.

### **Array: Everything You Need to Know**  

#### **What is an Array?**  
An **array** is a **linear data structure** that stores elements of the **same data type** in **contiguous memory locations**. It allows easy access to elements using an index.  

#### **Key Features of an Array**  
- **Fixed size**: The size of the array is defined at the time of declaration and cannot be changed dynamically in static arrays.  
- **Indexed access**: Elements can be accessed directly using an index.  
- **Homogeneous elements**: All elements must be of the same data type.  
- **Efficient retrieval**: Access time for any element is **O(1)** (constant time).  Memory-efficient because they store elements in contiguous memory locations, which allows for fast access **O(1)**.

---

## **Types of Arrays**  

### **1. One-Dimensional Array (1D Array)**  
A simple array where elements are stored in a single row.  

📌 **Declaration & Initialization in C/C++**  
```cpp
int arr[5] = {10, 20, 30, 40, 50};
```

📌 **Accessing Elements**  
```cpp
cout << arr[2];  // Output: 30
```

### **2. Multi-Dimensional Array (2D, 3D, etc.)**  
A collection of arrays where elements are arranged in **rows and columns**.  

📌 **2D Array Example in C/C++**  
```cpp
int matrix[2][3] = { {1, 2, 3}, {4, 5, 6} };
cout << matrix[1][2];  // Output: 6
```

📌 **3D Array Example**  
```cpp
int cube[2][2][2] = { {{1,2}, {3,4}}, {{5,6}, {7,8}} };
cout << cube[1][0][1];  // Output: 6
```

---

## **Operations on Arrays**  

### **1. Traversal (Accessing Elements) – O(n)**  
Iterating over each element in the array.  
```cpp
for (int i = 0; i < 5; i++) {
    cout << arr[i] << " ";
}
```

### **2. Insertion – O(n) (Worst Case)**  
Since an array has a fixed size, inserting an element requires shifting elements (except at the end).  
```cpp
// Insert element 25 at index 2
arr[2] = 25;
```

### **3. Deletion – O(n) (Worst Case)**  
Deleting an element requires shifting elements to maintain order.  

### **4. Searching**  
- **Linear Search – O(n)**: Checks each element one by one.  
- **Binary Search – O(log n)**: Only works on sorted arrays; divides the array in half to search.  

```cpp
// Binary Search Implementation
int binarySearch(int arr[], int size, int key) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key) return mid;
        else if (arr[mid] < key) left = mid + 1;
        else right = mid - 1;
    }
    return -1;
}
```

### **5. Sorting**  
Sorting arranges elements in increasing or decreasing order. Common sorting algorithms include:  
- **Bubble Sort – O(n²)**  
- **Selection Sort – O(n²)**  
- **Insertion Sort – O(n²)**  
- **Merge Sort – O(n log n)**  
- **Quick Sort – O(n log n) average case**  

---

## **Advantages & Disadvantages of Arrays**  

✅ **Advantages**  
✔️ Fast access time (O(1) for indexed access).  
✔️ Simplicity in implementation.  
✔️ Efficient memory usage (no extra pointers like linked lists).  

❌ **Disadvantages**  
❌ Fixed size (cannot grow dynamically in static arrays).  
❌ Costly insertions and deletions (O(n) in worst case).  
❌ Wastage of memory if array size is larger than needed.  

---

## **Dynamic Arrays**  
To overcome the fixed size issue of static arrays, **dynamic arrays** like **vector (C++)** or **ArrayList (Java)** are used.  

📌 **C++ Vector Example**  
```cpp
#include <vector>
vector<int> v = {1, 2, 3};
v.push_back(4);  // Adds element at the end
```

📌 **Java ArrayList Example**  
```java
import java.util.ArrayList;
ArrayList<Integer> list = new ArrayList<>();
list.add(10);
```

---

### **Real-Life Applications of Arrays**  
✔️ Image processing (storing pixel values).  
✔️ Database management systems.  
✔️ Scheduling and task management.  
✔️ Used in implementing **stacks, queues, heaps** etc.  

---