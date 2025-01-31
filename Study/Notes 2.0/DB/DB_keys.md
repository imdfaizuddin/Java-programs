In the context of relational databases, keys are used to uniquely identify records in a table. Here’s a breakdown of the terms you mentioned:

### 1. **Primary Key**
- **Definition**: A primary key is a column (or a set of columns) in a table that uniquely identifies each row in that table.
- **Properties**:
  - **Uniqueness**: No two rows can have the same primary key value.
  - **Non-null**: A primary key column cannot have NULL values.
  - **Stability**: The value of a primary key should not change over time.
- **Example**: In a `Students` table, the `StudentID` column could be the primary key because each student has a unique ID.

### 2. **Candidate Key**
- **Definition**: A candidate key is a column (or a set of columns) that can uniquely identify any row in the table. A table can have multiple candidate keys.
- **Properties**:
  - **Uniqueness**: Each candidate key must uniquely identify each row.
  - **Minimality**: A candidate key should be minimal, meaning no subset of the key should be able to uniquely identify the row.
- **Example**: In a `Students` table, both `StudentID` and `Email` could be candidate keys if both are unique for each student.

### 3. **Super Key**
- **Definition**: A super key is a set of one or more columns that can uniquely identify a row in a table. Unlike a candidate key, a super key does not need to be minimal.
- **Properties**:
  - **Uniqueness**: A super key must uniquely identify each row.
  - **Non-minimality**: A super key can have additional columns that are not necessary for uniqueness.
- **Example**: In a `Students` table, a combination of `StudentID` and `Email` could be a super key, even though `StudentID` alone is sufficient to uniquely identify each student.

### Summary of Differences:
- **Primary Key**: The chosen candidate key to uniquely identify rows in a table. There can be only one primary key per table.
- **Candidate Key**: Any column or set of columns that can uniquely identify rows. There can be multiple candidate keys in a table.
- **Super Key**: Any set of columns that can uniquely identify rows, including candidate keys and other combinations that may not be minimal.

### Explained with examples:

Sure! Let’s use a **Students** table to explain **Primary Key**, **Candidate Key**, and **Super Key** with examples.

---

### Table: **Students**

| **StudentID** | **Email**          | **Name**   | **Phone**       |
|---------------|--------------------|------------|-----------------|
| 101           | john@example.com   | John Doe   | 123-456-7890    |
| 102           | jane@example.com   | Jane Smith | 987-654-3210    |
| 103           | alice@example.com  | Alice Brown| 555-555-5555    |

---

### 1. **Primary Key**
- **Definition**: The chosen column (or set of columns) that uniquely identifies each row in the table.
- **Example**: In the `Students` table, the `StudentID` column is the **primary key** because:
  - It is unique for each student.
  - It cannot be NULL.
  - It is stable (does not change over time).

---

### 2. **Candidate Key**
- **Definition**: A column (or set of columns) that can uniquely identify each row in the table. A table can have multiple candidate keys, but only one is chosen as the primary key.
- **Example**: In the `Students` table:
  - `StudentID` is a candidate key because it is unique for each student.
  - `Email` is also a candidate key because it is unique for each student.
  - Both `StudentID` and `Email` are candidate keys because they satisfy the properties of uniqueness and minimality.

---

### 3. **Super Key**
- **Definition**: A set of one or more columns that can uniquely identify each row in the table. A super key may include extra columns that are not necessary for uniqueness.
- **Example**: In the `Students` table:
  - `{StudentID}` is a super key (and also a candidate key).
  - `{Email}` is a super key (and also a candidate key).
  - `{StudentID, Email}` is a super key, but it is not a candidate key because it is not minimal (either `StudentID` or `Email` alone is sufficient for uniqueness).
  - `{StudentID, Name}` is a super key, but it is not a candidate key because `StudentID` alone is sufficient for uniqueness.

---

### Summary of Examples:

| **Key Type**     | **Example in Students Table**                                                                 |
|-------------------|---------------------------------------------------------------------------------------------|
| **Primary Key**   | `StudentID` (chosen as the primary key).                                                    |
| **Candidate Key** | `StudentID` and `Email` (both are unique and minimal).                                      |
| **Super Key**     | `{StudentID}`, `{Email}`, `{StudentID, Email}`, `{StudentID, Name}`, `{Email, Phone}`, etc. |

---

### Visual Representation:

| **StudentID** | **Email**          | **Name**   | **Phone**       |
|---------------|--------------------|------------|-----------------|
| **101**       | john@example.com   | John Doe   | 123-456-7890    |
| **102**       | jane@example.com   | Jane Smith | 987-654-3210    |
| **103**       | alice@example.com  | Alice Brown| 555-555-5555    |

- **Primary Key**: `StudentID` (e.g., `101`, `102`, `103`).
- **Candidate Key**: `StudentID` or `Email` (e.g., `101` or `john@example.com`).
- **Super Key**: Any combination that includes `StudentID` or `Email`, such as `{StudentID, Email}` or `{Email, Phone}`.

---

This should help clarify the differences between **Primary Key**, **Candidate Key**, and **Super Key** with examples! Let me know if you have further questions. 😊