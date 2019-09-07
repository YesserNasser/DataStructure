# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 10:06:12 2019
@author: Yesser H. Nasser
ref: https://github.com/joeyajames/Python/blob/master/bfs.py
video = https://www.youtube.com/watch?v=-uR7BSfNJko
"""

""" Breath-First Search : is a graph traversal algorithm
it finds every vertex that is reachable from the source and finds its distance from the source
(the distance is the number of edges to traverse to reach that vertex)
it works on Directed and Undirected Graphs
it runs in O(V + E) time (v : numver of vertices, E : number of Edges)"""
"""
==== Example of BFS on a undirected graph ====
to explore the graph we assign attribute to each vertex

           A ---------- B         C
        /  |            |         |
      /    |            |         |
    /      |            |         |
  /        |            |         |
D -------- E            F ------- G
 \       /             / \       /
  \     /             /   \     /
   \   /             /     \   /
    \ /             /       \ /
     H ----------- I         J

The algorithm have 2 classes
Vertex class and Graph class

# ========================= vertex class  =====================================
4 variables:
 - name (vertex's name)
 - neighbors [] (list of neighbors - directly connected Vertices)
 - distance (the distance form the source)
 - color (color)
function:
    add_neighbor(v) v: name of vetex

# =========================== Graph class =====================================
Store all the vertices in dictionary object: vertices {}
4 functions: 
    - add_vertex(vert) takes vertex object and add it this vertex dictionary
    - add_edge(u,v) function that takes the letter name of the vortex at either end of the edge
    - print_graph() function
    - bfs() breadth-first search function

# === vertex class  ===
# color:
    red: visited
    black: not visited
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
       
"""
""" ====================== Python Implementation ==========================="""
'''=== vertex class ==='''
class Vertex:
    def __init__ (self,n):
        self.name = n
        self.neighbors = list() # creat an empty list for neighbors
        self.distance = 9999 # initilize distance to high number
        self.color = 'black' # initilize the color to black (unvisisted)
    
    def add_neighbor(self,v): # v the name of vertex
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort() # store the neighbors as sorted list
            
'''=== graph class ==='''
class Graph:
	vertices = {} # vertices dictionary

	def add_vertex(self, vertex): # takes vertex object
		if isinstance(vertex, Vertex) and vertex.name not in self.vertices: # check if vertex is a vertex object
			self.vertices[vertex.name] = vertex  # add to vertex dictionary
			return True
		else:
			return False

	def add_edge(self, u, v): # pass in the letter at either end of that edge
		if u in self.vertices and v in self.vertices: # verify that both are valid vertices in the graph
			for key, value in self.vertices.items():
				if key == u:
					value.add_neighbor(v)
				if key == v:
					value.add_neighbor(u)
			return True
		else:
			return False
	
	def print_graph(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + str(self.vertices[key].neighbors) + "  " + str(self.vertices[key].distance))

	def bfs(self, vert): # it takes vertex object as starting point
		q = list() #bfs uses q to process all these vertices, start empty q
		vert.distance = 0 # set distance to 0 since th distance to a vertex itself is 0
		vert.color = 'red'  # set color to red since we are already visting it
		for v in vert.neighbors:  #loop through each of the starting points neighbors and set its distance to 1
			self.vertices[v].distance = vert.distance + 1
			q.append(v)

		
		while len(q) > 0:  # pop of top vertex of the queue as long as this one item on the queue
			u = q.pop(0)  # is the letter name of the vertex we wanna get the vetex object
			node_u = self.vertices[u] # we assign vertex object to node_u
			node_u.color = 'red' # set node_u color to red since we gonna visit that vertex
			
			for v in node_u.neighbors: # we iterate on node_u neighbors 
				node_v = self.vertices[v] # for each vertex in its neighbor we get a vertex object
				if node_v.color == 'black': # if that neighbor vertex has not been visited 
					q.append(v)  # the we append neighbor vertex to our queue
					if node_v.distance > node_u.distance + 1:  # if neighbur distance is greater than u_distance form the source
						node_v.distance = node_u.distance + 1 # then we update his node_u distance + 1

g = Graph()
a = Vertex('A') 
g.add_vertex(a) 
g.add_vertex(Vertex('B'))

for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AD', 'AE', 'BF', 'CG', 'DE', 'HI', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs(a)
g.print_graph()




