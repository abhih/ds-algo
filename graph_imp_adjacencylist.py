#https://www.python-course.eu/graphs_python.php
class Vertex(object):
    def __init__(self,vertex):
        self.vertex=vertex
    def __str__(self):
        return self.vertex
    

class Graph(object):
    def __init__(self):
        self.vertices={}
    def add_neighbour(self,vertex1,vertex2,weight=1):
        if vertex1 not in self.vertices:
            self.vertices[vertex1]=[(vertex2,weight)]
        else:
            self.vertices[vertex1].append((vertex2,weight))
    def get_vertices(self,vertex):
        return self.vertices[vertex]
    def get_all_vertices(self):
        return self.vertices.keys()
    def add_vertex(self,vertex):
        self.vertices[vertex]=[]

    def __str__(self):
        graph_=""
        for v,e in self.vertices.items():
            for edges in e:
                graph_=graph_+"( " +str(v) + "\t->\t" +  str(edges[1]) + "\t->\t" + str(edges[0]) +")"
        return graph_

    def bfs(self,start):
        q = []
        from collections import defaultdict
        
        visited = defaultdict(lambda: False) #[False] * len(self.get_all_vertices())
        q.append(start)
        while q:
            s=q.pop()
            print(s)
            neighbors=self.get_vertices(s)
            for items in (neighbors):
                next_node=items[0]
                if next_node and not visited[next_node]:
                    #print(next_node)
                    visited[next_node]=True
                    q.append(next_node)
    def dfs(self,start):
        pass

        
A=Vertex("A")
A0=Vertex("A0")
A1=Vertex("A1")
A2=Vertex("A2")
A3=Vertex("A3")
A4=Vertex("A4")
A5=Vertex("A5")
graph=Graph()
graph.add_vertex(A)
graph.add_vertex(A0)
graph.add_vertex(A1)
graph.add_vertex(A2)
graph.add_neighbour(A,A0,10)
graph.add_neighbour(A0,A1,1)
graph.add_neighbour(A0,A2,12)
#graph.add_neighbour(A1,A2,2)
# graph.add_neighbour(A2,A3,3)
# graph.add_neighbour(A3,A4,3)
# graph.add_neighbour(A4,A5,11)
# graph.add_neighbour(A5,A,20)

#print(graph.get_vertices(A0))
#print(graph.get_vertices(A2))

print(graph)
(graph.bfs(A))