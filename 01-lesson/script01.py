"""
Linear Search Algorithm
"""

# Function

def linear_search(arr: list, query: int) -> int:
    position = 0

    for value in arr:
        if value == query:
            return position

        position += 1

    return -1


# Main

if __name__ == '__main__':
    sample = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 7

    print(f'The position of the query is {linear_search(sample, query)}.')
