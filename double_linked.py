class Node:
    def __init__(self, data = None):
        self.data = data
        self.next = None
        self.prev = None
        
class Double_Linked:
    def __init__(self):
        self.head = None
        
    def append(self, data):
        new_node = Node(data)
        current = self.head
        if self.head is None:
            self.head = new_node
        else:
            while current.next != None:
                current = current.next
            current.next = new_node
            
    def prepend(self,data):
        current = self.head
        if self.head is None:
            self.append(data)
        else:
            current = self.head
            new_node = Node(data)
            current.prev = new_node
            new_node.next = current
            self.head = new_node
            
    def show_list(self):
        current = self.head
        if current is None:
            return
        else:
            elems = [current.data]
            while current.next != None:
                current = current.next
                elems.append(current.data)
            return elems
     
    def length(self):
        num = 0
        current = self.head
        if current is None:
            return num
        else:
            num += 1
            while current.next != None:
                current = current.next
                num += 1
            return num
    
        
    def insert_node(self, data, index):
        length = self.length()
        if index >= length:
            print('Index out of range')
        else:
            new_node = Node(data)
            current = self.head
            if index == 0:
                self.prepend(data)
            else:
                for i in range(index):
                    current = current.next
                temp = current.next
                current.next = new_node
                new_node.next = temp
                new_node.prev = current
                temp.next.prev = new_node
    
    def delete_node(self, index):
        length = self.length()
        current = self.head
        if index >= length:
            print('Index out of range')
        elif index == 0:
            second = current.next
            current.next = None
            second.prev = None
            self.head = second
        else:
            for i in range(index):
                current = current.next
            temp = current.prev
            temp.next = current.next
            current.next.prev = temp
        
            
            
double = Double_Linked()
double.append(1)
double.append(2)
double.prepend(0)
print(double.show_list())             
    
        
    