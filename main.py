import numpy as np
import pygame as pg
import math


class Background:
    def __init__(self):
        pg.init()
        self.Res = self.WIDTH, self.HEIGHT= 600, 600
        self.FPS = 60
        self.screen = pg.display.set_mode(self.Res)
        self.clock = pg.time.Clock()
        
    def draw(self):
        self.screen.fill(pg.Color("darkslategray"))
        

    def run(self):
        while True:
            self.draw()
            [exit() for i in pg.event.get() if i.type == pg.QUIT]
            pg.display.set_caption(str(self.clock.get_fps()))
            pg.display.flip()
            self.clock.tick(self.FPS)

class Ball(pg.sprite.Sprite):
    """A ball that will move across the screen
    Returns: ball object
    Functions: update, calcnewpos
    Attributes: area, vector"""

    def __init__(self, vector):
        pg.sprite.Sprite.__init__(self)
        self.image = 3 
        screen = pg.display.get_surface()
        self.area = screen.get_rect()
        self.vector = vector

    def update(self):
        newpos = self.calcnewpos(self.rect,self.vector)
        self.rect = newpos

    def calcnewpos(self,rect,vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)

class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        self.z = coordinates[2]
        
class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop  = stop
class Wireframe:
    def __init__(self):
        self.nodes = []
        self.edges = []


    def addNodes(self, nodeList):
        for node in nodeList:
            self.nodes.append(Node(node))
    def addEdges(self, edgeList):
        for (start, stop) in edgeList:
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))


    def outputNodes(self):
        print("\n --- Nodes --- ")
        for i, node in enumerate(self.nodes):
            print( " %d: (%.2f, %.2f, %.2f)" % (i, node.x, node.y, node.z))
                
    def outputEdges(self):
        print ("\n --- Edges --- ")
        for i, edge in enumerate(self.edges):
            print( " %d: (%.2f, %.2f, %.2f)" % (i, edge.start.x, edge.start.y, edge.start.z),)
            print( "to (%.2f, %.2f, %.2f)" % (edge.stop.x,  edge.stop.y,  edge.stop.z))


if __name__ == '__main__':
    cube_nodes = [(x,y,z) for x in (0,1) for y in (0,1) for z in (0,1)]
    cube = Wireframe()
    cube.addNodes(cube_nodes)
    cube.addEdges([(n,n+4) for n in range(0,4)])

    cube.addEdges([(n,n+1) for n in range(0,8,2)])
    cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    cube.outputNodes()
    cube.outputEdges()
