"""
TreeMap
"""

# Imports

from script01 import *
from script03 import *

# Classes

class TreeMap:
    def __init__(self):
        self.root = None

    def __setitem__(self, key, value):
        node = find(self.root, key)
        if not node:
            self.root = insert(self.root, key, value)
            self.root = balance_bst(self.root)
        else:
            update(self.root, key, value)

    def __getitem__(self):
        node = find(self.root, key)
        return node.value if node else None

    def __iter__(self):
        return (x for x in list_all(self.root))

    def __len__(self):
        return tree_size(self.root)

    def display(self):
        return display_keys(self.root)


# Main

if __name__ == '__main__':
    # Create Users
    aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
    biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
    hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
    jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
    siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
    sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
    vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

    users = [('aakash', aakash), ('biraj', biraj), ('hemanth', hemanth),
        ('jadhesh', jadhesh), ('siddhant', siddhant), ('sonaksh', sonaksh),
        ('vishal', vishal)]

    # Create TreeMap
    treemap = TreeMap()

    # Insert Users
    treemap['aakash'] = aakash
    treemap['biraj'] = biraj
    treemap['hemanth'] = hemanth
    treemap['jadhesh'] = jadhesh
    treemap['siddhant'] = siddhant
    treemap['sonaksh'] = sonaksh
    treemap['vishal'] = vishal

    treemap.display()
