import pygame as pg
from OpenGL.GL import *
import numpy as np


class App:
    def __init__(self) -> None: 

        # Initialize Pygame
        pg.init()
        pg.display.set_mode((640, 400), pg.OPENGL|pg.DOUBLEBUF)
        self.clock = pg.time.Clock()

        # Initialize Opengl
        glClearColor(1, 0.2, 0.2, 1)
        self.mainloop()

    def mainloop(self):
        running: bool = True

        while running:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

            # refresh screen
            glClear(GL_COLOR_BUFFER_BIT)
            pg.display.flip()

            # timer
            self.clock.tick(60)
        self.quit()

    def quit(self):
        pg.quit( )      


class Triangle:
    def __init__(self) -> None:
        # x y z r g b
        self.vertices = (
            -0.5, -0.5, 0.0, 1.0, 0.0, 0.0,
             0.5, -0.5, 0.0, 0.0, 1.0, 0.0,
             0.0,  0.5, 0.0, 0.0, 0.0, 1.0
        )
        
        self.vertices = np.array(self.vertices, dtype=np.float32)

        self.vertices = 3
        self.vao = glGenVertexArrays(1)
        glBindVertexArray(self.vao)
        self.vbo = glGenBuffers(1)
        glBindBuffer(GL_ARRAY_BUFFER, self.vbo)
        glBufferData(GL_ARRAY_BUFFER, self.vertices.nbytes, self.vertices, GL_STATIC_DRAW)
        glEnableVertexAttribArray(0)
        glVertexAttribPointer(0, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(0))
        glEnableVertexAttribArray(1)
        glVertexAttribPointer(1, 3, GL_FLOAT, GL_FALSE, 24, ctypes.c_void_p(12))


    def destroy(self):
        glDeleteVertexArrays(1, (self.vao,))
        glDeleteBuffers(1, (self.vbo,))

        
if __name__=='__main__':
    app: App = App()