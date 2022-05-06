
class Node:
    
    def __init__(self, data):
        self.data = data
    def __repr__(self):
        return "Node data: %s" % self.data    

class Queue:
    
    def __init__(self):
        self.data = None
        self.size = []
        self.back = -1
        self.front = 5

    def enqueue(self, data):
        if self.back == 5:
            return 'Queue is full'
        else:    
            new_node = Node(data)
            self.back += 1
            self.size.append(data)

    def isfull(self):
        return self.back == self.front
    def isEmpty(self):
        return self.back != self.front

    def dequeue(self):
        if self.back == -1:
            return 'Empty Queue'
        else:
            self.size.pop(self.back)
            self.back += 1    

    def length(self):
        return self.back  

    def display(self):
        return print(self.size)         


q = Queue()
q.enqueue('josue')
q.enqueue('christ')
q.enqueue('emme')
q.enqueue('54')
q.enqueue('lili')
q.enqueue('nono')
q.enqueue('junior')
q.enqueue(45)
q.display()
q.dequeue()
q.display()
print(q.isfull())
print(q.isEmpty())