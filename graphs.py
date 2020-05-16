class Vertex(object):
    def __init__(self,vertex):
        self.id=vertex
        self.connected={}
    def add_nbr(self,vertex,edge=0):
        self.connected[vertex]=edge
    def get_nbr_edge(self,vertex):
        return self.connected[vertex]
    def get_vertices(self):
        return self.connected.keys()
    def get_id(self):
        return self.id


    # def __str__(self):
    #     return str(self.id) + ' connected: ' + str([x.id for x in self.connected])

class Graph(object):
    def __init__(self):
        self.vertices_list={}
        self.num_vertices=0

    def __iter__(self):
        return iter(self.vertices_list.values())

    def add_vertex(self,vertex): #mapping name to object
        new_vert=Vertex(vertex)
        self.vertices_list[vertex]=new_vert
        self.num_vertices+=1
        return new_vert
    def add_edge(self,source_vertex,destination_vertex,weight=0):
        if source_vertex not in self.vertices_list:
            self.add_vertex(source_vertex)
        if destination_vertex not in self.vertices_list:
            self.add_vertex(destination_vertex)
        self.vertices_list[source_vertex].add_nbr(destination_vertex,weight)
        #self.vertices_list[destination_vertex].add_nbr(self.vertices_list[source_vertex], weight)
    def get_vertex(self,vertex):
        return self.vertices_list[vertex] if vertex in self.vertices_list else None
    def get_vertices(self):
        return self.vertices_list.keys()
    

# A=Vertex("A")
# B=Vertex("B")
# C=Vertex("C")
# D=Vertex("D")

# A.add_nbr(B,8)
# A.add_nbr(C,7)
# B.add_nbr(C,9)
# C.add_nbr(D,10)
#print(A.get_vertices())
graph=Graph()
graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_edge("A","B",2)
graph.add_edge("A","C",3)
graph.add_edge("B","C",3)
graph.add_edge("B","D",5)
graph.add_edge("C","D",4)
#graph.add_edge("C","A",5)
#print(graph.get_vertices())
#print(graph.get_vertex("A"))
for i in graph:
    #print(i)
    for vertex in (i.get_vertices()):
        print( "Source vertex {0}, dest vertex {2} , ---{1}--- ".format(i.get_id(),i.get_nbr_edge(vertex),vertex))
        
