from traceback import print_tb


class Node:
    def __init__(self,data):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = Node
        self.last_node = None
    def append(self, data):
        if self.last_node == None:
           self.head = Node(data)
           self.last_node = self.head
        else :
            self.last_node.next = Node(data)
            self.last_node = self.last_node.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data, end = ' ')
            current = current.next

        
a_llist = LinkedList()
n = int(input("how many elements would you like to add?"))
for i in range (n):
    data = int(input("Enter data item :"))
    a_llist.append(data)     
print('the linkrd list: ',end= " ")
a_llist.display()