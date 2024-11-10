def knapsack_01(values, weights, capacity):
    n = len(values)
    dp = [[0 for _ in range(capacity + 1)] for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                # If the current item's weight is less than or equal to the current capacity,
                # choose the maximum of either including or excluding the current item
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                # If the current item's weight is more than the current capacity, exclude it
                dp[i][w] = dp[i - 1][w]

    return dp[n][capacity]  

def main():
    n = int(input("Enter the number of items: "))

    values = []
    weights = []
    
    for i in range(n):
        value = int(input(f"Enter the value of item {i + 1}: "))
        weight = int(input(f"Enter the weight of item {i + 1}: "))
        values.append(value)
        weights.append(weight)

    capacity = int(input("Enter the capacity of the knapsack: "))

    max_value = knapsack_01(values, weights, capacity)
    print(f"Maximum value in the knapsack: {max_value}")

if __name__ == "__main__":
    main()
