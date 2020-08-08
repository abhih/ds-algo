import sys
from collections import defaultdict

class Vertex(object):
    count=0
    def __new__(cls,*args):
        cls.count+=1
        return super(Vertex,cls).__new__(cls,args)
    def __init__(self,name):
        self.name=name
        self.neighbours={}
        self.count+=1
    def set_neighbour(self,vertex,weight):
        self.neighbours[vertex]=int(weight)
    def get_neighbours(self):
        return self.neighbours.keys()
    def get_neighbour_weight(self,vertex):
        return self.neighbours[vertex]
    def __str__(self):
        return self.name
    
class Graph(object):
    def __init__(self,vertices_list):
        self.vertices_list=vertices_list#self.vertex_count()#[] #all vertex list
        self.parent = defaultdict(lambda : -1)
    def vertex_count(self):
        return len(self.vertices_list)
    #to work with kruskal , you need to know about the disjoint set data structure. Its basically involves having a parent array initialized to -1
    #and then one find function to find the parent of the set and another union function to set the parent of the set, and another create set,
    #to create the data structure. Here we are using path compression technique using the parent array.
    
    def create_set(self,x):
        return set(x)
    def find_parent(self,parent,x):
        if self.parent[x]==-1:
            return x
        return self.find_parent(parent, parent[x]) #sending the parent of x for recursive
            
    def union(self,parent,x,y):
        x_set=self.find_parent(parent,x)
        y_set=self.find_parent(parent,y)
        parent[y_set]=x_set
        #return parent
    
    def is_cyclic(self):
        # parent = defaultdict(lambda : -1)
        #node_set=set()
        for vertex in self.vertices_list:
            nbr_vertex_list = vertex.get_neighbours()
            # print("nbr_vertex_list",[str(i) for i in nbr_vertex_list])
            # if len(nbr_vertex_list)==0:
            #     continue
            print([str(key)+":"+ str(self.parent[key]) for key in self.parent.keys()])
            for nbr in nbr_vertex_list:
                parent_x=self.find_parent(self.parent,vertex)
                parent_y=self.find_parent(self.parent,nbr)
                if parent_x==parent_y:
                    print("Yes")
                    return True
                # else:
                #     self.parent[parent_y] = parent_x
                #print(parent_x,parent_y)
                self.union(self.parent,parent_x,parent_y)
            
    def sort_edges(self):
        weight_list=[]
        for vertex in self.vertices_list:
            nbr_vertex=vertex.get_neighbours()
            for nbr in nbr_vertex:
                # print("{vertex} --{weight}-- {nbr}".format(vertex=vertex,weight=vertex.get_neighbour_weight(nbr),nbr=nbr))
                weight= vertex.get_neighbour_weight(nbr)
                u = vertex
                v = nbr
                weight_list.append({weight:(u,v)})
        
        weight_list = sorted(weight_list,key=lambda x: x.keys())
        #print(weight_list)
        return weight_list
    def kruskal(self):
        """
        so all you have to do is to use the path compression technique to find the loopable elements and just ignore it and you have kruskal
        """
        weight_list=self.sort_edges()
        result= []
        #parent = defaultdict(lambda : -1)
        for item in weight_list:
            x=item.values()[0][0]
            y=item.values()[0][1]
            # print(x,y)
            parent_x = self.find_parent(self.parent,x)
            parent_y = self.find_parent(self.parent,y)
            if parent_x==parent_y:
                continue
            else:
                result.append(item)
                self.union(self.parent,parent_x,parent_y)
        for item in result:
            weight = item.keys()
            vertex = item.values()[0][0]
            nbr = item.values()[0][1]
            print("{vertex} --{weight}-- {nbr}".format(vertex=vertex,weight=weight,nbr=nbr))
#---------------------------------------------------------------------------------------------------------------------------#

    def find_min(self,visited):
        min_vertex = None,None
        min_weight = sys.maxint
        for vertex in self.vertices_list:
            if visited[vertex]:
                nbr_vertex = vertex.get_neighbours()
                for nbr in nbr_vertex:
                    nbr_weight = vertex.get_neighbour_weight(nbr)
                    if (not visited[nbr]) and min_weight>nbr_weight:
                        min_weight = nbr_weight
                        min_vertex = (vertex,nbr)
        return min_vertex

    def prim(self,source):
        visited=defaultdict(lambda : False)
        parent = self.parent
        vertex = source
        nbrs_vertex=vertex.get_neighbours()
        visited[vertex] = True
        for index in range(len(self.vertices_list)):
            vertex, min_vertex  = self.find_min(visited)
            
            if not min_vertex:
                continue
            print("Vertex")
            print(str(vertex), str(min_vertex))
            x_set = self.find_parent(parent,vertex)
            y_set = self.find_parent(parent,min_vertex)
            print("Parent")
            print(str(x_set),str(y_set))
            if x_set!=y_set:
                parent[min_vertex]=vertex
            visited[vertex] = True
            visited[min_vertex] = True
            
        print(["Parent "+str(parent[i]) + "::: Child  "+str(i) for i in parent])
    
        
    
A=Vertex("A")
B=Vertex("B")
C=Vertex("C")
D=Vertex("D")
E=Vertex("E")
F=Vertex("F")
G=Vertex("G")


###
A.set_neighbour(B,"2")
B.set_neighbour(A,"2")
A.set_neighbour(D,"1")
D.set_neighbour(A,"1")
B.set_neighbour(D,"3")
D.set_neighbour(B,"3")
B.set_neighbour(C,"5")
C.set_neighbour(B,"5")
C.set_neighbour(D,"4")
D.set_neighbour(C,"4")
###
# A.set_neighbour(B,"28")
# B.set_neighbour(C,"16")
# #B.set_neighbour(G,"14")
# C.set_neighbour(D,"12")
# D.set_neighbour(E,"22")
# #D.set_neighbour(G,"18")
# E.set_neighbour(F,"23")
# #E.set_neighbour(G,"24")
# F.set_neighbour(A,"10")

g=Graph([A,B,C,D,E,F,G])
#g.print_vertex_weight()
#g.is_cyclic()
#g.sort_edges()
#g.kruskal()
g.prim(A)