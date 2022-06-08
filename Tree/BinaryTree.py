# implimenting pre-order traversal

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree(object):
    def __init__(self, root):
        self.root = Node(root)

    def search(self, find_val):
        """Return True if the value
        is in the tree, return
        False otherwise."""
        res = self.preorder_search(self.root, find_val)
        if res:
            return res
        return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        return self.preorder_print(self.root)

    def preorder_search(self, root, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        if root is None:
            return

        if root.value == find_val:
            return True

        left_val = self.preorder_search(root.left, find_val)
        if left_val == True:
            return True
        right_val = self.preorder_search(root.right, find_val)
        if right_val == True:
            return True

    def preorder_print(self, root):
        """Helper method - use this to create a 
        recursive print solution."""
        if root is None:
            #print('0')
            return

        """if root.value:
            print("1", root.value)
"""
        #print(f'in{root.value}', end='-')
        print(root.value, end='-')

        self.preorder_print(root.left)

        self.preorder_print(root.right)

        return ""


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
#print(tree.search(3))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
print(tree.print_tree())