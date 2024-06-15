import pymunk as pm
import pygame as pg
import random as ran

pg.init()

screen = pg.display.set_mode((1200,700))
Space = pm.Space()
clock = pg.time.Clock()
FPS = 40
population  = 300

class Ball():

    def __init__(self,x = 0,y =0):
        self.x = x
        self.y = y
        self.Body = pm.Body()
        self.Body.position = x , y
        self.shape = pm.Circle(self.Body,15)
        self.indc = 0
        self.shape.elasticity = 1
        self.Body.velocity = -10,50
        self.shape.density = 1
        self.shape.collision_type = 1
        Space.add(self.Body,self.shape)
        

    def draw(self):

        if (self.indc == 1):
            pg.draw.circle(screen,(255,0,0),(int(self.Body.position[0]),int(self.Body.position[1])),15)
        elif (self.indc == 2):
            pg.draw.circle(screen,(0,255,0),(int(self.Body.position[0]),int(self.Body.position[1])),15)
        else:
            pg.draw.circle(screen,(150,150,0),(int(self.Body.position[0]),int(self.Body.position[1])),15)
        
    def collide(self,space = 0,arbiter  = 0,data = 0):
        if ( self.shape.collision_type <= population + 1 ):
            self.shape.collision_type = population + 2
            self.indc = 1
            
        else:
            self.shape.collision_type = population + 3
            self.indc =2
        
    
class wall():
    def __init__(self,x,y):
        self.Body = pm.Body(body_type= pm.Body.STATIC)
        self.walls = pm.Segment(self.Body,x,y,10)
        self.walls.elasticity = 1
        Space.add(self.Body,self.walls)

def game():
        balls = [ Ball(ran.randint(0,1200),ran.randint(0,700)) for _ in range(0,population)  ]

        for i in range (1,population+1):
            balls[i-1].shape.collision_type = i
            handler = Space.add_collision_handler(i,population+2)
            # handler = Space.add_collision_handler(population + 2,population +3)
            handler.separate = balls[i-1].collide

        ran.choice(balls).collide()

        wallop = [wall((0,0),(0,700)),
            wall((0,700),(1200,700)),
            wall((1200,700),(1200,0))
            ,wall((1200,0),(0,0))]
        
        for ball in balls:
            ball.draw()
        while True:   
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
            screen.fill((255,255,255))
            
            for ball in balls:
                ball.draw()
            
            clock.tick(FPS)

            Space.step(1/FPS)
            pg.display.update()

game()
pg.quit()
        