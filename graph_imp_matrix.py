#https://www.python-course.eu/graphs_python.php
class Vertex(object):
    def __init__(self,vertex):
        self.vertex=vertex
    def __str__(self):
        return self.vertex
    

class Graph(object):
    def __init__(self,number_of_vertices):
        self.number_of_vertices=number_of_vertices
        self.graph_matrix=[[0] * number_of_vertices for _ in range(number_of_vertices)]
        
    def add_neighbour(self,vertex1,vertex2,weight=1):
        self.graph_matrix[vertex1][vertex2] = weight
        self.graph_matrix[vertex2][vertex1]=weight
        return


    def __str__(self):
        return str(self.graph_matrix)


# A=Vertex("A")
# A0=Vertex("A0")
# A1=Vertex("A1")
# A2=Vertex("A2")
# A3=Vertex("A3")
# A4=Vertex("A4")
# A5=Vertex("A5")
graph=Graph(3)
print(graph)
graph.add_neighbour(0,1,5)
graph.add_neighbour(0,2,3)
graph.add_neighbour(1,2,2)
print(graph)

#graph.add_neighbour(A2,A3,3)
# graph.add_neighbour(A3,A4,3)
# graph.add_neighbour(A4,A5,1)
# graph.add_neighbour(A5,A,2)
# graph.add_neighbour(A0,A2,1)
#print(graph.get_vertices(A0))
#print(graph.get_vertices(A2))


#print(graph.traverse_path(graph,A,A5))