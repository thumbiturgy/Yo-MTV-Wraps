class Node:
    
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class BinarySearchTree:
    
    def __init__(self, root_value):
        self.root = Node(root_value)
        
        
    def add_node(self, value, node=None):
        if not node:
            node = self.root
        if value > node.value:
            if not node.right:
                node.right = Node(value)
            else:
                return self.add_node(value, node.right)
        else:
            if not node.left:
                node.left = Node(value)
                return
            else:
                return self.add_node(value, node.left)
        
    def get_min(self, node=None):
        if not node:
            node = self.root
        if node.left:
            return self.get_min(node.left)
        else:
            return node.value
    
    def get_max(self, node=None):
        if not node:
            node = self.root
        if node.right:
            return self.get_max(node.right)
        else:
            return node.value
        
    def iterate_max(self, node=None):
        if not node:
            node = self.root
        while node.right:
            node = node.right
        return node.value
            
    def contains(self, target):
        current_node = self.root
        while current_node:
            if target == current_node.value:
                return True
            if target > current_node.value:
                current_node = current_node.right
            else:
                current_node = current_node.left
        return False
    def print_in_order(self, node = None):
        if not node:
            node = self.root
        if node:
            if node.left:
                self.print_in_order(node.left)
            print(node.value)
            if node.right:
                self.print_in_order(node.right)