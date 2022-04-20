# Create a element that could be in linked list
class Element:
    def __init__(self, value):
        self.value = value
        self.next = None

# Create linked list
class LinkedList:
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            # While we've not in the end of the linked list
            while current.next:
                # Change current element to the next one in the linked list
                current = current.next
            # Point the last element in the linked list to the new element
            current.next = new_element
        else:
            self.head = new_element

    def get_position(self, position):
        # Track current position and current element
        position_track = 1
        current = self.head
        while current:
            # check if position given equal the one we track
            if position == position_track:
                return current
            
            current = current.next
            position_track += 1

        return None

    def insert(self, new_element, position):
        position_track = 1
        current = self.head
        # 1:next:2 2:next:3 //4 3:next:4
        while current:
            # check if position given equal position track plus one to make some code run before we're in the position given
            if position == position_track + 1:
                # add new element in the position given and point the next to the prev element in that position
                new_element.next = current.next
                current.next = new_element
            # otherwise add one to position and change current element to the next one
            current = current.next
            position_track += 1
        pass

    def delete(self, value):
        current = self.head
        prev = None
        while current:
            if current.value == value:
                #If the number given is in the head of linked list
                if not prev:
                    #change the head to point the next element
                    self.head = current.next
                    current.next = None
                    return
                #change the prev point next from the current to the next of the current
                prev.next = current.next
                current.next = None
                return
            # otherwise add one to position and change current element to the next one
            prev = current
            current = current.next
        pass



# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print(ll.head.next.next.value)
# Should also print 3
print(ll.get_position(3).value)

# Test insert
ll.insert(e4,3)
# Should print 4 now
print(ll.get_position(3).value)

# Test delete
ll.delete(1)
# Should print 2 now
print(ll.get_position(1).value)
# Should print 4 now
print(ll.get_position(2).value)
# Should print 3 now
print(ll.get_position(3).value)