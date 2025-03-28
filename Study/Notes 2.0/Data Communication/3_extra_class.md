### **Default Subnet Masks for IPv4 Address Classes**  

| **Class** | **First Octet Range** | **Default Subnet Mask** | **CIDR Notation** | **Hosts per Network** |
|-----------|----------------------|-------------------------|-------------------|----------------------|
| **A** | 1 – 126 | 255.0.0.0 | /8  | 16,777,214 |
| **B** | 128 – 191 | 255.255.0.0 | /16 | 65,534 |
| **C** | 192 – 223 | 255.255.255.0 | /24 | 254 |
| **D** | 224 – 239 | **N/A (Multicast)** | **N/A** | **N/A** |
| **E** | 240 – 255 | **N/A (Experimental)** | **N/A** | **N/A** |

### **Explanation:**
- **Class A**: Supports very large networks, with a default subnet mask of **255.0.0.0**.
- **Class B**: Used for medium-sized networks, default subnet mask **255.255.0.0**.
- **Class C**: Used for smaller networks, default subnet mask **255.255.255.0**.
- **Class D**: Reserved for **multicast** networking, does not have a subnet mask.
- **Class E**: Reserved for **experimental purposes**, not used for standard networking.

Would you like a guide on **custom subnetting** beyond the default masks? 🚀