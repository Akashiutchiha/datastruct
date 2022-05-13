
class BinTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add(self, item, pos):
        if self.left == None or self.right is None:
            new_root = BinTree(item)
            if pos == 'left':
                self.right = new_root
            else:
                self.left = new_root
        else:
            print('element cannot be added here')




def preorder(SubTree):
    if SubTree is not None:
        print(f'{SubTree.data}')
        preorder(SubTree.left)
        preorder(SubTree.right)

def inorder(SubTree):
    if SubTree is not None:
        preorder(SubTree.left)
        print(f'{SubTree.data}')
        preorder(SubTree.right)

def postorder(SubTree):
    if SubTree is not None:
        preorder(SubTree.left)
        preorder(SubTree.right)
        print(f'{SubTree.data}')

n5 = BinTree(5)
n2 = BinTree(2)
n4 = BinTree(4)
n3 = BinTree(3)
n1 = BinTree(1)
n7 = BinTree(7)
n6 = BinTree(6)

#         5
#        / \
#       2   4
#      / \ / \ 
#     3  1 7  6
n5.right = n4
n5.left = n2
n2.right = n1
n2.left = n3
n4.right = n6
n4.left = n7


n7.add(5, 'right')
preorder(n4)