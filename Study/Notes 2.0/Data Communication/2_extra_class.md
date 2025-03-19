Here is a table outlining the five different classes of IPv4 addresses:

| Class | First Octet Decimal Range | First Octet Binary Range | IP Range | Default Subnet Mask | Hosts per Network ID | Number of Networks |
|-------|--------------------------|--------------------------|----------|----------------------|----------------------|--------------------|
| A     | 1 – 126                  | 00000001 – 01111110      | 1.0.0.0 – 126.255.255.255 | 255.0.0.0 ( /8 )  | 16,777,214 | 128 (excluding 0 & 127) |
| B     | 128 – 191                | 10000000 – 10111111      | 128.0.0.0 – 191.255.255.255 | 255.255.0.0 ( /16 ) | 65,534 | 16,384 |
| C     | 192 – 223                | 11000000 – 11011111      | 192.0.0.0 – 223.255.255.255 | 255.255.255.0 ( /24 ) | 254 | 2,097,152 |
| D     | 224 – 239                | 11100000 – 11101111      | 224.0.0.0 – 239.255.255.255 | N/A (Multicast) | N/A | N/A |
| E     | 240 – 255                | 11110000 – 11111111      | 240.0.0.0 – 255.255.255.255 | N/A (Experimental) | N/A | N/A |

### Notes:
- **Class A**: Used for very large networks, assigned to organizations requiring a vast number of IP addresses.
- **Class B**: Used for medium-sized networks, typically assigned to ISPs and large organizations.
- **Class C**: Used for small networks, commonly assigned to businesses and smaller organizations.
- **Class D**: Reserved for **multicast** groups, not used for normal unicast communication.
- **Class E**: Reserved for **experimental** purposes and not used for general networking.

### **What is Subnetting?**
Subnetting is the process of dividing a large network into smaller, more manageable sub-networks (subnets). This is done by borrowing bits from the host portion of an IP address to create additional network addresses.

### **Uses of Subnetting:**
1. **Efficient IP Address Allocation** – Reduces IP address wastage by assigning only the necessary addresses to each subnet.
2. **Improved Network Performance** – Reduces network congestion by limiting broadcast domains.
3. **Enhanced Security** – Isolates network segments to prevent unauthorized access.
4. **Simplified Management** – Makes troubleshooting and administration easier by organizing networks into logical groups.
5. **Optimized Routing** – Reduces the size of routing tables, improving routing efficiency.

---

### **Classful Subnetting**
Classful subnetting refers to the traditional method of subnetting where networks are divided strictly based on their class (A, B, or C), using default subnet masks.

| **Class** | **Default Subnet Mask** | **Subnet Bits Used** | **Total Subnets** | **Hosts per Subnet** |
|-----------|-------------------------|----------------------|------------------|-----------------|
| A ( /8 ) | 255.0.0.0 | 0 | 1 | 16,777,214 |
| B ( /16 ) | 255.255.0.0 | 0 | 1 | 65,534 |
| C ( /24 ) | 255.255.255.0 | 0 | 1 | 254 |

### **Limitations of Classful Subnetting**
- **Wastes IP Addresses** – Networks may receive more IPs than needed.
- **Fixed Network Sizes** – Cannot create flexible subnet sizes to fit different needs.
- **Inefficient Routing** – Large routing tables due to lack of aggregation.

To overcome these limitations, **Classless Inter-Domain Routing (CIDR)** and **VLSM (Variable Length Subnet Masking)** are used in modern networks.

### **Classless Subnetting (CIDR - Classless Inter-Domain Routing)**  
Classless subnetting allows flexible division of IP address space, eliminating the fixed class-based structure (A, B, or C). It uses **Variable Length Subnet Masking (VLSM)** to allocate IP addresses based on actual needs, making better use of available IPs.

| **CIDR Notation** | **Subnet Mask** | **Subnet Bits Used** | **Total Subnets** | **Hosts per Subnet** |
|-------------------|----------------|----------------------|------------------|-----------------|
| /8  | 255.0.0.0 | 0  | 1  | 16,777,214 |
| /16 | 255.255.0.0 | 8  | 256  | 65,534 |
| /24 | 255.255.255.0 | 16 | 65,536  | 254 |
| /26 | 255.255.255.192 | 18 | 262,144 | 62 |
| /30 | 255.255.255.252 | 22 | 4,194,304 | 2 |

### **Advantages of Classless Subnetting**
- **Efficient IP Address Utilization** – Reduces IP wastage by assigning only the needed addresses.
- **Flexible Subnet Sizes (VLSM)** – Different subnets can have different sizes.
- **Optimized Routing (Supernetting)** – Aggregates multiple networks, reducing routing table size.
- **Scalability** – Suitable for large networks, ISPs, and modern enterprises.

### **Example of CIDR Subnetting**
Given **192.168.1.0/24**, instead of using a fixed **/24 subnet**, it can be divided based on needs:
- **IT Department:** /26 → 62 hosts
- **HR Department:** /27 → 30 hosts
- **Admin Department:** /28 → 14 hosts

This flexibility ensures **better utilization of IP addresses** compared to classful subnetting.

Would you like examples on how to calculate subnet masks and IP ranges? 🚀