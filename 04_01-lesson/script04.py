"""
Knapsack Problem (Recursive)
"""

# Functions

def max_profit_recursive(weights: list, profits: list, capacity: int, idx=0) -> int:
    if idx == len(weights):
        return 0

    if weights[idx] > capacity:
        return max_profit_recursive(weights, profits, capacity, idx+1)
    else:
        option1 = max_profit_recursive(weights, profits, capacity, idx+1)
        option2 = profits[idx] + max_profit_recursive(weights, profits, capacity-weights[idx], idx+1)
        return max(option1, option2)

# Main

if __name__ == '__main__':
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    capacity = 165

    output = max_profit_recursive(weights, profits, capacity)

    print(f'The output is {output}.')
