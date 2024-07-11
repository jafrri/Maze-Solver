## Kruskal's Algorithm for Maze Generation
## Neil Thistlethwaite

from PIL import Image
import random
import numpy as np
import pandas as pd
global GRAPH_SIZE, CELL_THICKNESS, WALL_THICKNESS
import copy

## Somewhat naive implementation, as it doesn't do rank balancing,
## but this could easily be replaced with something more efficient.
class DisjointSet:
    def __init__(self, nodes):
        self.node_mapping = {}
        for i,val in enumerate(nodes):
            n = self.DSNode(val, i)
            self.node_mapping[val] = n

    def find(self, node):
        return self.find_node(node).parent

    def find_node(self, node):
        if type(self.node_mapping[node].parent) is int:
            return self.node_mapping[node]
        else:
            parent_node = self.find_node(self.node_mapping[node].parent.val)
            self.node_mapping[node].parent = parent_node
            return parent_node

    def union(self, node1, node2):
        parent1 = self.find_node(node1)
        parent2 = self.find_node(node2)
        if parent1.parent != parent2.parent:
            parent1.parent = parent2

    class DSNode:
        def __init__(self, val, parent):
            self.val = val
            self.parent = parent
## Maze generation parameters. Change as desired.
def generator(string):
    if string=="medium":
        GRAPH_SIZE = 30
    elif string=="easy":
        GRAPH_SIZE= 15
    elif string=="hard":
        GRAPH_SIZE= 50
    CELL_THICKNESS = 1
    WALL_THICKNESS = 1

    nodes = [(i,j) for j in range(GRAPH_SIZE) for i in range(GRAPH_SIZE)]
    neighbors = lambda n : [(n[0]+dx,n[1]+dy) for dx,dy in ((-1,0),(1,0),(0,-1),(0,1))
                            if n[0]+dx >= 0 and n[0]+dx < GRAPH_SIZE and n[1]+dy >= 0 and n[1]+dy < GRAPH_SIZE]

## Kruskal's Algorithm
    edges = [(node, nbor) for node in nodes for nbor in neighbors(node)]
    maze = []
    ds = DisjointSet(nodes)

    while len(maze) < len(nodes)-1:
        edge = edges.pop(random.randint(0, len(edges)-1))
        if ds.find(edge[0]) != ds.find(edge[1]):
            ds.union(edge[0], edge[1])
            maze.append(edge)

    img = np.zeros((GRAPH_SIZE * (CELL_THICKNESS + WALL_THICKNESS) + WALL_THICKNESS,
                    GRAPH_SIZE * (CELL_THICKNESS + WALL_THICKNESS) + WALL_THICKNESS),dtype=np.uint8)
    lst=[]

    for edge in maze:
        min_x = WALL_THICKNESS+min(edge[0][0],edge[1][0])*(CELL_THICKNESS + WALL_THICKNESS)
        max_x = WALL_THICKNESS+max(edge[0][0],edge[1][0])*(CELL_THICKNESS + WALL_THICKNESS)
        min_y = WALL_THICKNESS+min(edge[0][1],edge[1][1])*(CELL_THICKNESS + WALL_THICKNESS)
        max_y = WALL_THICKNESS+max(edge[0][1],edge[1][1])*(CELL_THICKNESS + WALL_THICKNESS)
        img[min_x:max_x+CELL_THICKNESS,min_y:max_y+CELL_THICKNESS] = 255
    img1=copy.deepcopy(img)
    im = Image.fromarray(img)

    for i in range(len(img1)):
        for j in range(len(img1[i])):
            if img1[i][j]==0:
                img1[i][j]=1
            elif img1[i][j]==255:
                img1[i][j]=0
    string=""
    for i in range(len(img1)):
        for j in range(len(img1[i])):
            if img1[i][j]==0:
                string=string+" "
            elif img1[i][j]==1:
                string=string+"X"
        string=string+"\n"
    file = open("small.txt","r+")
    file.truncate(0)
    file.write(string)
    file.close()
#generator()
#df1=pd.DataFrame(img1)
#df1.to_excel(r'C:\Users\HU-Student\Downloads\idea1.xlsx')

#im.show()
#im.save(input(r'C:\Users\HU-Student\Downloads\maze.jpg'))

## Save maze (include extension!)
