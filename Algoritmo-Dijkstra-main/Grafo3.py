'''
Created on 20 jun. 2021

@author: erido
'''

import csv

from numpy.random.mtrand import randint, uniform
from random import randrange
from numpy import random, int0, append
from cmath import sqrt
from xmlrpc.client import boolean
from pickle import TRUE
from turtledemo.penrose import star
from _tracemalloc import start
from distutils.command.clean import clean
from _operator import index
from Arista3  import aristasMalla, aristaErdosRenyi , aristaBarbasi,\
    aristasDorogobsev, aristasGeografico, aristasGilbert
from Nodo3 import nuevoN
from test.pydoc_mod import nodoc_func
from dis import dis
from regex._regex_core import V0


class Grafo3():
        nodos=[]
        aristas={}
        arbol={}
        x={}            
        y={}
        Visitados=[]
        
####### G E N E R A D O R E S    D E  G R A F O S        
        def malla(self,n,m,dirigido):#n es el numero de nodos a lo largo y m a lo ancho para un arreglo rectangular 
            lim=n*m
            self.nodos=nuevoN(lim)
            self.aristas= aristasMalla(lim,n, dirigido)
            self.aristas=list(self.aristas)
            with open("listAristasMalla500nodos.csv", "w") as fichero:
                writer = csv.writer(fichero)
                if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
                if dirigido==False:writer.writerow(['Source', 'Target'])
                writer.writerows(self.aristas)         
            return self.aristas
        
        def erdosRenyi(self, n,m, dirigido):#n=numero de nodos m= numero de aristas aleatorias  
            self.nodos=nuevoN(n)
            self.aristas= aristaErdosRenyi(n,m, dirigido )     
            self.aristas=list(self.aristas)   
            with open("listAristasErdosRenyi30Nodos.csv", "w") as fichero:
                writer = csv.writer(fichero)
                if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
                if dirigido==False:writer.writerow(['Source', 'Target'])
                writer.writerows(self.aristas) 
            return self.aristas      

        def gilbert(self,n,p, dirigido=boolean):# n es numero de nodos, p es la probabilidad 
            self.nodos=nuevoN(n)
            self.aristas= aristasGilbert(n,p,dirigido)        
            self.aristas=list(self.aristas)    
            with open("listAristasGilbert100nodos.csv", "w") as fichero:
                writer = csv.writer(fichero)
                if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
                if dirigido==False:writer.writerow(['Source', 'Target'])
                writer.writerows(self.aristas) 
            return self.aristas
    
        def geografico(self,n,r, dirigido= boolean):
            self.nodos=nuevoN(n)
            self.aristas= aristasGeografico(n,r,dirigido)
            self.aristas=list(self.aristas)    
            with open("listAristasGeografico500Nodos.csv", "w") as fichero:
                writer = csv.writer(fichero)
                if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
                if dirigido==False:writer.writerow(['Source', 'Target'])
                writer.writerows(self.aristas) 
            return self.aristas

        def Barabasi(self,n,g, dirigido=boolean):
            self.nodos=nuevoN(n)
            Grafo2.aristas=aristaBarbasi(n,g)            
            self.aristas=list(self.aristas)    
            with open("listAristasBarabasi500nodos.csv", "w") as fichero:
                writer = csv.writer(fichero)
                if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
                if dirigido==False:writer.writerow(['Source', 'Target'])
                writer.writerows(self.aristas) 
            return self.aristas

        def DorogobsevM(self,n, dirigido=boolean): #n es igual al numero de nodos 
            self.nodos=nuevoN(n)
            self.aristas=aristasDorogobsev(n, dirigido)
            self.aristas=list(self.aristas)    
            with open("listAristasDorogobsev500nodos.csv", "w") as fichero:
                writer = csv.writer(fichero)
                if dirigido==True:writer.writerow(['Source', 'Target', 'Type'])
                if dirigido==False:writer.writerow(['Source', 'Target'])
                writer.writerows(self.aristas) 
            return self.aristas
        

        
        def dijkstra(self, S): 
            distCopy={}
            length=[] # lista de distancias en el orden de las aristas ej. aristas=[(e1,e2), (e3, e4)] y length=[d1, d2]
            distancias={}
            copia_aristas=self.aristas #copia de las aristas
            newaristas={} # diccionario con donde {nodo1: [(nodo2, distancia)...]
            camino={}
            visitados=[]
            
            
            #########se modifica la forma en que guardamos la información
            for n in  range(1,len(self.nodos)+1): # inicializamos arreglo de distancias 
                distancias[n]=10000
            distancias[S]=0
                    
            #Generar lista de distancias aleatorias para cada arista
            for i in range(0, len(self.nodos)):
                newaristas[i]=[] #generar key en el diccionario para cada nodo declarando una lista para las tuplas
                camino[i]=[]
            
            for i2 in range (len(self.aristas)):    
                length.append(random.uniform(0,5)) 
                
            k=0;j=0
            newaristas.pop(0)
            while (len(self.aristas))>0:
                x=self.aristas[k]
                a=int(x[0]);b=int(x[1]);c=length[j]
                newaristas[a].append((b,c))
                self.aristas.pop(k)
                j=j+1;
            dist0=dict(newaristas)    
            
               
            v0=S;# Comenzamos a explorar con el nodo fuente             
            
            while  len(newaristas)!=0:                
                #genero el vector de todas las distancias de las aristas que se forman a partir de e0
                if len(newaristas[v0])+1>0:
                    d=newaristas[v0]
                    
                    for  i in range (0,len(newaristas[v0])):
                        d1=d[i]
                        d2=d1[1]                #( d1[0]=v1, d1[1]=distancia)       
                        dist=d2+distancias[v0]  # d(v1)=d(v0)+l(v0,v1)
                        
                        if distancias[d1[0]]>=dist:
                            for j in range(1,len(camino)):
                                if d1[0] in camino[j]:
                                    camino[j].pop(camino[j].index(d1[0]))
 
                            camino[v0].append(d1[0])#se seleccióna la distancia mínima
                            distancias[d1[0]]=dist

                    newaristas.pop(v0)
                    visitados.append(v0)
                    distCopy=dict(distancias)
                    for m in range(len(distCopy)):
                        w=min(distCopy.items(), key=lambda x:x[1])
                        w=w[0]
                    
                        if w not in visitados:
                            v0=w
                            break
                        else: 
                            distCopy.pop(w)
                    #seleccionar y guardar 
                    
                    
                else: 
                    newaristas.pop(v0); #(print('elimino'))
                    visitados.append(v0)
                    distCopy=dict(distancias)
                    for m in range(len(distCopy)):
                        w=min(distCopy.items(), key=lambda x:x[1])
                        w=w[0]
                        if w not in visitados:
                            v0=w
                            break
                        else: 
                            distCopy.pop(w)
                            #OBTENGO LA DISTANCIA MINIMA 
                aristasArbol=[]
                i=0
                while i<len(camino.values()):
                    if len(camino[i])>0:
                        for j in range (len(camino[i])):
                            x=(camino[i])
                            print(x)
                            a=x; b=x[j]
                            print(b)
                            print(dist0)
                            #d=dist0[i]
                            #d.index[]
                            for l in range (len(dist0[i])):
                                e=dist0[i]
                                e1=e[l]
                                if e1[0]==b: d=e1[1]
                            aristasArbol. append((i, b, d))           
                    i=i+1    
                    print("arbol de aristas", aristasArbol)         
                    print("distancias generales", distancias)
                    print("camino")
                 
                       
                    
                
                        
                        
                    
                        
                
                    
                    
                    
                
                    
                
                
                
                
                
            
            
        
            
            
                    
            
            
                
       
#otras funciones                                               
def lista(x):
    new=[];aristas=x
    
    for i in range(0, len(aristas)+1):
                if i== 0: new.append(0)
                else: 
                    original=aristas[i-1]
                    new.append(int(original[0]))
                    new.append(int(original[1])) 
    return new  



a=Grafo3()
a.malla(3, 3, True)
#a.gilbert(100, .30, False)
#a.erdosRenyi(100,200,False)
#a.geografico(30, 2, True)
#a.Barabasi(100, 3, False)
#a.DorogobsevM(30, False)D
a.dijkstra(1)
#a.saveRecursivo()
