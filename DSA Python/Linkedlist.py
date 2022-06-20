from audioop import add


class Node:
    data = None
    next_node = None
    def __init__(self, data):
        self.data = data


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
        return None       


    def display(self):
        curNode = self.head
        while curNode is not None :
            print(f'{curNode.data} -> ' )
            curNode = curNode.next_node

Info = Linkedlist()
road = (input('Type the information concerning the road-> ')).split(',')
# ici toutes les information doivent etre separer par une vigurle comme ceci,
# lundi, 7:AM, 9min, 250frs, pointA, pointB

Info.add(road)
Info.display()
print(type(road))


        