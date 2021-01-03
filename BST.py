
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.help_insert(data, self.root)
            
    def help_insert(self, data, current):
        if data < current.data:
            if current.left is None:
                current.left = Node(data)
            else:
                self.help_insert(data, current.left)
        
        elif data > current.data:
            if current.right is None:
                current.right = Node(data)
            else:
                self.help_insert(data, current.right)
                
        else:
            print('value is already present in the tree')
    
    def find(self, data):
        if self.root:
            is_found = self._find(data, self.root)
            if is_found:
                return True
            return False
        else:
            return None
        
    def _find(self, data, current):
        if data > current.data and current.right:
            return self._find(data, current.right)
        elif data < current.data and current.left:
            return self._find(data, current.left)
        if data == current.data:
            return True
        

        
    def preorder(self, start, traversal):
        if start != None:
            traversal.append(start.data)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        
        return traversal
    
    
    def bst_property(self, start):
        if start is None:
            return True
        else:
            nodes = [start]
            while len(nodes) != 0:
                current = nodes[0] 
                if current.right:
                    if current.data < current.right.data:
                        nodes.append(current.right)
                    else:
                        return False
                
                if current.left:
                    if current.data > current.left.data:
                        nodes.append(current.left)
                    else:
                        return False      
                nodes.pop(0)
            return True  

    
            
                     
                        
                    
                
            
tree = BST()
tree.insert(4)
tree.insert(2)
tree.insert(8)
tree.insert(5)
tree.insert(10)
tree.root.left.left = Node(11)

print(tree.preorder(tree.root, []))
print(tree.bst_property(tree.root))











