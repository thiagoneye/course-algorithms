"""
Hash Table
"""

# Constants

MAX_HASH_TABLE_SIZE = 4098

# Classes

class BasicHashTable:
    def __init__(self, max_size=MAX_HASH_TABLE_SIZE):
        self.data_list = max_size*[None]

    def insert(self, key, value):
        """
        Insert a new key-value pair.
        """
        idx = BasicHashTable.get_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def find(self, key):
        """
        Find the value associated with a key.
        """
        idx = BasicHashTable.get_index(self.data_list, key)
        key_value = self.data_list[idx]

        if key_value is None:
            return None
        else:
            key, value = key_value
            return value

    def update(self, key, value):
        """
        Change the value associated with a key.
        """
        idx = BasicHashTable.get_index(self.data_list, key)
        self.data_list[idx] = (key, value)

    def list_all(self):
        """
        List all the keys.
        """
        list_of_keys = list()

        for key_value in self.data_list:
            if key_value is not None:
                key, value = key_value
                list_of_keys.append(key)

        return list_of_keys

    @staticmethod
    def get_index(data_list, a_string):
        result = sum([ord(a_character) for a_character in a_string])
        return result % len(data_list)


# Main

if __name__ == '__main__':
    # QUESTION 1: Create a Python list of size MAX_HASH_TABLE_SIZE, with all the
    # values set to None.
    data_list = MAX_HASH_TABLE_SIZE*[None]
    print(len(data_list) == 4098)
    print(data_list[99] == None)

    # QUESTION 2: Complete the get_index function below which implements the
    # hashing algorithm described above.
    print(BasicHashTable.get_index(data_list, '') == 0)
    print(BasicHashTable.get_index(data_list, 'Aakash') == 585)
    print(BasicHashTable.get_index(data_list, 'Don O Leary') == 941)

    # QUESTION 3: Complete the hash table implementation below by following the
    # instructions in the comments.
    basic_table = BasicHashTable(max_size=1024)
    print(len(basic_table.data_list) == 1024)

    basic_table.insert('Aakash', '9999999999')
    basic_table.insert('Hemanth', '8888888888')
    print(basic_table.find('Hemanth') == '8888888888')

    basic_table.update('Aakash', '7777777777')
    print(basic_table.find('Aakash') == '7777777777')

    print(basic_table.list_all() == ['Aakash', 'Hemanth'])
