import sys
class MinHeap(object):
    def __init__(self,maxsize):
        self.maxsize=maxsize
        self.heap=[0] * (self.maxsize+1)
        self.heap[0]=-1 * sys.maxsize
        self.size=0
        self.HEAD=0
    def left_child(self,pos):
        return 2*pos
    def right_child(self,pos):
        return (2*pos)+1
    def parent(self,pos):
        return pos//2
    def insert(self,elem):
        if self.size < self.maxsize:
            self.heap[self.size]=elem
            self.size+=1
            current=self.size
            while self.heap[current] < self.heap[self.parent(current)]:
                self.swap(current,self.parent(current))
                current=self.parent(current)

    def get_heap(self):
        return (self.heap)
    def swap(self, item1,item2):
        self.heap[item1],self.heap[item2]=self.heap[item2],self.heap[item1]
    def is_leaf(self,pos):
        if pos >= (self.size//2) and pos <= self.size: 
            return True
        return False
    def heapify(self,pos):
        if not self.is_leaf(pos):
            if self.heap[pos] > self.heap[self.left_child(pos)] or self.heap[pos] > self.heap[self.right_child(pos)]:
                if self.heap[self.left_child(pos)] > self.heap[self.right_child(pos)]:
                    self.swap(pos,self.right_child(pos))
                    self.heapify(self.right_child(pos))
                if self.heap[self.left_child(pos)] < self.heap[self.right_child(pos)]:
                    self.swap(pos,self.left_child(pos)) #swap the smaller size element
                    self.heapify(self.left_child(pos))
            
    def min_heap(self):
        for pos in range(self.size//2, 0, -1):
            self.heapify(pos)

    def display(self): 
        for i in range(1, (self.size//2)+1): 
            print(" PARENT : "+ str(self.heap[i])+" LEFT CHILD : "+
                str(self.heap[self.right_child(i)])+" RIGHT CHILD : "+
                str(self.heap[self.left_child(i)])) 

    def delete(self):
        popped=self.heap[-1]
        self.heap=self.heap[:-1]
        self.size-=1
        self.min_heap()
        return popped


mheap=MinHeap(7)
mheap.insert(10)
mheap.insert(2)
mheap.insert(3)
mheap.insert(4)
mheap.insert(5)
mheap.insert(6)
(mheap.min_heap())
mheap.display()