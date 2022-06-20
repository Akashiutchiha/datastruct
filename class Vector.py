class Vector(object):
    def __init__(self):
    
        #actual number of elements in the array
        self.size = 0
        #maximum capacity of the array initialized to 2
        self.capacity = 2
        self.array = self._create_array(self.capacity)
        
    def length(self):
        #This method returns the length of the array
        return self.size
        
        #This method verifies whether an element exist in the Vector
    def contains(self, item):
        for i in range (self.size):
    	    if self.array[i] == item:
                return True

        #This method gets an item at a particular index
    def getitem(self, ndx):
        if not 0 <= ndx<self.size:
            print("Invalid Index")
            return
        return self.array[ndx]
        
    def setitem(self, ndx, item):
        #Replaces the element at index ndx
        if ndx < 0 or ndx>self.size:
            return "IndexError"
        self.array[ndx]= item
       
    def append(self, item):
        #Adds a new element to the end of the array
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
            
        self.array[self.size] = item
        self.size +=1
        
        
    def insert(self, ndx, item):
        #Inserts an element at index
        if ndx < 0 or ndx>self.size:
            print("IndexError")
            return
        
        if self.size == self.capacity:
            self._resize(2*self.capacity)
            
        for i in range(self.size-1, ndx-1,-1):
            self.array[i+1] = self.array[i]
            
        self.array[ndx] = item
        self.size +=1
        
    def remove(self, ndx):
        #returns the value at index
        if self.size == 0:
            print("EmtpyVector")
            return
        
        if ndx < 0 or ndx>self.size-1:
            print("IndexError")
            return
        
        if ndx == self.size-1:
            item = self.array[ndx]
            self.array[ndx] = None
            return item
            
        item = self.array[ndx]
        for i in range (ndx, self.size-1,-1):
            self.array[i] = self.array[i+1]	
        self.array[self.size] = None
        self.size -=1
        #error: displays the element of array[size] as 'None' and doesn't correctly return the item'
        return item
        
    def indexof(self, item):
        for i in range(self.size - 1):
            if self.array[i] == item:
                return i
            else: "ItemError"   
        
        
        #This method appends a vactor to another vector 
    def extend(self, second_Vector):
        second_Vector = Vector()
        new_Vector = Vector()
        new_Vector.array = self.array + second_Vector.array
        return new_Vector.array

        #Creates a new vector which is a subvector of another vector containing values 
        #from start to end
    def subVector(self, start, end):
        new_Vector = Vector()
        for i in range(self.size - 1):
            if i > start-1 and i <= end:
                new_Vector.append(self.array[i])
                return new_Vector.array
            else: pass
        
    def iterator(self):
        for i in range(self.size - 1):
            return self.array[i]

    
    def _create_array(self, length):
        #Method that creates the array of given size
        return [None] *length
    
    def _resize(self, new_capacity):
        #Resizes the array to the new capacity by creating a new array
        new_array = self._create_array(new_capacity)
        
        # Reassigning all elements in the old array into the new one 
        for i in range(self.size):
            new_array[i] = self.array[i]
            
        self.array = new_array
        self.capacity = new_capacity
        
    def delete(self):
        #pops the last element from the end of the array
        element = None
        
        if self.size > 0: #if the array is not empty,
            element = self.array[self.size-1]
            self.array[self.size-1] = None #empty the placeholder at index self.size-1
            self.size -= 1
            
            # if self.size < self.capacity//4:
            #     self._resize(self.capacity//2)
            
        return element

    def show_array(self):
        for i in range(self.size):
            print(self.array[i])
 


