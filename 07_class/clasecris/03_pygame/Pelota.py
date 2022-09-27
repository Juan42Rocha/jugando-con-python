import pygame
from colores import COLOR

class Pelota:
    def __init__(self,screen,posx,posy,radio,color,velx,vely):
        self.screen=screen
        self.w=pygame.display.Info().current_w
        self.h=pygame.display.Info().current_h
        
        self.posx=posx
        self.posy=posy
        self.radio=radio
        self.color=color
        self.velx=velx
        self.vely=vely

    def updatePelota(self):
        self.ViveVIVE()
        self.colisiones()
        self.cambiacolor()
        
        pygame.draw.circle(self.screen,self.color,[self.posx,self.posy],self.radio,0)
    #   pygame.draw.circle(screen,colorcirc,[poscircx,poscircy],radiocirc,0)
    #circle(obj,color,[xpos,ypos],radio, saturacion)

    def ViveVIVE(self):
        self.posx+=self.velx
        self.posy+=self.vely

    def colisiones(self):
        if self.posx >= self.w-self.radio:
            self.velx=-1
        elif self.posx <= 0+self.radio:
            self.velx=1
        elif self.posy >= self.h-self.radio:
            self.vely=-1
        elif self.posy <= 0+self.radio:
            self.vely=1

    def cambiacolor(self):
        if( (self.posx >= self.w-self.radio) or (self.posx <= 0+self.radio)or(self.posy >= self.w-self.radio)or(self.posy <= 0+self.radio)):
            self.color= COLOR.RandomColorVb()
