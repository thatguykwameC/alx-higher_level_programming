#!/usr/bin/python3
"""
This script implements a backtracking solution to the N-Queens problem.
It finds and prints the coordinates of N queens on an NxN chessboard,
ensuring that they are in non-attacking positions.
"""

from sys import argv

if __name__ == "__main__":
    # Initialize the answer list
    a = []

    # Validate command-line arguments
    if len(argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    if not argv[1].isdigit():
        print("N must be a number")
        exit(1)

    n = int(argv[1])
    if n < 4:
        print("N must be at least 4")
        exit(1)

    # Initialize the answer list
    for i in range(n):
        a.append([i, None])

    def already_exists(y):
        """Check if a queen already exists in the same column."""
        for x in range(n):
            if y == a[x][1]:
                return True
        return False

    def reject(x, y):
        """Checks if current position violates the non-attacking condition."""
        if already_exists(y):
            return False
        i = 0
        while i < x:
            if abs(a[i][1] - y) == abs(i - x):
                return False
            i += 1
        return True

    def clear_a(x):
        """Clear the answers from the point of failure onward."""
        for i in range(x, n):
            a[i][1] = None

    def nqueens(x):
        """Recursive backtracking function to find the solution."""
        for y in range(n):
            clear_a(x)
            if reject(x, y):
                a[x][1] = y
                if x == n - 1:  # Accept the solution
                    print(a)
                else:
                    nqueens(x + 1)  # Move on to the next column

    # Start the recursive process with x = 0
    nqueens(0)
