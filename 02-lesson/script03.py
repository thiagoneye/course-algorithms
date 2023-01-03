"""
Binary Search Tree
"""

# Classes

class BSTNode:
    def __init__(self, key, value=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


# Funtions

def display_keys(tree, space='\t', level=0):
    if tree is None:
        print(space*level + '∅')
        return

    if tree.left is None and tree.right is None:
        print(space*level + str(tree.key))
        return

    display_keys(tree.right, space, level+1)
    print(space*level + str(tree.key))
    display_keys(tree.left, space, level+1)

def insert(tree, key, value):
    if tree is None:
        tree = BSTNode(key, value)
    elif key < tree.key:
        tree.left = insert(tree.left, key, value)
        tree.left.parent = tree
    elif key > tree.key:
        tree.right = insert(tree.right, key, value)
        tree.right.parent = tree

    return tree

def find(tree, key):
    if tree is None:
        return None
    elif key == tree.key:
        return tree
    elif key < tree.key:
        return find(tree.left, key)
    else:
        return find(tree.right, key)

def update(tree, key, value):
    target = find(tree, key)
    if target is not None:
        target.value = value

def list_all(tree):
    if tree is None:
        return []

    return list_all(tree.left) + [(tree.key, tree.value)] + list_all(tree.right)

def is_balanced(tree):
    if tree is None:
        return True, 0

    balanced_l, height_l = is_balanced(tree.left)
    balanced_r, height_r = is_balanced(tree.right)

    balanced = balanced_l and balanced_r and abs(height_l - height_r) <= 1
    height = 1 + max(height_l, height_r)

    return balanced, height

def maked_balanced_bst(data, parent=None):
    if not data:
        return None

    mid = len(data) // 2
    key, value = data[mid]

    root = BSTNode(key, value)
    root.parent = parent
    root.left = maked_balanced_bst(data[:mid], root)
    root.right = maked_balanced_bst(data[mid+1:], root)

    return root

def balance_bst(tree):
    return maked_balanced_bst(list_all(tree))

# Main

if __name__ == '__main__':
    # Imports
    from script01 import User

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

    # Create Tree
    tree = BSTNode(jadhesh.username, jadhesh)
    tree = insert(tree, siddhant.username, siddhant) #
    tree = insert(tree, vishal.username, vishal) #
    tree = insert(tree, biraj.username, biraj)
    tree = insert(tree, sonaksh.username, sonaksh)
    tree = insert(tree, aakash.username, aakash)
    tree = insert(tree, hemanth.username, hemanth)
    display_keys(tree)

    # Find Key
    # print(find(tree, 'siddhant').value)

    # New Tree
    tree = maked_balanced_bst(users)
    display_keys(tree)
