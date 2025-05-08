Here’s a breakdown of the terms **cyclic**, **acyclic**, **multi**, and **planner (likely meant to be planar)** in the context of **graph theory**:

---

### 🔁 **Cyclic Graph**

* A **cyclic graph** contains **at least one cycle**, which is a path that starts and ends at the same vertex with no repeated edges or vertices (except the start/end).
* Example: A triangle (3 vertices connected in a loop).

---

### 🚫 **Acyclic Graph**

* An **acyclic graph** is a graph with **no cycles**.
* If directed: it's called a **Directed Acyclic Graph (DAG)**—used in scheduling, compilers, etc.
* If undirected: typically a **tree** (connected and acyclic).

---

### 🔁🔁 **Multigraph**

* A **multigraph** allows **multiple edges (parallel edges)** between the same pair of vertices.
* May or may not allow loops (edges that connect a vertex to itself).
* Example: Two cities connected by more than one road.

---

### 🗺️ **Planar Graph** *(not "planner")*

* A **planar graph** can be **drawn on a plane without any edges crossing**.
* Example: A triangle, square, or a tree is planar.
* **K₅ (complete graph on 5 vertices)** and **K₃,₃ (complete bipartite graph)** are **not planar**—proved by **Kuratowski's theorem**.

---

### Summary Table:

| Type       | Description                                 | Cycles Allowed? | Edge Restrictions        |
| ---------- | ------------------------------------------- | --------------- | ------------------------ |
| Cyclic     | Has at least one cycle                      | Yes             | Simple or multiple edges |
| Acyclic    | No cycles                                   | No              | Usually simple           |
| Multigraph | Multiple edges between vertex pairs allowed | Yes/No          | Allows parallel edges    |
| Planar     | Drawable without edge crossings             | Yes/No          | Depends on drawing       |

Would you like a diagram to visually show these graph types?
