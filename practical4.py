# Function to print board
def print_board(board, n):

    for i in range(n):

        for j in range(n):

            if board[i] == j:
                print("Q", end=" ")
            else:
                print(".", end=" ")

        print()

    print()


# Check if position is safe
def is_safe(board, row, col):

    for i in range(row):

        # Same column
        if board[i] == col:
            return False

        # Diagonal check
        if abs(board[i] - col) == abs(i - row):
            return False

    return True


# Backtracking function
def solve_n_queens(board, row, n):

    global solution_count

    # If all queens placed
    if row == n:

        solution_count += 1

        print(f"Solution {solution_count}:\n")

        print_board(board, n)

        return

    for col in range(n):

        if is_safe(board, row, col):

            board[row] = col

            # Recursive call
            solve_n_queens(board, row + 1, n)

            # Backtrack
            board[row] = -1


# Main
n = int(input("Enter number of queens: "))

board = [-1] * n

solution_count = 0

solve_n_queens(board, 0, n)

if solution_count == 0:
    print("No Solution Exists")

else:
    print("Total Solutions:", solution_count)