Data link layer
function of data link layer
- Frame 
- Flow control 
- error handling 
- physical address - mac address. (48 bit hexadecimal no)

Error detection and error correction
error - if sender and receiver msg are mis-matched
type of error
single bit
multi bit 
burst bit

Parity check

### **Data Link Layer (DLL)**
The **Data Link Layer** is the second layer of the **OSI (Open Systems Interconnection) model**. It is responsible for **node-to-node communication** and provides reliable data transfer over the physical layer.

### **Functions of the Data Link Layer**
1. **Framing**  
   - The DLL breaks the stream of bits received from the network layer into **frames** (structured packets of data).  
   - It adds headers and trailers to define the beginning and end of each frame.

2. **Flow Control**  
   - Ensures that the sender does not overwhelm the receiver by sending data at a rate higher than the receiver can process.  
   - Common techniques: **Stop-and-Wait Protocol**, **Sliding Window Protocol**.

3. **Error Handling**  
   - Detects and corrects errors that may occur during transmission.  
   - Uses error detection methods like **Parity Check, CRC (Cyclic Redundancy Check), Checksum**.  
   - Some protocols also support **error correction**.

4. **Physical Addressing (MAC Addressing)**  
   - Each device on a network has a **MAC (Media Access Control) address**, a **48-bit hexadecimal number** (e.g., **00:1A:2B:3C:4D:5E**).  
   - The MAC address uniquely identifies devices within a network.

---

## **Error Detection and Error Correction**
Errors occur when the received data differs from the sent data. These errors can be classified into:

### **Types of Errors**
1. **Single Bit Error**  
   - Only **one** bit is altered (0 → 1 or 1 → 0).  
   - Example:  
     - **Sent:** `10101010`  
     - **Received:** `10101000` (only one bit flipped)

2. **Multi-bit Error**  
   - **More than one** bit is altered in a single transmission.  
   - Example:  
     - **Sent:** `10101010`  
     - **Received:** `10000010` (multiple bits flipped)

3. **Burst Error**  
   - A **sequence** of bits (more than one) is altered due to noise or interference.  
   - Example (burst of 4 bits changed):  
     - **Sent:** `101010101011`  
     - **Received:** `101000001011`

---

## **Parity Check (Error Detection)**
Parity checking is a simple method for detecting errors in transmitted data.

### **Types of Parity Check**
1. **Even Parity**  
   - The number of **1s in the data** should be **even** (including the parity bit).  
   - If the count of 1s is odd, an extra `1` is added to make it even.  
   - Example:  
     - **Data:** `1010001` (3 ones → odd)  
     - **Even Parity Bit:** `1`  
     - **Transmitted Data:** `10100011`

2. **Odd Parity**  
   - The number of **1s in the data** should be **odd** (including the parity bit).  
   - If the count of 1s is even, an extra `1` is added to make it odd.  
   - Example:  
     - **Data:** `1010001` (3 ones → odd)  
     - **Odd Parity Bit:** `0`  
     - **Transmitted Data:** `10100010`

### **Parity Check Limitations**
- It **only detects errors**, but **cannot correct them**.  
- If an **even number of bits** change, the error may go undetected.  
- Not suitable for high-noise environments.

Would you like to explore **other error detection methods**, such as **CRC (Cyclic Redundancy Check) or Hamming Code (error correction)?** 🚀

### **Flow Control in Data Communication**
Flow control is a technique used in data communication to **regulate the rate of data transmission** between a sender and a receiver, ensuring that the receiver is not overwhelmed with data it cannot process.

#### **Why is Flow Control Needed?**
- The **sender** may transmit data at a **higher speed** than the **receiver** can process.
- If there is no control, the receiver’s buffer may **overflow**, leading to **data loss**.
- Flow control ensures **smooth and efficient communication** between devices.

---

## **Types of Flow Control**
There are two main types of flow control techniques:

### **1. Stop-and-Wait Flow Control**
- The sender **sends one frame** and **waits for an acknowledgment (ACK)** from the receiver before sending the next frame.
- If no acknowledgment is received (due to error or packet loss), the sender retransmits the frame.

#### **Example**
1. **Sender sends Frame 1.**
2. **Receiver processes Frame 1 and sends an acknowledgment (ACK1).**
3. **Sender receives ACK1 and sends Frame 2.**
4. The process repeats for each frame.

#### **Advantages:**
✔ Simple to implement  
✔ Ensures no data loss  

#### **Disadvantages:**
✖ Slow, as the sender waits for each ACK before sending the next frame  
✖ Inefficient for high-speed networks  

---

### **2. Sliding Window Protocol**
- Allows multiple frames to be sent **before waiting for an acknowledgment**.
- Uses a **window size (N)** to control how many frames can be sent before requiring an acknowledgment.
- Two types of sliding window protocols:
  - **Go-Back-N (GBN)**
  - **Selective Repeat (SR)**

#### **A. Go-Back-N (GBN) Protocol**
- The sender can **send multiple frames** (up to a window size `N`) without waiting for individual ACKs.
- If an error occurs in a frame, **all subsequent frames are retransmitted** from the error frame.

##### **Example (Go-Back-3, N=3)**
1. Sender sends **Frames 1, 2, 3**.
2. Receiver **acknowledges Frame 1 and 2**.
3. Frame 3 gets **corrupted**.
4. Sender **retransmits Frame 3 and all subsequent frames**.

#### **B. Selective Repeat (SR) Protocol**
- The sender **only retransmits the corrupted frames**, not the entire sequence.
- More **efficient** than GBN but requires **more buffer space**.

##### **Example (Selective Repeat, N=3)**
1. Sender sends **Frames 1, 2, 3**.
2. Receiver **ACKs Frame 1 and 2**.
3. Frame 3 is **corrupted**.
4. Sender **retransmits only Frame 3**.

#### **Advantages of Sliding Window Protocol**
✔ **More efficient** than Stop-and-Wait  
✔ **Better throughput** for high-speed networks  

#### **Disadvantages**
✖ Requires **more memory (buffering frames)**  
✖ More **complex to implement**  

---

## **Comparison of Flow Control Techniques**
| Flow Control Method | Efficiency | Error Handling | When to Use |
|---------------------|------------|---------------|--------------|
| **Stop-and-Wait** | Low | Retransmit single frame | Low-speed or reliable links |
| **Go-Back-N** | Moderate | Retransmit all frames after error | High-speed networks, less buffering needed |
| **Selective Repeat** | High | Retransmit only the error frame | High-speed networks, but requires more memory |

