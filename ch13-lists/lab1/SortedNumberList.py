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
        self.insert_after(Node(number), self.find_last_smaller(number, self.head)) 

    # Removes the node with the specified number value from the list. Returns
    # True if the node is found and removed, False otherwise.
    def remove(self, number):
        # Calls remove on searched key, returns false if key not found, and returns true and modifies the list if the key is found
        return self.remove_at(self.find_equal_node(number, self.head))
    
    # Helper Functions
    
    # remove at target node helper function
    def remove_at(self, node_to_remove):
        
        # Returns False, as there was no term provided and nothing was removed
        if node_to_remove == None:
            return False
        
        # Get the next and previous nodes belonging to the node to be removed
        previous = node_to_remove.get_previous()
        next = node_to_remove.get_next()

        # if next isn't null connect it's previous value to the previous node
        if next is not None:
            next.set_previous(previous)        
        
        # if previous isn't null set it's next value to the next node
        if previous is not None:
            previous.set_next(next)        
        
        # if the node to be removed is the head, set the head to the next node
        if node_to_remove is self.head:
            self.head = next        
        
        # if the node is the tail, set the tail to the previous node
        if node_to_remove is self.tail:
            self.tail = previous
        
        # returns true as the node was found and removed
        return True

    # Recursive Equal node finder helper function
    # Returns the first equal node or None if nothing is found
    def find_equal_node(self, key, current_node):
        if (current_node != None and current_node.get_data() <= key):
            if current_node.get_data() == key:
                return current_node
            return self.find_equal_node(current_node.get_next())
        return None
    
    # Recursive Last smaller node finder, returns None if none are smaller
    def find_last_smaller(self, key, current_node):
        if (current_node != None and current_node.get_data() < key):
            next_nodes = self.find_last_smaller(key, current_node.get_next())
            if(next_nodes == None):
                return current_node
            else:
                return next_nodes
       
    # prepend helper function
    def prepend(self, new_node):
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.set_next(self.head)
            self.head.set_previous(new_node)
            self.head = new_node
    
    # slightly modified insert after helper function
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