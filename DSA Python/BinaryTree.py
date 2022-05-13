from ast import Sub


class BinTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
def preorder(SubTree):
    if SubTree is not None:
        print(f'{SubTree.data}')
        preorder(SubTree.left)
        preorder(SubTree.right)

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

preorder(n5)