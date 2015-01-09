import pygame
from pygame.locals import *
import random
import math
import time
import os
import copy


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
       print(self.state)           
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
           self.direction = ""
            
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

class greengost:
    
    def __init__(self,color):
        self.x = 262
        self.y = 252
        self.direction = "right"
        self.color = color
        self.oldcolor = color
        self.state = 0

    def movement(self,x,y,tim,st):
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

            if len(dire)>1:
                longx = 0
                longy = 0
                if (st == "up"):
                    longx = (self.x - x)
                    longy = (self.y - (y-72))
                    if ((0 < longx < 500) & (0 < longy < 600)):
                        longx = (self.x - x)
                        longy = (self.y - (y-72))
                    else:
                        longx = 0
                        longy = 0
                if (st == "down"):
                    longx = (self.x - x)
                    longy = (self.y - (y+72))
                    if ((0 < longx < 500) & (0 < longy < 600)):
                        longx = (self.x - x)
                        longy = (self.y - (y+72))
                    else:
                        longx = 0
                        longy = 0
                if (st == "left"):
                    longx = (self.x -(x-75))
                    longy = (self.y - y)
                    if ((0 < longx < 500) & (0 < longy < 600)):
                        longx = (self.x - (x-75))
                        longy = (self.y - y)
                    else:
                        longx = 0
                        longy = 0
                if (st == "right"):
                    longx = (self.x - (x+75))
                    longy = (self.y - y)
                    if ((0 < longx < 500) & (0 < longy < 600)):
                        longx = (self.x - (x+75))
                        longy = (self.y - y)
                    else:
                        longx = 0
                        longy = 0
                

                if self.color != (255,255,255): 
                

                 if ((longx > 0) & (longy > 0)):
                    if (("left" in dire) & ("up" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","left"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("right" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                      
                if self.color == (255,255,255):
                 if ((longx > 0) & (longy > 0)):
                    if (("right" in dire) & ("down" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("left" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("left","up"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                      

                            
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
    
class redgost:
    
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

            if len(dire)>1:
                longx = (self.x - x)
                longy = (self.y - y)
                if self.color != (255,255,255): 
                

                 if ((longx > 0) & (longy > 0)):
                    if (("left" in dire) & ("up" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","left"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("right" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                      
                if self.color == (255,255,255):
                 if ((longx > 0) & (longy > 0)):
                    if (("right" in dire) & ("down" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("left" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("left","up"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                      
                
                           
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
        

class sbluegost:
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
            if (math.sqrt((self.x - x)**2 + (self.y - y)**2) >= 50.0):
             if len(dire)>1:

                longx = (self.x - x)
                longy = (self.y - y)

                if self.color != (255,255,255): 
                

                 if ((longx > 0) & (longy > 0)):
                    if (("left" in dire) & ("up" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","left"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("right" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                      
                if self.color == (255,255,255):
                 if ((longx > 0) & (longy > 0)):
                    if (("right" in dire) & ("down" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("left" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("left","up"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                      

                            
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


class bluegost:
    def __init__(self,color):
        self.x = 262
        self.y = 252
        self.direction = "right"
        self.color = color
        self.oldcolor = color
        self.state = 0

    def movement(self,x,y,tim,redx,redy,st):
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

            if len(dire)>1:
#y=36 y=564 x=37 x=437
                points = []
                ddis = {}
                if (st == "up"):
                    y = (y-72)
                    
                if (st == "down"):
                    y = (y+72)
                    
                if (st == "left"):
                    x = (x-75)
                    
                if (st == "right"):
                    x = (x+75)
                try:    
                #(b - y)=(((redy - y)/(redx - x))(a-x))
                # b =  (((redy - y)/(redx - x))(a-x)) + y
                # a = ((b - y)((redx - x)/(redy - y)))+ x
                 x1 = ((36 - y)*((redx - x)/(redy - y)))+ x
                 x2 = ((564 - y)*((redx - x)/(redy - y)))+ x
                 y1 = (((redy - y)/(redx - x))*(37-x)) + y
                 y2 = (((redy - y)/(redx - x))*(437-x)) + y
                 if (36 < x1 < 438):
                    points.append((x1,36))
                 if (36 < x2 < 438):
                    points.append((x2,564))
                 if (25 < y1 < 565):
                    points.append((37,y1))
                 if (25 < y2 < 565):
                    points.append((437,y2))
                 print(points,x1,x2,y1,y2,redx,redy,x,y)   
                 for i in points:
                    dista = math.sqrt((i[0] - x)**2 + (i[1] - y)**2)
                    ddis[i] = dista
                 fddis = sorted(ddis.values())    
                 fp = [key for key , value in ddis.iteritems() if value == fddis[0]][0]    
                 longx = (self.x - fp[0])
                 longy = (self.y - fp[1])

                except ZeroDivisionError:
                    if (redx - x > 0):
                        longx = (self.x - 37)
                        longy = (self.y - redy)
                    if (redx - x < 0):
                        longx = (self.x - 437)
                        longy = (self.y - redy)
                    if (redy - y < 0):
                        longx = (self.x - redx)
                        longy = (self.y - 564)
                    if (redy - y > 0):
                        longx = (self.x - redx)
                        longy = (self.y - 36)
                    else:
                        longx = (self.x - (random.choice(xconstants))[0])
                        longy = (self.x - (random.choice(xconstants))[1])
                except IndexError:
                        longx = (self.x - (random.choice(xconstants))[0])
                        longy = (self.x - (random.choice(xconstants))[1])
                    
                if self.color != (255,255,255): 
                

                 if ((longx > 0) & (longy > 0)):
                    if (("left" in dire) & ("up" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","left"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("right" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                      
                if self.color == (255,255,255):
                 if ((longx > 0) & (longy > 0)):
                    if (("right" in dire) & ("down" in dire)):
                        print(1)
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","right"))
                    if (("right" in dire) & ("down" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("down" in dire)):
                        self.direction = "down"
                 if ((longx < 0) & (longy > 0)):
                    print(2)
                    if (("left" in dire) & ("down" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "down"
                        else :
                            self.direction = random.choice(("down","left"))
                    if (("left" in dire) & ("down" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("down" in dire)):
                        self.direction = "down"    
            

                 if ((longx > 0) & (longy < 0)):
                    print(3)
                    if (("right" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "right"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("up","right"))
                    if (("right" in dire) & ("up" not in dire)):
                        self.direction = "right"
                    if (("right" not in dire) & ("up" in dire)):
                        self.direction = "up"
                 if ((longx < 0) & (longy < 0)):
                    print(4)
                    if (("left" in dire) & ("up" in dire)):
                        if (max(longx,longy) == longx):
                            self.direction = "left"
                        if (max(longx,longy) == longy):
                            self.direction = "up"
                        else :
                            self.direction = random.choice(("left","up"))
                    if (("left" in dire) & ("up" not in dire)):
                        self.direction = "left"
                    if (("left" not in dire) & ("up" in dire)):
                        self.direction = "up"
                        
                 if ((longx == 0) & (longy != 0)):
                    print(5)
                    if (longy > 0):
                        if "down" in dire:
                            self.direction = "down"
                        else:
                            self.direction == random.choice(dire)
                    if (longy < 0):
                        if "up" in dire:
                            self.direction = "up"
                        else:
                            self.direction == random.choice(dire) 

                 if ((longx != 0) & (longy == 0)):
                    print(6)
                    if (longx > 0):
                        if "right" in dire:
                            self.direction = "right"
                        else:
                            self.direction == random.choice(dire)
                    if (longx < 0):
                        if "left" in dire:
                            self.direction = "left"
                        else:
                            self.direction == random.choice(dire)
                      

                            
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


cconstants = copy.copy(xconstants)
#print(cconstants)
node(xconstants)
o1 = pachero()
g1 = sbluegost((0,255,255))
g2 = redgost((255,51,51))
g3 = bluegost((51,51,255))
g4 = greengost((51,255,51))
fimage = pygame.image.load("fruit.gif").convert()
boole = True
bye = [False,False,False,False]
while boole:
    screen.blit(image,(0,0))
    screen.blit(font.render("score = "+str(score),True,(255,255,255)),(0,0))
    if (o1.x,o1.y) in cconstants:
        pellet.play()
        score = score + 10
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
                bye[0] = True
                
            if event.key == pygame.K_UP:
                bye[1] = True
                
            if event.key == pygame.K_LEFT:
                bye[2] = True
                
            if event.key == pygame.K_RIGHT:
                bye[3] = True
                

                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                bye[0] = False
                
            if event.key == pygame.K_UP:
                bye[1] = False
                
            if event.key == pygame.K_LEFT:
                bye[2] = False
                
            if event.key == pygame.K_RIGHT:
                bye[3] = False
                

    if (bye[0] == True):
            o1.direction = "down"
    if (bye[1] == True):
            o1.direction = "up"
    if (bye[2] == True):
            o1.direction = "left"
    if (bye[3] == True):
            o1.direction = "right"
            
    o1.movement()
    if (g1.state == 1)|(g2.state == 1)|(g3.state == 1)|(g4.state == 1):
        score = 0
        extralife.play()
        o1.x = 212
        o1.y = 564
    g1.movement(o1.x,o1.y,o1.time2)
    g2.movement(o1.x,o1.y,o1.time2)
    g3.movement(o1.x,o1.y,o1.time2,g2.x,g2.y,o1.olddirect)
    g4.movement(o1.x,o1.y,o1.time2,o1.olddirect)
   
    pygame.display.update()
pygame.display.quit()
