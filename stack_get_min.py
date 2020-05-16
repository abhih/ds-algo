class Stack(object):
    min=[]
    def __init__(self,length):
        self.stack=[]
    def getlength(self):
        return len(self.stack)
    def push(self,item):
        self.stack.append(item)
        if self.min==[]:
            self.min.append(item)
        if item<self.min[0]:
            self.min[0]=item
    def getmin(self):
        return self.min
    def pop(self):
        return(self.stack.pop())
    def getelement(self):
        return self.stack

obj=Stack(5)
print(obj.getlength())
obj.push(5)
obj.push(9)
obj.push(9)
obj.pop()
obj.push(1)
print(obj.getmin())
obj.push(2)
obj.push(3)
print(obj.getmin())
obj.push(0)
print(obj.getelement())
print(obj.getmin())