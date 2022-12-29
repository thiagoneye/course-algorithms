"""
Linear Search Algorithm
"""

# Function

def locate_card(cards: list, query: int) -> int:
    position = 0

    for card in cards:
        if card == query:
            return position

        position += 1

    return -1

# Main

if __name__ == '__main__':
    cards = [13, 11, 10, 7, 4, 3, 1, 0]
    query = 7

    print(f'The position of card is {locate_card(cards, query)}.')
