# 📑 Data Structures & Algorithms: Lab Viva Questions Guide
**Name:** Anveshna | **Roll No:** 2501010130

---

### **Stacks & Data Structures**
**1. What is an ADT?**
An **Abstract Data Type (ADT)** is a logical description of a data structure. It defines **what** operations can be performed (like `push` or `pop`) without specifying **how** they are implemented in the code.

**2. Why push/pop can be 180°C O(1)?**
In a stack, all operations occur at the **top**. Since you are only adding or removing the most recent element and never shifting or searching through the rest of the data, the time taken is constant (**O(1)**) regardless of the stack size.

**3. One real-world use of stack?**
The **Undo/Redo** functionality in applications. Each action is pushed onto a stack, and "Undo" simply pops the last action performed.

---

### **Complexity Analysis**
**1. Big-O vs Big-Theta difference?**
* **Big-O (O):** Represents the **upper bound** (worst-case). It says the algorithm will not take more than this much time.
* **Big-Theta (Θ):** Represents a **tight bound**. It describes the exact growth rate, meaning the algorithm's performance is precisely bounded between the same upper and lower limits.

**2. What does worst-case represent?**
It represents the maximum number of steps an algorithm will take for a given input size **n**. It is used as a performance guarantee for systems.

**3. Why complexity matters in real systems?**
Complexity determines **scalability**. An inefficient algorithm might work for 10 users but crash a server when 1 million users join. Optimizing complexity saves time, server costs, and energy.

---

### **Recursion & Memory**
**1. What is recursion depth?**
It is the total number of active function calls currently residing on the system stack at any point during the execution of a recursive function.

**2. Why recursion uses stack memory?**
Each recursive call creates a **stack frame** to store local variables, parameters, and the return address. This allows the computer to "remember" where it was and resume correctly once a base case is hit.


**3. When iteration is better than recursion?**
Iteration is better when **memory is a constraint** or the depth of logic is very high. Iteration uses a fixed amount of memory, whereas deep recursion can lead to a "Stack Overflow" error.

---

### **Fibonacci & Memoization**
**1. Why naive Fibonacci is slow?**
It is slow because of **redundant calculations**. It solves the same subproblems (like calculating $fib(3)$) multiple times across different branches of the recursion tree, leading to **O(2ⁿ)** time.


**2. Memoization relates to DP?**
Yes. Memoization is a **top-down** approach to **Dynamic Programming**. It solves the main problem by breaking it into subproblems and storing the results to avoid doing the same work twice.

**3. Space impact of memoization?**
It reduces time complexity to **O(n)** but increases space complexity to **O(n)** because you must allocate extra memory (like an array or dictionary) to store the cached results.

---

### **Tower of Hanoi**
**1. Why moves are 2ⁿ - 1?**
To move **n** disks, you must move the **n-1** disks twice (once to the auxiliary peg and once to the destination) plus move the largest disk once. This follows the recurrence $$T(n) = 2T(n-1) + 1$$, which solves to **2ⁿ - 1**.

**2. What is recursion tree idea?**
It is a visual representation of the recursive calls. Each node is a call, and the tree branches out at every step. For Hanoi, it forms a full binary tree, illustrating how the work doubles with each new disk.


**3. Practical risk of exponential algorithms?**
The risk is **time explosion**. Adding just a few more items to the input can turn a task that takes seconds into one that takes years to finish.

---

### **Binary Search**
**1. Why sorted data is required?**
Binary search works by comparing the target to the middle element to decide which half of the data to discard. If the data isn't sorted, there is no way to know if the target lies in the left or right half.

**2. Best/avg/worst case?**
* **Best:** **O(1)** (Target is found exactly at the first midpoint).
* **Avg/Worst:** **O(log n)** (The search space is halved repeatedly until only one element remains).


**3. Divide & Conquer meaning?**
It is a strategy that **Divides** a large problem into smaller subproblems of the same type, **Conquers** them (usually recursively), and then **Combines** the results to solve the original problem.