import pygame 
from Pelota import Pelota 
from colores import COLOR

pygame.init()

# se le da en ancho y el alto en una lista 
screen = pygame.display.set_mode([800,600])

pelota=Pelota(screen,200,200,20,COLOR.WHITE,1,-1)

# parametros del rectangulo
anchorect=200
altorect=100
dxrect=1
dyrect=1

font = pygame.font.SysFont('arial', 32)
text = font.render('PELIGRO EPILEPSIA ', True, COLOR.ORANGE, COLOR.WHITE)
textRect = text.get_rect()

bContinua = True
while bContinua:
  
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            bContinua = False
            screen.fill(COLOR.BLACK)
            print("Cerrando")

    screen.fill(COLOR.BLUE)
    
    screen.blit(text, textRect)  # Agrega texto
         
    #pygame.draw.rect(screen,COLOR.sRed,[100-3,100+6,anchorect,altorect],0)
    #pygame.draw.rect(screen,COLOR.RED,[100,100,anchorect,altorect],0)
    #rect(obj,color,[xpos,ypox,dx,dy])

    pelota.updatePelota()
    pygame.time.delay(5)   # delay(ms)
    pygame.display.update()
    
pygame.quit()
