'''
Created on 28 jun. 2021

@author: erido
'''
from pygame._sprite import pygame
from matplotlib.pyplot import spring
from pygame.examples.sprite_texture import win
from numpy import sqrt
from platform import dist
from cmath import log, log10
from _ast import While
from numpy.distutils.log import Log
from numpy.polynomial.tests.test_classes import random

####Primero se inicializan las variables para la ventana
x=1500; 
y=300
ventana=pygame.display.set_mode(x, y)

MinDiametro=30
MinDiametro2=30

MaxDiametro=50
MaxDiametro=50
##### Asignamos valores a las variables del algoritmo:
c1=2
c2=1
c3=1
c4=0.1
n=9 ####numero de nodos|vertices del grafo 
D=min(x, y)/n
radio=50


def IDistancias(self, G): # Se genera un arreglo con las distancias 
    Distancias=[]
    XY={}
    for j in range (G.nodos):
        x=G.aristas[j]
        a=x[0]
        b=x[1]
        Y=(random.uniform(250,1250))
        X=(random.uniform(50,250))
        XY[j]=(X,Y)
        Distancias.append((a, b,))
    return Distancias, XY

i=0
def spring(self, G):
    reloj=pygame.time.Clock()
    [V, XY]=IDistancias(G)
    M=1000
    XA=0
    YA=0    
        
    while i<M:     
        for l in range (len(V)):
            w=V[l]
            a=w[1]; b=w[2]
            ax=(XY[a])[0]
            ay=(XY[a])[1]
            bx=(XY[b])[0]
            by=(XY[b])[1]
            
            d=sqrt((bx-ax)**2-(by-bx)**2)
            fa=c1*log(d/c2)
            fr=c3/sqrt(d)
            
            ##actualizar coordenas 
            R=c3/sqrt(d)
            A=c1*Log(d/c2)
            
        
         pygame.draw.circle((0,0,0), (100,100,100), (ax, ay), radio)
        pygame.draw.circle((0,0,0), (100,100,100), (bx, by), radio)
        pygame.draw.line((0,0,0), (100,100,100), (ax,ay), (bx, by))
  
        
        clock.tick(60)
            
        pygame.display.update()
        if i==1000: pygame.quit()
        i=i+1
    
    

    



