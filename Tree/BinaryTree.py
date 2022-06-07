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
        """if self.root.value == find_val:
            return True

        print(self.root.left.value)
        if self.root.left:
            search(root = self.root.left)
        return False"""
        #print('response: ', self.preorder_search(self.root, find_val))
        #return self.preorder_search(self.root, find_val)
        res = self.preorder_search(self.root, find_val)
        if res:
            return res
        return False
        #return False

    def print_tree(self):
        """Print out all tree nodes
        as they are visited in
        a pre-order traversal."""
        #return self.preorder_print(self.root)

    def preorder_search(self, root, find_val):
        """Helper method - use this to create a 
        recursive search solution."""
        #print('root is: ', root)
        if root is None:
            return

        #print(root.value, root.value == find_val, find_val)
        #print(root.value)

        """if root.value == find_val:
            print('stop running')
            return True
            # => it returns but it still running to calcul the right side or the children if there are some

        print('recursive')
"""
        if root.value == find_val:
            return True

        left_val = self.preorder_search(root.left, find_val)
        if left_val == True:
            return True
        right_val = self.preorder_search(root.right, find_val)
        if right_val == True:
            return True

        
        """print(start.value, find_val, start.value == find_val)
        if start.value == find_val:
            return True

        #print(self.root.left.value)
        if start.left:
            #print(start.left.value, find_val)
            if start.value == find_val: #start.left.value
                return True
            self.preorder_search(start.left, find_val)
        if start.right:
            #print(start.right.value, find_val)
            if start.value == find_val: #start.right.value
                return True
            self.preorder_search(start.right, find_val)"""
        
        #return False

    def preorder_print(self, start):
        """Helper method - use this to create a 
        recursive print solution."""
        if start.value:
            print(start.value)
        
        #print(self.root.left.value)
        if start.left:
            #print(start.left.value, find_val)
            print(start.left.value)
            self.preorder_print(start.left)
            return
        if start.right:
            #print(start.right.value, find_val)
            print(start.right.value)
            self.preorder_print(start.right)
            return
        #print(traversal)


# Set up tree
tree = BinaryTree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)

# Test search
# Should be True
print(tree.search(4))
print(tree.search(3))
# Should be False
print(tree.search(6))

# Test print_tree
# Should be 1-2-4-5-3
#print(tree.print_tree())