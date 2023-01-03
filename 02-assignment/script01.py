"""
Hash Table
"""

# Constants

MAX_HASH_TABLE_SIZE = 4098

# Classes

class HashTable:
    def __init__(self):
        pass

    def insert(self, key, value):
        """
        Insert a new key-value pair.
        """
        pass

    def find(self, key):
        """
        Find the value associated with a key.
        """
        pass

    def update(self, key, value):
        """
        Change the value associated with a key.
        """
        pass

    def list_all(self):
        """
        List all the keys.
        """
        pass

    def find(self, key):
        """
        Find the value associated with a key.
        """
        pass

    def update(self, key, value):
        """
        Change the value associated with a key.
        """
        pass

    def list_all(self):
        """
        List all the keys.
        """
        pass


# Functions




# Functions

def get_index(data_list, a_string):
    result = 0

    for a_character in a_string:
        a_number = ord(a_character)
        result += a_number

    list_index = result % MAX_HASH_TABLE_SIZE

    return list_index

# Main

if __name__ == '__main__':
    phone_numbers = {
        'Aakash': '999198237',
        'Hemanth': '999874376',
        'Siddhant': '999419674'
    }

    print(phone_numbers)

    data_list = MAX_HASH_TABLE_SIZE*[None]

    key, value = 'Aakash', '7878787878'

    idx = get_index(data_list, key)
    print(idx)
