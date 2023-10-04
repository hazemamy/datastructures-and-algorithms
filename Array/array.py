import ctypes

class Array:
    def __init__(self,size):
        array_data_type = ctypes.py_object * self._capacity
        self.size = size
        self._capacity = max(16, 2*size )
        
        self.memory = array_data_type()

        for i in range(self._capacity):
            self.memory[i] = None


    def __get__ (self,idx):
        self.memory[idx]

    def __set__ (self,idx,val):
        self.memory[idx] = val

    def __disp__ (self):
        for n in range(self._capacity):
            print(self.memory[n])



    def __append__ (self, num):
        if self.size == self._capacity:
            self.expand_capacity
        self.memory[self.size] = num 
        self.size += 1