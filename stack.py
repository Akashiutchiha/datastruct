class Stacks():
    def __init__(self, size):
        self.top = -1
        self.container = []
        limit = 10
        self.size = size

        if self.size > limit:
            self.size = limit


    def push(self, x):
        if self.is_full():
            print('Is full')
            return
        self.container.append(x)
        self.top += 1
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            existing = self.container[self.top]
            self.container.pop(self.top)
            self.pop -= 1
            return existing
    def is_empty(self):
        return self.top < 0
    def is_full(self):
        return len(self.container) >= self.size

    def peek(self):
        if self.is_empty():
            return -1
        else :
            return self.container[self.top]
    def snap(self):
        print(self.container)


s1 = Stacks()
s1.push()