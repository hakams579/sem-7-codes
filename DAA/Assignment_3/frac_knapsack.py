class Item:
    def __init__(self, value, weight):
        self.value = value
        self.weight = weight
        self.ratio = value / weight  # Value-to-weight ratio

def fractional_knapsack(capacity, items):
    # Sort items by their value-to-weight ratio in descending order
    items.sort(key=lambda x: x.ratio, reverse=True)

    total_value = 0
    for item in items:
        if capacity == 0:
            break
        
        # Take the minimum of the remaining capacity and the current item's weight
        take_weight = min(capacity, item.weight)
        total_value += take_weight * item.ratio
        capacity -= take_weight

    return total_value

def main():
    n = int(input("Enter the number of items: "))

    items = []
    for _ in range(n):
        value = float(input("Enter the value of item: "))
        weight = float(input("Enter the weight of item: "))
        items.append(Item(value, weight))

    capacity = float(input("Enter the capacity of the knapsack: "))

    max_value = fractional_knapsack(capacity, items)
    print(f"Maximum value in the knapsack: {max_value:.2f}")

if __name__ == "__main__":
    main()