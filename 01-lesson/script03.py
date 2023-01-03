"""
Recursive Binary Search Algorithm
"""

# Function

def binary_search(arr: list, query: int, index=0) -> int:
    """
    It is assumed that the list arr is sorted.
    """
    number_of_elements = len(arr)

    if number_of_elements == 1 and arr != query:
        return -1

    if arr[0] == query:
        return 0

    midpoint = number_of_elements // 2

    if arr[midpoint] == query:
        return index + midpoint
    elif arr[midpoint] < query:
        return binary_search(arr[midpoint:], query, index + midpoint)
    else:
        return binary_search(arr[:midpoint], query, index)

# Main

if __name__ == '__main__':
    sample = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    query = 8

    print(f'\nThe position of the query {query} in the sample is {binary_search(sample, query)}.')
