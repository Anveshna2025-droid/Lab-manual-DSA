# Name = Anveshna
# Course = B.Tech CSE Core 
# Section = A
# Roll no. = 2501010130
# Experiment - 8: Arrays 2D (Matrix Traversal + Ops)
# Submitted to = Deepak Kaushik Sir
# <=========================================>

# Aim - Practice 2D arrays for real-world tabular data and understand traversal complexity.

# Input / Output expectation
# Input: matrix (rows and columns). 
# Output: computed sums + search result + transpose preview.

# <=====================CODE STARTS==========================>

class MatrixOps:
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols
        self.matrix = []

    def create_matrix(self):
        """Initializes the matrix with user-provided values."""
        print(f"\nFilling a {self.rows}x{self.cols} matrix:")
        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                while True:
                    try:
                        val = int(input(f"Enter element at [{i}][{j}]: "))
                        row.append(val)
                        break
                    except ValueError:
                        print("Invalid input. Please enter an integer.")
            self.matrix.append(row)

    def display(self, mat=None):
        """Displays the matrix in a clean tabular format."""
        target = mat if mat else self.matrix
        if not target:
            print("Matrix is empty.")
            return
        for row in target:
            print("\t" + "\t".join(map(str, row)))

    def compute_sums(self):
        """Calculates and displays row-wise and column-wise sums."""
        print("\n[Row-wise Sums]")
        for i in range(self.rows):
            r_sum = sum(self.matrix[i])
            print(f"Row {i} Sum: {r_sum}")

        print("\n[Column-wise Sums]")
        for j in range(self.cols):
            c_sum = 0
            for i in range(self.rows):
                c_sum += self.matrix[i][j]
            print(f"Column {j} Sum: {c_sum}")

    def search(self, target):
        """Searches for a value and returns its coordinates."""
        for i in range(self.rows):
            for j in range(self.cols):
                if self.matrix[i][j] == target:
                    return f"SUCCESS: Value {target} found at position ({i}, {j})"
        return f"FAILED: Value {target} not found in the matrix."

    def get_transpose(self):
        """Returns the transposed version of the matrix."""
        # Row-column swap logic
        transposed = [[self.matrix[j][i] for j in range(self.rows)] for i in range(self.cols)]
        return transposed

def main():
    print("=== Welcome Anveshna! Starting Experiment 8 ===")
    try:
        r = int(input("Enter number of rows: "))
        c = int(input("Enter number of columns: "))
        
        m_obj = MatrixOps(r, c)
        m_obj.create_matrix()

        while True:
            print("\n" + "-"*35)
            print("      2D ARRAY OPERATIONS MENU      ")
            print("-"*35)
            print("1. Display Original Matrix")
            print("2. Compute Row & Column Sums")
            print("3. Search for a specific Value")
            print("4. Preview Transpose Matrix")
            print("0. Exit Program")

            choice = input("\nSelect an option: ").strip()

            if choice == "1":
                print("\nCurrent Matrix State:")
                m_obj.display()

            elif choice == "2":
                m_obj.compute_sums()

            elif choice == "3":
                try:
                    target = int(input("Enter value to search: "))
                    print(m_obj.search(target))
                except ValueError:
                    print("Invalid input. Please enter an integer.")

            elif choice == "4":
                print("\nTransposed Matrix Preview:")
                t_mat = m_obj.get_transpose()
                m_obj.display(t_mat)
                print(f"(New dimensions: {m_obj.cols}x{m_obj.rows})")

            elif choice == "0":
                print("\nExperiment 8 complete. Closing...")
                break
            else:
                print("Invalid selection. Please try again.")

    except ValueError:
        print("Initial dimensions must be integers. Restarting...")
        main()

if __name__ == "__main__":
    main()

# <=====================CODE ENDS============================>