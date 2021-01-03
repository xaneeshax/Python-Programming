class Stack:
    def __init__(self):
        self.items = []
        
    def push(self, item):
        self.items.append(item)
        
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        if self.items == []:
            return True
        return False
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
    
    def get_stack(self):
        return self.items
    
    def __len__(self):
        return len(self.items)
    
'''
stack = Stack()
print(stack.is_empty())
stack.push(1)
stack.push(2)
stack.push(3)
print(stack.peek())
stack.pop()
print(stack.get_stack())
'''


def is_balanced(parens):
    s = Stack()
    balanced = True
    index = 0
    
    while index < len(parens) and balanced:
        char = parens[index]
        if char in '({[':
            s.push(char)
        else:
            if s.is_empty():
                balanced = False
            elif s.peek() + char in ['()', '{}', '[]']:
                s.pop()
            else: 
                balanced = False
        index += 1
        
    if not s.is_empty():
        balanced = False
            
    return balanced
            
print(is_balanced('((){}{}[])'))
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        