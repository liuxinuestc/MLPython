class aa:
    def __init__(self,array):
        self.arr = array
        self.length = len(array)
    def swap_0_n(self,n,index0):
        t = 0
        for i in range(self.length):
            if self.arr[i] == n:
                t = i
                break
        self.arr[index0] = n
        self.arr[t] = 0
        return t
    def swap_0_sort(self):
        index0 = 0
        for i in range(self.length):
            if (self.arr[i] == 0):
                index0 = i
        for i in range(1,self.length):
            if i == self.arr[i]:
                continue
            if self.arr[i] == 0:
                index0 = self.swap_0_n(i,i)
            else:
                self.arr[index0] = self.arr[i]
                self.arr[i] = 0
                index0 = self.swap_0_n(i,i)
        return self.arr

import numpy.random as rand
a = list(range(9))
# rand.shuffle(a)
b = aa(a)
print(a)
print(b.swap_0_sort())




