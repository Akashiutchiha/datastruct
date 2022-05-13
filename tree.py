class BinTree():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def preorder(self):
        list = []
        list.append(self.data)