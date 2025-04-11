import pygame
import sys 
# espacios para variables
color1 = (16, 244, 234)
color2 =(130, 244, 16)
color3 =(255, 0, 0)
color4 = (174, 16, 16)
color5 =(235, 16, 16)
color6 =(212, 175, 55)
color7 =(0,0,0)
color6_1 = (200, 175, 20)
color8 = (200, 197, 185)
color9 = (255, 247, 0)
blanco= (255,255,255)
color10=(46, 28, 28)
verde =(0,255,0)
cafe = (172, 116, 23)
pygame.init()

ventana = pygame.display.set_mode((600,600))
pygame.display.set_caption("tren")
clock = pygame.time.Clock()
XX = -100 
MOVIMIENTO = 2
xx2 = -20 
MOVIMIENTO2 = 1
while 1:
    clock.tick(50)

    for event in pygame.event.get():
        if  event.type ==pygame.QUIT:
            sys.exit()
    ventana.fill(color1)
    XX = XX + MOVIMIENTO 

    if XX >= 650:
        XX = -100
        MOVIMIENTO = 2
    elif XX<= -10:
        XX = 2
       
    xx2 = xx2 + MOVIMIENTO2 

    if xx2 >= 700:
        xx2 = -100
        MOVIMIENTO2 = 2
    elif xx2<= -100:
        xx2 = 2
    #terreno
    
    puntosmontaña = [(-100,355),(100,50),(200,350)]
    pygame.draw.polygon(ventana,cafe,puntosmontaña)
    puntosmontaña = [(100,435),(200,150),(300,350)]
    pygame.draw.polygon(ventana,cafe,puntosmontaña)
    pygame.draw.rect(ventana,cafe,(200,250,500,200))


    pygame.draw.rect(ventana,color2,(0,350,600,500))
    #tren
    pygame.draw.rect(ventana,color4,(290,220,100,80))
    pygame.draw.rect(ventana,color5,(300,230,80,60))
    pygame.draw.rect(ventana,color5,(190,240,40,60))
    pygame.draw.rect(ventana,color6,(185,250,50,20))
    pygame.draw.rect(ventana,color6,(185,220,50,20))
    pygame.draw.circle(ventana,color6,(140,350),40)
    pygame.draw.rect(ventana,color3,(150,300,250,100))
    pygame.draw.rect(ventana,color6_1,(135,300,20,100))
    pygame.draw.rect(ventana,color6_1,(125,290,20,120))
    pygame.draw.rect(ventana,color6_1,(285,200,110,20))
    pygame.draw.rect(ventana,color6_1,(300,180,80,20))
    #las llantas
    ##llanta 1
    pygame.draw.circle(ventana,color8,(340,390),40)
    pygame.draw.circle(ventana,color7,(340,390),20)
    #llanta2
    pygame.draw.circle(ventana,color8,(250,400),30)
    pygame.draw.circle(ventana,color7,(250,400),10)
    #llanta3
    pygame.draw.circle(ventana,color8,(180,400),30)
    pygame.draw.circle(ventana,color7,(180,400),10)
    #la carita
    pygame.draw.circle(ventana,color9,(340,260),40)
    #ojo izq
    pygame.draw.circle(ventana,blanco,(325,250),10)
    pygame.draw.circle(ventana,verde,(325,250),5)
    #ojo der
    pygame.draw.circle(ventana,blanco,(355,250),10)
    pygame.draw.circle(ventana,verde,(355,250),5)
    #la boca
    pygame.draw.circle(ventana,color10,(340,280),10)
    
    # animar las nbes
    for i in range(100):
        pygame.draw.ellipse(ventana,blanco,(XX,50,100,10))
        pygame.draw.ellipse(ventana,blanco,(XX,100,200,20))
        pygame.draw.ellipse(ventana,blanco,(xx2,75,40,20))
        pygame.draw.ellipse(ventana,blanco,(xx2,34,200,20))
    pygame.display.flip()
    