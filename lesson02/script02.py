"""
Binary Tree
"""

# Classes

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


# Functions

def parse_tuple(data):
    if isinstance(data, tuple) and len(data) == 3:
        node = TreeNode(data[1])
        node.left = parse_tuple(data[0])
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)

    return node

def tree_to_tuple(tree):
    if tree is None:
        return None
    return (tree_to_tuple(tree.left), tree.key, tree_to_tuple(tree.right))

def display_keys(node, space='\t', level=0):
    if node is None:
        print(space*level + '∅')
        return

    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return

    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left, space, level+1)


# Main

if __name__ == '__main__':
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = parse_tuple(tree_tuple)

    display_keys(tree)

    print(tree_to_tuple(tree))
