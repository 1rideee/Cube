import numpy as np
import pygame as pg

class Cube:
    def __init__(self):
        pg.init()
        self.Res = self.WIDTH, self.HEIGHT= 1600, 900
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

if __name__ == '__main__':
    app = Cube()
    app.run()
