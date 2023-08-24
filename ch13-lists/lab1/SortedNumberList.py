from Node import Node

class SortedNumberList:
    def __init__(self,):
        self.head = None
        self.tail = None

#Solution:

    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        # Inserts a node with the value after the last smaller node, if no target can be found the insert function prepends the list
        self.insert_after(Node(number), self.find_last_smaller(number)) 

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # Calls remove on searched key, returns false if key not found, returns true and modifies the list if key is found
        return self.remove_at(self.find_equal_node(number))
    
    # Helper Functions
    
    # remove at target node helper function
    def remove_at(self, target_node):
        
        # Returns false and does nothing if no target node given
        if target_node == None:
            return False

        # Get the next and previous nodes
        previous = target_node.get_previous()
        next = target_node.get_next()
        
        # if next isn't null connect it's previous value to the previous node
        if next is not None:
            next.set_previous(previous)
        
        # if previous isn't null set it's next value to the next node
        if previous is not None:
            previous.set_next(next)
        
        # if the node is the head, set the next node to the next node
        if target_node is self.head:
            self.head = next
        
        # if the node is the tail, set the tail to the previous node
        if target_node is self.tail:
            self.tail = previous
        
        #returns true as the node was found
        return True

    # Equal node finder helper function
    # Returns the first equal node or None if nothing is found
    def find_equal_node(self, key):
        current_node = self.head
        while(current_node != None and current_node.data <= key):
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None
    
    # Returns the last Node Smaller than a key value or None if all are greater
    def find_last_smaller(self, key):
        current_node = self.head
        smallest = None
        while(current_node != None and current_node.data < key):
            smallest = current_node
            current_node = current_node.next
        return smallest
       
    #prepend helper function
    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
    
    # insert after helper function
    def insert_after(self, new_node, target_node):
        
        # If no target node is specified the list is prepended, this covers both the case of the list being empty and the case that no nodes are smaller than the new node
        if target_node is None:
            self.prepend(new_node)
            
        # if the target is the tail connect the node and make it the new tail
        elif target_node is self.tail:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node
        
        # otherwise connect the new node between the target and it's successor node
        else:
            successor_node = target_node.get_next()
            new_node.set_next(successor_node)
            new_node.set_previous(target_node)
            target_node.set_next(new_node)
            successor_node.set_previous(new_node)