class Node:
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data

    def __repr__(self) -> str:
        return "<Node data: %s>" % self.data  

class Linkedlist:

    def __init__(self):
        self.head = None  
    def is_empty(self):
        return self.head == None 

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next_node   
        return count  

    def add(self, data):
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        current = self.head
        while current:
            if current.data == key:
                return key
            else:
                current = current.next_node 
        return 'Not found'    

#This will be used for displaying the linkedlist created
    def __repr__(self):
        nodes = []
        current = self.head
        while(current):
            if current == self.head:
                nodes.append("[head > %s]" % current.data)
            elif current.next_node == None:
                nodes.append('[Tail > %s]' % current.data)
            else:
                nodes.append("[%s]" % current.data)   
            current = current.next_node
        return "->".join(nodes)  

               