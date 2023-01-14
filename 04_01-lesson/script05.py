"""
Knapsack Problem (Dynamic Programming)
"""

# Functions

def max_profit_dc(weights: list, profits: list, capacity: int) -> int:
    n = len(weights)
    table = [(capacity+1)*[0] for _ in range(n+1)]

    for i in range(n):
        for j in range(1, capacity+1):
            if weights[i] > j:
                table[i+1][j] = table[i][j]
            else:
                table[i+1][j] = max(table[i][j], profits[i] + table[i][j - weights[i]])

    return table[-1][-1]

# Main

if __name__ == '__main__':
    weights = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
    profits = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
    capacity = 165

    output = max_profit_dc(weights, profits, capacity)

    print(f'The output is {output}.')
