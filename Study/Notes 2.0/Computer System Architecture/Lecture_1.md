### **Understanding 1’s and 2’s Complement with Explanation**  

#### **1’s Complement**  
1’s complement is a way of representing the negative of a number in binary by flipping all the bits (0 → 1, 1 → 0).  

🔹 **Why is it used?**  
It was an early method to represent negative numbers in binary. However, it has a drawback: there are two representations of zero (`0000` and `1111` in 4-bit representation). This leads to computational issues, so 2’s complement is preferred.  

✅ **Example (4-bit representation of +5 and -5 using 1’s complement)**  
- **+5** → `0101`  
- **-5** (1’s complement) → `1010` (flipping all bits)  

🛑 **Problem:** There are two zeroes (`0000` and `1111`), making arithmetic operations difficult.

---

#### **2’s Complement**  
2’s complement solves the issue of two zeroes by ensuring only one representation of zero. It is found by taking the 1’s complement and adding 1.  

🔹 **Why is it used?**  
- It simplifies binary subtraction (addition and subtraction use the same hardware).  
- It avoids having two zero representations.  

✅ **Example (4-bit representation of +5 and -5 using 2’s complement)**  
1. **+5** → `0101`  
2. **Find 1’s complement of 5** → `1010`  
3. **Add 1** →  
   ```
   1010
 + 0001
  ------
   1011
   ```
4. **-5 (2’s complement)** → `1011`

---

### **How to Identify Positive and Negative Numbers in 2’s Complement?**  
- If **MSB (Most Significant Bit) is 0**, the number is **positive**.  
- If **MSB is 1**, the number is **negative** (stored in 2’s complement form).  

✅ **Examples:**  
- `0110` (MSB = 0) → **Positive (6)**  
- `1011` (MSB = 1) → **Negative (-5 using 2’s complement)**  

---

### **Converting 2’s Complement Back to Decimal**
To find the decimal value of a **negative** binary number in 2’s complement:  
1. Check if MSB is **1** (indicating a negative number).  
2. Take the **2’s complement** (flip bits and add 1).  
3. Convert to decimal and add a negative sign.  

✅ **Example (Finding Decimal of `1011` in 4-bit system)**  
1. `1011` (MSB = 1, so it’s negative).  
2. Take **1’s complement**: `0100`  
3. Add 1: `0101` → **5**  
4. Add negative sign → **-5**  

---

### **Summary**
| Binary Representation | 1’s Complement | 2’s Complement |
|----------------------|---------------|---------------|
| `0101` (+5)        | `1010`         | `1011` (-5)  |
| `0110` (+6)        | `1001`         | `1010` (-6)  |

- **1’s complement:** Flip all bits.  
- **2’s complement:** Flip all bits and add 1.  
- **Negative numbers in 2’s complement always start with 1**.  

Let me know if you need more clarification! 🚀