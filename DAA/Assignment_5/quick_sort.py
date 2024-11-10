import random

comparison_count = 0

def deterministic_partition(arr, low, high):
    global comparison_count
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        comparison_count += 1  # Count each comparison
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    return deterministic_partition(arr, low, high)

def deterministic_quick_sort(arr, low, high, recursion_depth=0):
    global max_recursion_depth
    if low < high:
        pi = deterministic_partition(arr, low, high)
        deterministic_quick_sort(arr, low, pi - 1, recursion_depth + 1)
        deterministic_quick_sort(arr, pi + 1, high, recursion_depth + 1)
        max_recursion_depth = max(max_recursion_depth, recursion_depth)

def randomized_quick_sort(arr, low, high, recursion_depth=0):
    global max_recursion_depth
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quick_sort(arr, low, pi - 1, recursion_depth + 1)
        randomized_quick_sort(arr, pi + 1, high, recursion_depth + 1)
        max_recursion_depth = max(max_recursion_depth, recursion_depth)

def print_array(arr):
    print("[", end="")
    print(", ".join(map(str, arr)), end="")
    print("]")

def print_time_complexity(algorithm):
    if algorithm == "Deterministic":
        print("\nTime Complexity for Deterministic Quicksort:")
        print("Best case: O(n log n) - Happens when partitions are balanced")
        print("Worst case: O(n^2) - Happens when the smallest or largest element is always the pivot")
        print("Average case: O(n log n)")

    elif algorithm == "Randomized":
        print("\nTime Complexity for Randomized Quicksort:")
        print("Best case: O(n log n)")
        print("Worst case: O(n^2) - But this is very rare due to randomization")
        print("Average case: O(n log n) - Randomization helps avoid worst case")

if __name__ == "__main__":
    array_size = int(input("Enter the size of the array: "))
    arr = []
    for i in range(array_size):
        element = int(input(f"Enter the {i+1} element of the array: "))
        arr.append(element)

    print("Original array is:", end=" ")
    print_array(arr)

    while True:
        print('*' * 10, "MENU", '*' * 10)
        print("Choose the sorting method")
        print("1. Deterministic Quicksort")
        print("2. Randomized Quicksort")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            arr_deterministic = arr.copy()  
            comparison_count = 0  
            max_recursion_depth = 0  
            deterministic_quick_sort(arr_deterministic, 0, len(arr_deterministic) - 1)
            print("\nSorted array using Deterministic Quicksort:", end=" ")
            print_array(arr_deterministic)
            print(f"Number of comparisons: {comparison_count}")
            print(f"Maximum recursion depth: {max_recursion_depth}")
            print_time_complexity("Deterministic")  

        elif choice == 2:
            arr_randomized = arr.copy()  
            comparison_count = 0  
            max_recursion_depth = 0  
            randomized_quick_sort(arr_randomized, 0, len(arr_randomized) - 1)
            print("\nSorted array using Randomized Quicksort:", end=" ")
            print_array(arr_randomized)
            print(f"Number of comparisons: {comparison_count}")
            print(f"Maximum recursion depth: {max_recursion_depth}")
            print_time_complexity("Randomized")  

        elif choice == 3:
            print("Exiting successfully!!")
            break

        else:
            print("Invalid choice!")
