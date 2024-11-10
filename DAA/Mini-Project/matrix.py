import time
import threading

# Standard Matrix Multiplication
def matrix_multiply(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result

# Multithreaded Matrix Multiplication (One Thread Per Row)
def thread_per_row(i, A, B, result):
    for j in range(len(B[0])):
        for k in range(len(B)):
            result[i][j] += A[i][k] * B[k][j]

def multithreaded_row_matrix_multiply(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    threads = []
    for i in range(len(A)):
        thread = threading.Thread(target=thread_per_row, args=(i, A, B, result))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    return result

# Multithreaded Matrix Multiplication (One Thread Per Cell)
def thread_per_cell(i, j, A, B, result):
    for k in range(len(B)):
        result[i][j] += A[i][k] * B[k][j]

def multithreaded_cell_matrix_multiply(A, B):
    result = [[0] * len(B[0]) for _ in range(len(A))]
    threads = []
    for i in range(len(A)):
        for j in range(len(B[0])):
            thread = threading.Thread(target=thread_per_cell, args=(i, j, A, B, result))
            threads.append(thread)
            thread.start()

    for thread in threads:
        thread.join()
    return result

# Function to get matrix input from the user
def get_matrix_input(name):
    rows = int(input(f"Enter the number of rows for matrix {name}: "))
    cols = int(input(f"Enter the number of columns for matrix {name}: "))
    
    print(f"Enter the elements of matrix {name} row by row:")
    matrix = []
    for i in range(rows):
        row = list(map(int, input().split()))
        if len(row) != cols:
            print(f"Error: You must enter exactly {cols} elements.")
            return None
        matrix.append(row)
    
    return matrix

# Function to check if matrix multiplication is possible
def can_multiply(A, B):
    return len(A[0]) == len(B)

def main():

    print("Matrix A:")
    A = get_matrix_input("A")
    
    print("\nMatrix B:")
    B = get_matrix_input("B")

    if A is None or B is None:
        print("Matrix input was invalid.")
        return
    
    if not can_multiply(A, B):
        print("Matrix multiplication not possible. The number of columns in A must equal the number of rows in B.")
        return

    # Standard Matrix Multiplication
    start = time.time()
    result_standard = matrix_multiply(A, B)
    end = time.time()
    print("\nStandard Matrix Multiplication Result:")
    for row in result_standard:
        print(row)
    print("Time Taken:", end - start)

    # Multithreaded - Row
    start = time.time()
    result_thread_row = multithreaded_row_matrix_multiply(A, B)
    end = time.time()
    print("\nMultithreaded (Per Row) Matrix Multiplication Result:")
    for row in result_thread_row:
        print(row)
    print("Time Taken:", end - start)

    # Multithreaded - Cell
    start = time.time()
    result_thread_cell = multithreaded_cell_matrix_multiply(A, B)
    end = time.time()
    print("\nMultithreaded (Per Cell) Matrix Multiplication Result:")
    for row in result_thread_cell:
        print(row)
    print("Time Taken:", end - start)

if __name__ == "__main__":
    main()
