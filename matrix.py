class Matrix(object):
    def __init__(self,row,column):
        self.row=row
        self.column=column
        self.matrix=[
            [0] * (self.row),
            [0] * (self.column)]
    def display(self):
        print(self.matrix)
        # for i in range(len(self.matrix[0])):
        #     for j in range(len((self.matrix[1]))):
        #         print(self.matrix[i][j])
    def disp_coordinates(self,x,y):
        print(self.matrix[x][y])

    def set_matrix(self,x,y,val):
        self.matrix[x][y]=val

obj=Matrix(2,2)
obj.set_matrix(1,1, "A")
#obj.disp_coordinates(1,1)
obj.display()