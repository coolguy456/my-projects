import pygame
from pygame.locals import *
import random
import math
import time
import os


file = open("maze.txt","r")
maze = file.read()
file.close()

pygame.init()
pellet = pygame.mixer.Sound("pellet.wav")
eatgh = pygame.mixer.Sound("eatgh.wav")
eatfruit = pygame.mixer.Sound("eatfruit.wav")
extralife = pygame.mixer.Sound("extralife.wav")
score = 0
fconstants = [(112,324),(362,324),(237,468),(237,132)]
font = pygame.font.SysFont("arial",20)
screen = pygame.display.set_mode((500,600),0,32)
image = pygame.image.load("maze.jpg").convert()
xconstants = []
pygame.display.set_caption("pacman pacman")
clock = pygame.time.Clock()
k = 1
nodes = {}
def node(x):
    for i in x:
        
        if (i[0],i[1]-24) in x:
            s1="u"
        else:
            s1="n"
        if (i[0],i[1]+24) in x:
            s2="d"
        else:
            s2="n"
        if (i[0]-25,i[1]) in x:
            s3="l"
        else:
            s3="n"
        if (i[0]+25,i[1]) in x:
            s4="r"
        else:
            s4="n"
        s = s1 + s2 + s3 + s4    
        if (s != "udnn") & (s != "nnlr"):
            nodes[i] = s


    
class pachero:
    def __init__(self):
        self.x = 212
        self.y = 564
        self.color = (255,255,0)
        self.olddirect = ""
        self.direction = ""
        self.state = "off"
        self.time1 = 0
        self.time2 = "no"
    def movement(self):
                  
       if (self.x,self.y) in xconstants:
           self.state = "off"
       else:
           self.state = "on"
       if (time.time() - self.time1 < 15.0)   &   (self.time1 != 0) :
           self.time2 = "yes"
       else :
           self.time2 = "no"
       if (o1.x,o1.y) in fconstants:
        global score
        eatfruit.play()
        score =  score + 50
        fconstants.remove((o1.x,o1.y))
        self.time1 = time.time()
        
       if self.state == "off":
           if self.direction == "up":
               if (self.x,self.y - 24) in xconstants:
                  self.y = self.y - 1
                  self.olddirect="up"
           if self.direction == "down":
               if (self.x,self.y + 24) in xconstants:
                  self.y = self.y + 1
                  self.olddirect = "down"
           if self.direction == "left":
               if (self.x-25,self.y) in xconstants:
                  self.x = self.x - 1
                  self.olddirect = "left"
           if self.direction == "right":
               if (self.x + 25 , self.y) in  xconstants:
                  self.x = self.x + 1
                  self.olddirect = "right"

            
       if self.state == "on":
           if self.olddirect == "up":
               self.y = self.y - 1
           if self.olddirect == "down":
               self.y = self.y + 1
           if self.olddirect == "left":
               self.x = self.x - 1
           if self.olddirect == "right":
               self.x = self.x + 1

       def rtrn(self):
           return (self.x,self.y)

class ghost:
    def __init__(self,color):
        self.x = 262
        self.y = 252
        self.direction = "right"
        self.color = color
        self.oldcolor = color
        self.state = 0
    
    def movement(self,x,y,tim):
        self.state = 0
        dire = []
        if (self.x , self.y) in nodes.keys():
            a = nodes[(self.x , self.y)]
            if a[0] == "u":
                dire.append("up")
            if a[1] == "d":
                dire.append("down")
            if a[2] == "l":
                dire.append("left")
            if a[3] == "r":
                dire.append("right")    
            self.direction = random.choice(dire)

        if self.direction == "up":
            self.y = self.y - 1
        if self.direction == "down":   
            self.y = self.y + 1
        if self.direction == "left":
            self.x = self.x - 1
        if self.direction == "right":
            self.x = self.x + 1
        if tim == "yes":
            self.color = (255,255,255)
        else:
            self.color = self.oldcolor
            
        if (math.sqrt((self.x - x)**2 + (self.y - y)**2) < 24.0):
            if (self.color == (255,255,255)):          
              self.color = self.oldcolor
              eatgh.play()
              global score
              score = score + 80
              self.x = 262
              self.y = 252
            else:
              self.state = 1  
    def rtrn(self):
        return (self.x,self.y)

        
def drawrect(x,y,s):
    x2 = 25*x
    y2 = 24*y
    x1 = x2-25
    y1 = y2-24
    pygame.draw.rect(s,(0,0,0),(x1,y1,25,24),0)
    pygame.draw.circle(s,(255,255,0),(int((x1+x2)/2),int((y1+y2)/2)),3)
     
screen.fill((153,102,204))   
i = 0
while i<525:
    try:
      index = maze.index("1",i,525)
      y = int(index/21) + 1
      x = (index % 21) + 1
      #drawrect(x,y,screen)
      i = index + 1
      xconstants.append((25*(x-1)+12,24*(y-1)+12))
      
    except ValueError:
        i=526


cconstants = xconstants.copy()
#print(cconstants)
node(xconstants)
o1 = pachero()
g1 = ghost((0,255,255))
g2 = ghost((255,51,51))
g3 = ghost((51,51,255))
g4 = ghost((51,255,51))
fimage = pygame.image.load("fruit.gif").convert()
boole = True
while boole:
    screen.blit(image,(0,0))
    screen.blit(font.render("score = "+str(score),True,(255,255,255)),(0,0))
    if (o1.x,o1.y) in cconstants:
        pellet.play()
        score = score + 10
        #print((o1.x ,o1.y) in cconstants)
        cconstants.remove((o1.x, o1.y))
        
    
    for i in cconstants:
        pygame.draw.circle(screen,(255,255,0),i,3)
    for i in fconstants:
        screen.blit(fimage,(i[0]-7,i[1]-10))
    pacman = pygame.draw.circle(screen,o1.color,(o1.x , o1.y),12)
    skyghost = pygame.draw.circle(screen,g1.color,(g1.x , g1.y),12)
    redghost = pygame.draw.circle(screen,g2.color,(g2.x , g2.y),12)
    blueghost = pygame.draw.circle(screen,g3.color,(g3.x , g3.y),12)
    greenghost = pygame.draw.circle(screen,g4.color,(g4.x , g4.y),12)
    clock.tick(100)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            boole = False
        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_DOWN:
                o1.direction = "down"
            if event.key == pygame.K_UP:
                o1.direction = "up"
            if event.key == pygame.K_LEFT:
                o1.direction = "left"
            if event.key == pygame.K_RIGHT:
                o1.direction = "right"
         
    o1.movement()
    if (g1.state == 1)|(g2.state == 1)|(g3.state == 1)|(g4.state == 1):
        score = 0
        extralife.play()
        o1.x = 212
        o1.y = 564
    g1.movement(o1.x,o1.y,o1.time2)
    g2.movement(o1.x,o1.y,o1.time2)
    g3.movement(o1.x,o1.y,o1.time2)
    g4.movement(o1.x,o1.y,o1.time2)
   
    pygame.display.update()
pygame.display.quit()
