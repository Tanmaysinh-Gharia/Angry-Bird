import pygame as pg

pg.init()

screen = pg.display.set_mode((1200 ,600))

clock = pg.time.Clock()
FPS = 40

accleration = 1

class Ball():
    def __init__(self):
        self.y = 300
        self.velocity = 5
    
    def draw(self):
        pg.draw.circle(screen,(255,100,0),(450,self.y),15)

    def move(self):
        self.velocity += accleration
        self.y += self.velocity

        if self.y >= 500:
            self.velocity = -self.velocity
        
        # if self.y < 50:
        #     self.velocity = -self.velocity

def print_text(text,position):
    font = pg.font.SysFont("Times New Roman",40,True)
    font_surf = font.render(text,True,(0,0,255),(255,255,0))
    screen.blit(font_surf,position)

ls = [ (10,10) , (10,100) , (100,100) , (100,10)]
def game():
    ball = Ball()
    while True:
        image = pg.image.load("download.jpg")
        image = pg.transform.scale(image,(1200,600))
        
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return
        screen.fill((255,255,255))
        # pg.draw.circle(screen,(255,100,0),(450,150),15)
        # screen.blit(image,(0,0))
        pg.draw.line(screen,(0,0,0),(0,500),(1200,500),7)
        pg.draw.lines(screen,(0,0,255),True,ls,3)

        ball.draw()
        ball.move()
        print_text("Tanmay",(600,300))
        pg.display.update()
        clock.tick(FPS)
        print("velocity {}".format(ball.velocity))
        print("Y : {}".format(ball.y))

game()
pg.quit()
