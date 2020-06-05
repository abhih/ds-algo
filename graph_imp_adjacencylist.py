#https://www.python-course.eu/graphs_python.php
from collections import defaultdict

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
        try:
            vert=self.vertices[vertex]
        except Exception as e:
            vert=None
        return vert
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
        visited = defaultdict(lambda: False) #[False] * len(self.get_all_vertices())
        q.append(start)
        while q:
            s=q.pop()
            print(s)
            neighbors=self.get_vertices(s)
            for items in (neighbors):
                next_node=items[0]
                if next_node and not visited[next_node]:
                    visited[next_node]=True
                    q.append(next_node)
    def _dfs(self,start,visited):
        print(start)
        visited[start] = True
        neighbors=self.get_vertices(start)
        if not neighbors:
            return
        for vertex_weight in neighbors:
            vertex=vertex_weight[0]
            if not visited[vertex]:
                self._dfs(vertex,visited)
    
    def dfs(self,start):
        visited = defaultdict(lambda : False)
        return self._dfs(start,visited)
    
    def topological_sort(self):
        in_degree = defaultdict(lambda : 0)
        for v in self.vertices:
            vertices=self.get_vertices(v)
            for vertex_edge in vertices:
                vertex=vertex_edge[0]    
                in_degree[vertex]+=1
        indegree_dict={k:in_degree[k] for k in self.get_all_vertices()}
        print("Indegree items",{str(k):in_degree[k] for k in indegree_dict.keys()})
        result=[]
        q=[]
        for v,degree in indegree_dict.items():
            if degree==0:
                q.append(v)
        print("initial queue items",[str(i) for i in q])
        while q:
            zero_indegree_vertex=q.pop()
            result.append(zero_indegree_vertex)
            all_nbr_vertices=self.get_vertices(zero_indegree_vertex)
            # if not all_nbr_vertices:
            #     return [str(i) for i in result]
            for v_e in all_nbr_vertices:
                v=v_e[0]
                if indegree_dict[v]>0:
                    indegree_dict[v]-=1
                if indegree_dict[v]==0:
                    q.append(v)

        return [str(i) for i in result]

        
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
graph.add_vertex(A3)
graph.add_vertex(A4)
#graph.add_vertex(A5)
graph.add_neighbour(A,A0,1)
graph.add_neighbour(A0,A1,2)
graph.add_neighbour(A0,A2,3)
graph.add_neighbour(A1,A2,4)
graph.add_neighbour(A2,A3,5)
graph.add_neighbour(A2,A4,6)
graph.add_neighbour(A3,A4,7)
# graph.add_neighbour(A4,A5,11)
#graph.add_neighbour(A5,A,20)
#graph.add_neighbour(A4,A,11)
#print(graph.get_vertices(A0))
#print(graph.get_vertices(A2))

print(graph)
#graph.bfs(A)
#print(graph.dfs(A1))
print(graph.topological_sort())