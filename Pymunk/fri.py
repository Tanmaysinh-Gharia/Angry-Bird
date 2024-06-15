import pymunk as pm         # Import pymunk..
import pygame as pg

pg.init()

height_o_screen = 700
screen = pg.display.set_mode((1200,height_o_screen))
clock = pg.time.Clock()
FPS = 40

def convert_cord(cords):
    return cords[0],height_o_screen-cords[1]

space = pm.Space()

body = pm.Body()
body.position = 200,700
body.mass = 1
shape = pm.Circle(body,30)

shape.density = 1
shape.elasticity = 0
shape.friction = 6
space.add(body,shape)
space.gravity = 0, -500

segment_body = pm.Body(body_type=pm.Body.STATIC)
segment_shape = pm.Segment(segment_body,(0,200),(1200,0),25)
segment_shape.elasticity = 0
segment_shape.friction = 1.5
segment_shape.friction = 5
space.add(segment_body,segment_shape)
image = pg.image.load("Tenni.png")
image = pg.transform.scale(image,(60,60))

def game():
    while True:
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        
        screen.fill((255,255,255))
        x,y = convert_cord(body.position)
        # print(x,y)
        pg.draw.circle(screen,(255,0,0),(int(x),int(y)),30)
        pg.draw.line(screen,(0,0,0),(0,500),(1200,700),50)
        screen.blit(image,(int(x)-30,int(y)-30))
        pg.display.update()
        print(body.position[0],body.position[1])
        clock.tick(FPS)
        space.step(1/FPS)
        
game()
pg.quit()
    
