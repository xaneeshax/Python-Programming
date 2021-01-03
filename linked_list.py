class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        
    
class linked_list:
    def __init__(self):
        self.head = node()
        
    def append(self, data):
        new_node = node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = new_node
        
    def length(self):
        count = 0
        current = self.head
        while current.next != None:
            current = current.next
            count += 1
        return count
    
    def display(self):
        current = self.head
        elements = []
        while current.next != None:
            current = current.next
            elements.append(current.data)
        return elements
    
    def get(self, index):
        current = self.head
        if self.length() <= index:
            print('invalid - index out of range')
            return None
        else:
            while current.next != None:
                current = current.next
                index -= 1
                if index == -1:
                    return current.data
                
    def erase(self, index):
        if self.length() < index:
            print('invalid - index out of range')
            return 
        else:
            current = self.head
            for ind in range(index):
                current = current.next
            current.next = current.next.next   
            return
        
    def delete_list(self):
        current = self.head
        current.next = None
        return
    
    def get_from_end(self, index):
        index = self.length() - index - 1
        return self.get(index)
    
    def middle_of_list(self):
        import math
        length = self.length()
        index = math.floor(length / 2)
        if length % 2 == 1:
            return self.get(index)
        else:
            return (self.get(index - 1), self.get(index))
        
    def count_occur(self, num):
        current = self.head
        times = 0
        while current.next != None:
            current = current.next
            if current.data == num:
                times += 1
        return times
                
    def is_palindrome(self):
        elems = self.display()
        for i in range(len(elems) // 2):
            if elems[i] != elems[-(i+1)]:
                return False
            return True
            
    def remove_duplicates_ord(self):
        if self.head.next != None:
            current = self.head.next
            alt = current
            num = current.data
        while current.next != None:
            current = current.next
            if current.data != num:
                alt = current    
            num = current.data
            
                    
                

                
   
linked = linked_list()
linked.append(1)
linked.append(1)
linked.append(4)
linked.append(4)
linked.append(5)

print(linked.is_palindrome())


'''
print(linked.count_occur(1))
print(linked.count_occur(2))
print(linked.count_occur(9))
print(linked.middle_of_list())
print(linked.get_from_end(0))
print(linked.length())
print(linked.display())
print(linked.get(0))
print(linked.display())
print(linked.get(2))
print(linked.display())
linked.erase(3)
print(linked.display())    
#linked.delete_list()
#print(linked.display())
'''