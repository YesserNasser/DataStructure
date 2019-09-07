# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 14:20:29 2019
@author: Yesser H. Nasser
"""
''' ======================== Depth-first Search ============================'''
''' 
Depth-first search algorithm is a graph traversal algorithm
- when given a choice it will go deeper into a graph (unlike BFS)
which explores graph breadth wise first, it works in both directed and undirected graphs

Attributes of DFS vertex:
    - Discovery time
    - Finish time
    - Color
    - Predecessor Vertex (pi)

Example of the graph to apply DFS algorithm
          A -------- B          C
          |          |          |
          |          |          |
          |          |          |
D ------- E          F -------- G
 \       /          / \        / 
  \     /          /   \      /
   \   /          /     \    /
    \ /          /       \  /
     H -------- I          J
    
The algorithm has 2 classes
Vertex class and Graph class

# ========================= vertex class  =====================================
5 instance variables:
 - name (vertex's name)
 - neighbors [] (list of neighbors - directly connected Vertices)
 - discovery time (dicovery time of the vertex)
 - finish time (finish time of the vertex)
 - color (color)
function:
    add_neighbor(v) v: name of vertex

# =========================== Graph class =====================================
Store all the vertices in dictionary object: vertices {} (key, value) pair
3 functions: 
    - add_vertex(vert) takes vertex object and add it this vertex dictionary
    - add_edge(u,v) function that takes the A, B, C, D the character from and to
    - dfs() depth-first search function
===============================================================================
# neighbors[]                 |      # vertices{}
A: B, E                       |    'A' -> vertex A
B: A, F                       |    'B' -> vertex B
C: G                          |    'C' -> vertex C
D: E, H                       |    'D' -> vertex D
E: A, D, H                    |    'E' -> vertex E
F: B, G, I, J                 |    'F' -> vertex F
G: C, F, J                    |    'G' -> vertex G
H: D, E, I                    |    'H' -> vertex H
I: F, H                       |    'I' -> vertex I
J: F, G                       |    'J' -> vertex J
'''
''' ========================================================================'''
''' ========================= Pyhton Implementation ========================'''
class Vertex:
    def __init__(self,n): # constractor for the class vertex
        self.name = n # takes name
        self.neighbors = list()
        
        self.discovery = 0 # initial values
        self.finish = 0 # intial values
        self.color = 'black' # initial color
        
    def add_neighbor(self,v): # takes vertex letter A, B, ...
        nset = set(self.neighbors) # convert neighbors list into a set
        if v not in nset: # check if it is in neighbors list if not
            self.neighbors.append(v) # append to neighbors
            self.neighbors.sort() # resort
class Graph:
    vertices = {}
    time = 0
    
    def add_vertex(self,vertex): # take a vertex
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v): # vertices at either end
        if u in self.vertices and v in self.vertices: # check if u and v are existing vertices in our graph
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v) # setting the neighbors in the Vertex class for u and v
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False
    
    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print (key + str(self.vertices[key].neighbors)+ " " + str(self.vertices[key].discovery) + "/" +str(self.vertices[key].finish))
            
# DFS could be recursive or iterative (an iterative function is one that loops to repeat some part of the code, 
# and a recursive function is one that calls itself again to repeat the code.)     
# recursive implementation of dfs  
            
    def _dfs(self, vertex): #(used internally) take vertex
        global time
        vertex.color = 'red' # set color to red (discovered)
        vertex.discovery = time
        time += 1
        
        for v in vertex.neighbors: # iterate through vertex neighbors 
            if self.vertices[v].color == 'black': # test if its block
                self._dfs(self.vertices[v])
        vertex.color = 'blue' # set color to blue ===> finished
        vertex.finish = time
        time +=1
    
    def dfs(self, vertex): # pass a vertex (it could any vertex)
        global time
        time = 1 # set time to 1 and pass it to _dfs
        self._dfs(vertex)
        
        
g = Graph()
a = Vertex('A') 
g.add_vertex(a) 
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'DA', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.dfs(a)
g.print_graph()