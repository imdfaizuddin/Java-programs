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

## **Accessing, Inserting, and Deleting Elements in an Array**  

### **1. Accessing Elements in an Array**  
**Accessing an element** in an array is done using the index. Since arrays use **contiguous memory**, retrieving an element takes **constant time** \(O(1)\).  

#### **Time Complexity**  
- **Best case:** O(1)  
- **Worst case:** O(1)  
- **Average case:** O(1)  
- **Space Complexity:** O(1)  

#### **Example in C++**
```cpp
#include <iostream>
using namespace std;

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int index = 2;

    cout << "Element at index " << index << " is " << arr[index] << endl; // Output: 30
    return 0;
}
```

#### **Example in Java**
```java
public class ArrayAccess {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int index = 2;

        System.out.println("Element at index " + index + " is " + arr[index]); // Output: 30
    }
}
```

---

### **2. Inserting an Element in an Array**  
Insertion in an array can happen in different positions:  
1. **At the end (O(1))** – If space is available, inserting at the end takes constant time.  
2. **At a specific index (O(n))** – Requires shifting elements.  
3. **At the beginning (O(n))** – Requires shifting all elements.  

#### **Time Complexity**  
| **Insertion Type**  | **Best Case** | **Worst Case** | **Average Case** |
|-------------------|-------------|-------------|-------------|
| Insert at End    | O(1)        | O(1)        | O(1)        |
| Insert at Start  | O(1)        | O(n)        | O(n)        |
| Insert at Middle | O(1)        | O(n)        | O(n)        |

#### **Space Complexity**: O(1)  

#### **Example in C++ (Insertion at a Specific Index)**
```cpp
#include <iostream>
using namespace std;

void insertElement(int arr[], int &size, int index, int value) {
    for (int i = size; i > index; i--) {
        arr[i] = arr[i - 1];
    }
    arr[index] = value;
    size++;  
}

int main() {
    int arr[6] = {10, 20, 30, 40, 50}; // Array with extra space
    int size = 5;
    
    insertElement(arr, size, 2, 25); // Insert 25 at index 2

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
```
**Output:**  
```
10 20 25 30 40 50
```

#### **Example in Java**
```java
import java.util.Arrays;

public class ArrayInsertion {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50, 0}; // Extra space for insertion
        int size = 5;
        int index = 2, value = 25;

        // Shift elements to the right
        for (int i = size; i > index; i--) {
            arr[i] = arr[i - 1];
        }
        arr[index] = value;
        size++;

        System.out.println(Arrays.toString(Arrays.copyOf(arr, size)));
    }
}
```

---

### **3. Deleting an Element from an Array**  
To delete an element, we need to **shift elements** to maintain order.

1. **Deleting from the end (O(1))** – Simply reduce the size.  
2. **Deleting from a specific index (O(n))** – Requires shifting elements.  
3. **Deleting from the beginning (O(n))** – Requires shifting all elements.  

#### **Time Complexity**  
| **Deletion Type**  | **Best Case** | **Worst Case** | **Average Case** |
|------------------|-------------|-------------|-------------|
| Delete at End   | O(1)        | O(1)        | O(1)        |
| Delete at Start | O(1)        | O(n)        | O(n)        |
| Delete at Middle| O(1)        | O(n)        | O(n)        |

#### **Space Complexity**: O(1)  

#### **Example in C++ (Deleting an Element at a Specific Index)**
```cpp
#include <iostream>
using namespace std;

void deleteElement(int arr[], int &size, int index) {
    for (int i = index; i < size - 1; i++) {
        arr[i] = arr[i + 1];
    }
    size--; // Reduce size
}

int main() {
    int arr[5] = {10, 20, 30, 40, 50};
    int size = 5;
    
    deleteElement(arr, size, 2); // Delete element at index 2

    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    return 0;
}
```
**Output:**  
```
10 20 40 50
```

#### **Example in Java**
```java
import java.util.Arrays;

public class ArrayDeletion {
    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int size = 5;
        int index = 2;

        // Shift elements to left
        for (int i = index; i < size - 1; i++) {
            arr[i] = arr[i + 1];
        }
        size--;

        System.out.println(Arrays.toString(Arrays.copyOf(arr, size)));
    }
}
```

---

### **Summary of Operations, Time, and Space Complexity**
| **Operation** | **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** |
|--------------|-------------|-------------|-------------|----------------|
| **Access**   | O(1)        | O(1)        | O(1)        | O(1)           |
| **Insertion at End** | O(1) | O(1) | O(1) | O(1) |
| **Insertion at Middle** | O(1) | O(n) | O(n) | O(1) |
| **Insertion at Start** | O(1) | O(n) | O(n) | O(1) |
| **Deletion at End** | O(1) | O(1) | O(1) | O(1) |
| **Deletion at Middle** | O(1) | O(n) | O(n) | O(1) |
| **Deletion at Start** | O(1) | O(n) | O(n) | O(1) |

---

### **Conclusion**  
- **Accessing an element** in an array is **always O(1)**.  
- **Insertion and deletion at the end** are **O(1)** (if there's space).  
- **Insertion and deletion in the middle or beginning** require **O(n) time** due to shifting elements.  
- Arrays are **efficient for read operations but less flexible for frequent insertions and deletions**.  

## **Searching in an Array**  
Searching in an array means finding whether a particular element exists and, if so, returning its index. There are two primary searching techniques:  

1. **Linear Search** – Works for both sorted and unsorted arrays.  
2. **Binary Search** – Works only for sorted arrays and is more efficient.  

---

## **1. Linear Search (O(n))**  
In **linear search**, we check each element one by one until we find the target element or reach the end of the array.  

### **Time Complexity**
| **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** |
|--------------|--------------|--------------|----------------|
| O(1) (First element) | O(n) (Last element or not found) | O(n) | O(1) |

### **C++ Implementation**
```cpp
#include <iostream>
using namespace std;

int linearSearch(int arr[], int size, int key) {
    for (int i = 0; i < size; i++) {
        if (arr[i] == key)
            return i; // Return index if found
    }
    return -1; // Return -1 if not found
}

int main() {
    int arr[] = {10, 20, 30, 40, 50};
    int key = 30;

    int index = linearSearch(arr, 5, key);
    if (index != -1)
        cout << "Element found at index " << index << endl;
    else
        cout << "Element not found" << endl;

    return 0;
}
```

### **Java Implementation**
```java
public class LinearSearch {
    public static int linearSearch(int[] arr, int key) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == key)
                return i; // Return index if found
        }
        return -1; // Return -1 if not found
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50};
        int key = 30;

        int index = linearSearch(arr, key);
        if (index != -1)
            System.out.println("Element found at index " + index);
        else
            System.out.println("Element not found");
    }
}
```

---

## **2. Binary Search (O(log n))**  
**Binary search** works by repeatedly dividing the sorted array into two halves and checking the middle element.  

### **Steps for Binary Search**
1. Find the middle element.  
2. If the middle element is the target, return its index.  
3. If the target is smaller, search the left half.  
4. If the target is larger, search the right half.  
5. Repeat until the element is found or the search space is empty.  

### **Time Complexity**
| **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** |
|--------------|--------------|--------------|----------------|
| O(1) (Middle element is target) | O(log n) | O(log n) | O(1) (Iterative), O(log n) (Recursive) |

### **C++ Implementation (Iterative)**
```cpp
#include <iostream>
using namespace std;

int binarySearch(int arr[], int size, int key) {
    int left = 0, right = size - 1;
    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (arr[mid] == key)
            return mid;
        else if (arr[mid] < key)
            left = mid + 1;
        else
            right = mid - 1;
    }
    return -1; // Element not found
}

int main() {
    int arr[] = {10, 20, 30, 40, 50}; // Sorted array
    int key = 30;

    int index = binarySearch(arr, 5, key);
    if (index != -1)
        cout << "Element found at index " << index << endl;
    else
        cout << "Element not found" << endl;

    return 0;
}
```

### **Java Implementation (Iterative)**
```java
public class BinarySearch {
    public static int binarySearch(int[] arr, int key) {
        int left = 0, right = arr.length - 1;
        while (left <= right) {
            int mid = left + (right - left) / 2;
            if (arr[mid] == key)
                return mid;
            else if (arr[mid] < key)
                left = mid + 1;
            else
                right = mid - 1;
        }
        return -1; // Element not found
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50}; // Sorted array
        int key = 30;

        int index = binarySearch(arr, key);
        if (index != -1)
            System.out.println("Element found at index " + index);
        else
            System.out.println("Element not found");
    }
}
```

---

## **Comparison of Searching Algorithms**
| **Algorithm** | **Best Case** | **Worst Case** | **Average Case** | **Space Complexity** | **When to Use?** |
|--------------|-------------|-------------|-------------|----------------|----------------|
| **Linear Search** | O(1) | O(n) | O(n) | O(1) | Works for both sorted & unsorted arrays |
| **Binary Search** | O(1) | O(log n) | O(log n) | O(1) | Only works for sorted arrays |

---

## **Conclusion**
- **Linear Search**:  
  ✅ Works on both sorted and unsorted arrays.  
  ❌ Inefficient for large datasets (**O(n)** time complexity).  
- **Binary Search**:  
  ✅ Efficient for large datasets (**O(log n)** time complexity).  
  ❌ Requires the array to be sorted.  

---