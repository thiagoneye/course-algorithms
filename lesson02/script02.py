"""
Binary Tree
"""

# Classes

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def height(self):
        if self is None:
            return 0
        return 1 + max(TreeNode.height(self.left), TreeNode.height(self.right))

    def size(self):
        if self is None:
            return 0
        return 1 + TreeNode.size(self.left) + TreeNode.size(self.right)

    def maximum(self):
        if self is None:
            return 0
        return max(TreeNode.maximum(self.left), self.key, TreeNode.maximum(self.right))

    def minimum(self):
        if self is None:
            return float('inf')
        return min(TreeNode.minimum(self.left), self.key, TreeNode.minimum(self.right))

    def traverse_inorder(self):
        if self is None:
            return []
        return (TreeNode.traverse_inorder(self.left) + [self.key] + TreeNode.traverse_inorder(self.right))

    def traverse_preorder(self):
        if self is None:
            return []
        return ([self.key] + TreeNode.traverse_preorder(self.left) + TreeNode.traverse_preorder(self.right))

    def traverse_postorder(self):
        if self is None:
            return []
        return (TreeNode.traverse_postorder(self.left) + TreeNode.traverse_postorder(self.right) + [self.key])

    def display_keys(self, space='\t', level=0):
        if self is None:
            print(space*level + '∅')
            return

        if self.left is None and self.right is None:
            print(space*level + str(self.key))
            return

        TreeNode.display_keys(self.right, space, level+1)
        print(space*level + str(self.key))
        TreeNode.display_keys(self.left, space, level+1)

    def to_tuple(self):
        if self is None:
            return None

        if self.left is None and self.right is None:
            return self.key

        return (TreeNode.to_tuple(self.left), self.key, TreeNode.to_tuple(self.right))

    def __str__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    def __repr__(self):
        return "BinaryTree <{}>".format(self.to_tuple())

    @staticmethod
    def parse_tuple(data):
        if data is None:
            node = None
        elif isinstance(data, tuple) and len(data) == 3:
            node = TreeNode(data[1])
            node.left = TreeNode.parse_tuple(data[0])
            node.right = TreeNode.parse_tuple(data[2])
        else:
            node = TreeNode(data)

        return node

    def is_bst(tree):
        def check_bst(node, min_key, max_key):
            if node is None:
                return True
            if node.key < min_key or node.key > max_key:
                return False
            return check_bst(node.left, min_key, node.key) and check_bst(node.right, node.key, max_key)

        return check_bst(tree, float('-inf'), float('inf'))


# Main

if __name__ == '__main__':
    tree_tuple = ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))
    tree = TreeNode.parse_tuple(tree_tuple)
    print(tree)
    print(tree.height())
    print(tree.size())
    print(tree.traverse_inorder())
    print(tree.traverse_preorder())
    print(tree.traverse_postorder())
    print(tree.maximum())
    print(tree.minimum())
    print(TreeNode.is_bst(tree))

    print('\n')

    tree_tuple = ((20, 30, 40), 50, (None, 90, 100))
    tree = TreeNode.parse_tuple(tree_tuple)
    print(tree)
    print(tree.height())
    print(tree.size())
    print(tree.traverse_inorder())
    print(tree.traverse_preorder())
    print(tree.traverse_postorder())
    print(tree.maximum())
    print(tree.minimum())
    print(TreeNode.is_bst(tree))
