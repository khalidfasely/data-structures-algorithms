class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST(object):
    def __init__(self, root):
        self.root = Node(root)

    def insert(self, new_val):
        pointer = self.root
        inserted = False
        while not inserted:

            if pointer.value > new_val:
                if pointer.left is None:
                    pointer.left = Node(new_val)
                    inserted = True
                    break
                pointer = pointer.left

            elif pointer.value < new_val:
                if pointer.right is None:
                    pointer.right = Node(new_val)
                    inserted = True
                    break
                pointer = pointer.right

    def search(self, find_val):
        pointer = self.root

        #In case the root is the value we searching about
        if pointer.value == find_val:
            return True
        
        finish_searching = False
        while not finish_searching:
            if pointer.value > find_val:
                if pointer.left is None:
                    finish_searching = True
                    return False
                pointer = pointer.left
            
            elif pointer.value < find_val:
                if pointer.right is None:
                    finish_searching = True
                    return False
                pointer = pointer.right

            else:
                return True

# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print(tree.search(4))
# Should be False
print(tree.search(6))