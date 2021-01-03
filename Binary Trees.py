from Queues import Queue 
from Stacks import Stack

class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None
        
class Binary_Tree:
    def __init__(self, root):
        self.root = Node(root)
        
    def preorder(self, start, traversal):
        if start != None:
            traversal.append(start.value)
            traversal = self.preorder(start.left, traversal)
            traversal = self.preorder(start.right, traversal)
        
        return traversal
    
    def inorder(self, start, traversal):
        if start != None:
            traversal = self.inorder(start.left, traversal)
            traversal.append(start.value)
            traversal = self.inorder(start.right, traversal)
        
        return traversal
    
    def postorder(self, start, traversal):
        if start != None:
            traversal = self.postorder(start.left, traversal)
            traversal = self.postorder(start.right, traversal)
            traversal.append(start.value)
        
        return traversal
 
    def levelorder(self, start):
        if start is None:
            return
        queue = Queue()
        queue.enqueue(start)
        
        traversal = []
        while len(queue) > 0:
            traversal.append(queue.front())
            node = queue.dequeue()
            
            if node.left != None:
                queue.enqueue(node.left)
            if node.right != None:
                queue.enqueue(node.right)
        
        return traversal
            
    def mylevelorder(self, start):
        nodes = []
        temp = []
        if start != None:
            temp.append(start)
        
        while len(temp) != 0:
                nodes.append(temp[0].value)

                if temp[0].left:
                    temp.append(temp[0].left)
                if temp[0].right:
                    temp.append(temp[0].right)
                    
                temp.pop(0)
        
        return nodes

    def reverse_levelorder(self, start):
        if start is None:
            return
        
        stack = Stack()
        stack.push(start)
        
        traversal = []
        while len(stack) > 0:
            traversal.append(stack.peek().value)
            node = stack.pop()
            
            if node.left:
                stack.push(node.left)
            if node.right:
                stack.push(node.right)
                
        return traversal[::-1]
    
    def size(self, start, count):
        if start != None:
            count += 1
            count = self.size(start.left, count)
            count = self.size(start.right, count)
        
        return count
    
    def height(self, start):
        if start is None:
            return
        
        level = 0
        parents = [start]
        children = []
        switch = True
        
        while switch:
            for parent in parents:
                if parent.left:
                    children.append(parent.left)
                if parent.right:
                    children.append(parent.right)
                    
            if len(children) == 0:
                switch =  False
            else:
                parents = children
                children = []
                level += 1
        
        return level
    
    
            
                

     
tree = Binary_Tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
tree.root.right.right.right = Node(8)


print(tree.preorder(tree.root, []))
print(tree.inorder(tree.root, []))
print(tree.postorder(tree.root, []))
print(tree.levelorder(tree.root))
print(tree.mylevelorder(tree.root))
print(tree.reverse_levelorder(tree.root))
print(tree.size(tree.root, 0))
print(tree.height(tree.root))

