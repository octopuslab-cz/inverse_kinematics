from utils.transform import Point2D, invkin2
import sys, pygame, math
from random import randint
from time import sleep


pygame.init() 

size = 900                                                           
wxh = width, height = size, size
screen =  pygame.display.set_mode(wxh)  

BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

x0 = size/2
y0 = size/2
multip=2

arm = 70  # mm 70

# print(math.radians(180 / math.pi)) # def 1 rad: 360 / 2pi
# math.degrees(math.pi) # > 180.0


def trans_point(p,m=multip):
        x = x0 + p.x*m
        y = size - y0 - p.y*m
        return Point2D(x,y)


def cross(p,color,a=5,th=3):
        #cross
        pygame.draw.line(screen, color, [p.x-a,p.y], [p.x+a,p.y], th)
        pygame.draw.line(screen, color, [p.x,p.y-a], [p.x, p.y+a], th)
        pygame.display.flip()
        

def point(p,col):
        pygame.draw.line(screen, col, [p.x, p.y], [p.x, p.y+2], 2)


def p2s(p,m=multip): #point (p.x,p.y) to screen point (x,y) transform
        x = x0 + p.x * m
        y = size - y0 - p.y * m
        return (x,y)


def arm_angles(alfa,beta,color=BLUE):
        beta = alfa-beta
        sa = math.sin(math.radians(alfa))
        ca = math.cos(math.radians(alfa))

        pa = Point2D(arm * ca, arm * sa)
        cross(trans_point(pa), GREEN)
        pygame.draw.line(screen, GREEN, [x0,y0], p2s(pa), 1)
        
        sb = math.sin(math.radians(beta))
        cb = math.cos(math.radians(beta))

        pb = Point2D(arm * cb + int(pa.x), arm * sb + int(pa.y))
        cross(trans_point(pb), color)
        pygame.draw.line(screen, color, p2s(pa), p2s(pb), 1)

        pygame.display.flip()
        return(pb)   

# =====================================

p0 = Point2D(x0,y0)
p1 = Point2D(80,90)
p2 = Point2D(100,30)


def test1():
       angles = [(0,0),(60,0),(90,0),(150,0),(0,45),(60,45),(90,45),(150,45),(0,90),(60,90),(90,90),(150,90)]
       
       for angle in angles:
               alfa = angle[0]
               beta = angle[1]
               bod2 = arm_angles(alfa,beta)
               print(alfa,beta,bod2.x,bod2.y)

               alfa, beta = invkin2(p2)

               sleep(1)

#bod2 = arm_angles(alfa,beta,WHITE)
#print(alfa,beta,bod2.x,bod2.y)


def test2():
        for i in range(1000):
              alfa = randint(0,180)
              beta = randint(0,360)
              bod2 = arm_angles(alfa,beta)




def test5():
        for i in range(10):
              x = randint(50,120)
              y = randint(50,120)
              p3 = Point2D(x,y)
              cross(trans_point(p3), WHITE)
              alfa, beta = invkin2(p3)
              print(x,y,alfa,beta)
              arm_angles(alfa, beta)
        

def test6():
       points = [(10,10),(30,30),(50,100),(75,100),(50,50),(75,75),(100,50),(100,75),(90,90)]
       
       for p in points:
              p2 = Point2D(p[0],p[1])          
              cross(trans_point(p2), WHITE)
              
              alfa, beta = invkin2(p2)
              print(p[0],p[1],alfa,beta)
              arm_angles(alfa, beta)

              sleep(1)
             

def test7():
    for j in range(6):     
        for i in range(6):
              x = j * 15
              y = i * 15
              p2 = Point2D(x,y)          
              cross(trans_point(p2), WHITE)
              
              alfa, beta = invkin2(p2)
              print(x,y,alfa,beta)
              
              arm_angles(alfa,beta)

              sleep(0.5)

# =====================================
print("start")
cross(p0, RED)
      
#test1()
#test2()

test7()
