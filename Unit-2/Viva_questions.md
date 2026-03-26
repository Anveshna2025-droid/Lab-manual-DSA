# 📑 Data Structures Lab: Experiment Series (7-13)
**Name:** Anveshna | **Course:** B.Tech CSE Core | **Section:** A  
**Roll No:** 2501010130 | **Submitted to:** Deepak Kaushik Sir

---

## Experiment 7: Arrays 1D (Operations + Shifting Cost)
* **Why index access is O(1)?** Arrays use **Contiguous Memory**. The address of any element is calculated instantly using: $Address = Base + (Index \times Size)$.
* **Why insertion at start is O(n)?** Every existing element must be shifted one position to the right to create a vacancy for the new element at index 0.
* **Static vs. Dynamic Arrays?** Static arrays have a fixed size allocated at compile-time, while dynamic arrays can resize at runtime when they become full.

---

## Experiment 8: Arrays 2D (Matrix Traversal + Ops)
* **Complexity of scanning a matrix?** It is **$O(R \times C)$**. You must visit every cell once using nested loops (one for rows, one for columns).
* **Real-world use of 2D arrays?** Image processing (pixel grids), Google Sheets/Excel, and game boards like Chess or Sudoku.
* **Memory layout (Row-Major)?** 2D data is stored in a 1D memory line by placing the first row completely, then the second row, and so on.

---

## Experiment 9: Dynamic Array Simulation (Resize + Pop)
* **What is Amortized Complexity?** The average cost of an operation over time. While one `append` might be $O(n)$ due to resizing, most are $O(1)$. The average is **Amortized O(1)**.
* **Why doubling helps?** Doubling the capacity ensures that the "expensive" resize operations happen less and less frequently as the array grows.
* **Why pop-end is O(1)?** Removing from the end requires no shifting of other elements; we simply update the size counter.

---

## Experiment 10: Singly Linked List (Core Ops)
* **Why search is O(n)?** Linked Lists are not contiguous. To find a value, you must start at the `head` and follow pointers one by one until you reach the target.
* **Why insert-at-head is O(1)?** You only need to update two pointers: the new node's `next` and the `head` pointer. No shifting is required.
* **Node Structure?** A node consists of two parts: **Data** (the value) and **Next** (the pointer/address to the following node).

---

## Experiment 11: Doubly Linked List (Extended Ops)
* **DLL advantage over SLL?** It allows **bidirectional traversal** (forward and backward) and allows you to delete a node without needing to "search" for its predecessor.
* **Browser history mapping?** Browsers use DLLs to manage history: the `prev` pointer is the **Back** button, and the `next` pointer is the **Forward** button.
* **Deletion ease in DLL?** A node in a DLL knows its own predecessor. To delete it, you simply link its `prev` node to its `next` node directly.

---

## Experiment 12: Stack using SLL + Parentheses Checker
* **Why is Stack ideal here?** Parentheses follow a **LIFO** (Last-In, First-Out) nesting order. The most recently opened bracket must be the first one closed.
* **What fails in "([)]"?** The algorithm pops `(` when it expects to see the match for `]`. Since the top of the stack doesn't match the closing bracket, it returns False.
* **Underflow meaning?** When you attempt to `pop` or `peek` from a stack that contains zero elements.

---

## Experiment 13: Queue using SLL (O(1) operations)
* **Why BFS uses a Queue?** BFS explores level-by-level. A queue ensures that nodes discovered first are visited first (**FIFO**).
* **FIFO meaning?** **First-In, First-Out**. The first element added to the structure is the first one to be removed.
* **Scheduling example?** **CPU Task Scheduling** or **Printer Spooling**, where tasks are processed in the exact order they arrived.