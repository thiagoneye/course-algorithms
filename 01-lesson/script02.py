"""
Binary Search Algorithm (While Function)
"""

# Function

def binary_search(arr: list, query: int) -> int:
    """
    It is assumed that the list arr is sorted.
    """
    number_of_elements = len(arr)

    inferior_limit = 0
    upper_limit = number_of_elements - 1

    while inferior_limit <= upper_limit:
        midpoint = (inferior_limit + upper_limit) // 2

        if arr[midpoint] < query:
            inferior_limit = midpoint + 1
        elif arr[midpoint] > query:
            upper_limit = midpoint - 1
        else:
            return midpoint

    return -1


# Main

if __name__ == '__main__':
    sample = [1, 1, 2, 3, 4, 4, 5, 6, 7, 8, 8, 9, 10]
    query = 7

    print(f'The position of the query is {binary_search(sample, query)}.')
