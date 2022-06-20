# Just go through this Code an Comment 


class Vector:
    def __init__(self, data1, data2):
        self.data1 = data1
        self.data2 = data2
        self.Vec_arr = [data1, data2]
        

    def lenght(self):
        return len(self.Vec_arr)

    def contains(self, item):
        for i in self.Vec_arr:
            if item is self.Vec_arr[i]:
                return True
            else: return False

    def getitem(self, ndx):
        for i in range(len(self.Vec_arr) - 1):
            if ndx == i:
                return self.Vec_arr[i]
            else:
                return "IndexError"

    def setitem(self, ndx, item):
        self.Vec_arr[ndx] = item

    def append(self, item):
        #The actual append method is to be written
        lst = [item]
        self.Vec_arr = self.Vec_arr + lst
        return self.Vec_arr
    
    def insert(self, ndx, item):
        #The actual insert() method is tobe written
        self.append(item)
        temp = 0
        for i in range(len(self.Vec_arr)-1, 0, -1):
            temp = self.Vec_arr[i - 1]
            self.Vec_arr[i] = self.Vec_arr[i-1]
            self.Vec_arr[i] = temp
            if i == ndx:
                self.Vec_arr[ndx] = item
                break
            else: 'IndexError'

    def remove(self, ndx):
        #Actual remove method is to be written
        for i in range(0, len(self.Vec_arr)-1):
            if i == ndx:
               self.Vec_arr.remove(i)

    def indexOf(self, item):
        for i in range(len(self.Vec_arr) - 1):
            if self.Vec_arr[i] == item:
                return i
            else: "ItemError"   

    def extend(self, Vec):
        Vec = Vector(data1 = None, data2 = None)
        Vec_arr2 = self.Vec_arr + Vec.Vec_arr


    #Subvector(from, to) still Lacking here
    #subVector(from, to)

    def iterator(self):
        items = []
        for item in self.Vec_arr:
            items.append(item)
            print(items)


v1 = Vector(1, 2)
print(v1.Vec_arr)
v2 = Vector(3, 4)
v1.append(10)
v1.append(3)
v1.insert(1, 8)
print(v1.Vec_arr)
v1.remove(2)
print(v1.Vec_arr)
print(v1.indexOf(10))

