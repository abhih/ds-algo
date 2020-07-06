from collections import defaultdict
import sys

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
    def vertex_count(self):
        return len(self.vertices_list)
    
    def min_distance(self,vertex,unvisited_set):
        min_weight=sys.maxint
        # total_vertices_length=self.vertices_list
        # for i in range(total_vertices_length):
    
    def dijkstra(self,source):
        #neighbours=source.get_neighbours()
        visited_set=defaultdict(lambda : False)
        visited_cost = {source: 0}
        # initial_weight=0
        vertex_list=self.vertices_list
        visited_set[source]=True
        path={}
        #print([str(i) for i in vertex_list])
        #print(set(vertex_list))
        #set_trace()
        while len(vertex_list) != 0:
            min_node=None
            for node_index in range(1,len(vertex_list)):
                try:
                    if visited_set[vertex_list[node_index-1]]:
                        if min_node is None:
                            min_node=vertex_list[node_index-1]
                        elif visited_cost[vertex_list[node_index-1]] < visited_cost[min_node]:
                            min_node=vertex_list[node_index-1]
                except Exception as e:
                    print(e)
                    continue
            if min_node is None:
                break
            # print(str(min_node))
            # print(str(min_node), min_node in vertex_list)
            vertex_list.remove(min_node)
            current_cost = visited_cost[min_node]
            current_neighbours = min_node.get_neighbours()
            for nbr_index in range(1,len(current_neighbours)):
                try:
                    next_cost = current_cost + min_node.get_neighbour_weight(current_neighbours[nbr_index-1])
                except Exception as e :
                    print(e)
                    continue
                #next_cost = min_node.get_neighbour_weight(current_neighbours[nbr_index])
                if not visited_set[current_neighbours[nbr_index-1]] or next_cost < current_cost:
                    visited_set[current_neighbours[nbr_index-1]]=True
                    visited_cost[current_neighbours[nbr_index-1]]=next_cost
                    path[current_neighbours[nbr_index-1]] = min_node
        print("visited_cost",visited_cost)
        print("path is ",[str(i) for i in path])
            
A=Vertex("A")
B=Vertex("B")
C=Vertex("C")
D=Vertex("D")
E=Vertex("E")
A.set_neighbour(B,"1")
B.set_neighbour(C,"2")
C.set_neighbour(D,"3")
D.set_neighbour(E,"4")
A.set_neighbour(C,"1")
C.set_neighbour(E,"2")

g=Graph([A,B,C,D,E])
g.dijkstra(A)
#print(g.vertex_count())
