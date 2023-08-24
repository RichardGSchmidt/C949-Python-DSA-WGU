from Node import Node

class SortedNumberList:
    def __init__(self,):
        self.head = None
        self.tail = None    

# Solution:

    # Inserts the number into the list in the correct position such that the
    # list remains sorted in ascending order.
    def insert(self, number):
        
        # Finds the last node smaller than number
        last_smaller = self.find_last_smaller(number)
        
        # If nothing is smaller, prepend the new node, this also covers the event the list is empty
        if last_smaller is None:
            self.prepend(Node(number))
            
        # Otherwise insert the new node after the last smaller node
        else:
            self.insert_after(Node(number), last_smaller) 

            


    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        
        # Finds first node matching key value is in list
        node_to_remove = self.find_equal_node(number)
        
        # If the node isn't found False is returned
        if node_to_remove == None:
            return False
            
        # Otherwise the found node is removed 
        else:
            self.remove_at(node_to_remove)
            return True

        

    # helper methods
    
    # remove at target node helper function
    def remove_at(self, target_node):
        
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

    # Equal node finder helper function
    # Returns the first equal node or None if nothing is found
    def find_equal_node(self, key):
        current_node = self.head
        while(current_node != None):
            if current_node.data == key:
                return current_node
            current_node = current_node.next
        return None
    
    # Returns the last Node Smaller than a key value or None if all are greater
    def find_last_smaller(self, key):
        current_node = self.head
        smallest = None
        while(current_node != None):
            if current_node.data < key:
                smallest = current_node
            current_node = current_node.next
        return smallest
       
    #prepend helper function
    def prepend(self, newNode):
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head.previous = newNode
            self.head = newNode
    
    # insert after helper function
    def insert_after(self, new_node, target_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        elif target_node is self.tail:
            self.tail.set_next(new_node)
            new_node.set_previous(self.tail)
            self.tail = new_node
        else:
            successor_node = target_node.get_next()
            new_node.set_next(successor_node)
            new_node.set_previous(target_node)
            target_node.set_next(new_node)
            successor_node.set_previous(new_node)