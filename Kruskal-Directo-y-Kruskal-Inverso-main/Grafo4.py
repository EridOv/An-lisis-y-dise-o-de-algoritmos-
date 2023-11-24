'''
Created on 27 jun. 2021

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
from Arista4  import aristasMalla, aristaErdosRenyi , aristaBarbasi,\
    aristasDorogobsev, aristasGeografico, aristasGilbert
from Nodo4 import nuevoN
from test.pydoc_mod import nodoc_func
from dis import dis
from regex._regex_core import V0
from copy import copy
from platform import dist


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
        

        def Kruskal(self, i):###Kruscal directo
            ######Se inicializa:
            distancias={}
            camino=[]
            U=[]
            V=[]
            #####El primer paso es acomodar las distancias y las aristas 
            for j in range (len(self.aristas)):
                x=(self.aristas[j]); a=int(x[0]); b=int(x[1])  # se guarda distancia: arista
                distancias[(random.uniform(0,5))]=[(a, b)]
            ####El segundo paso es comparar 
            while len(distancias)!=0:
                Aristamin=min(distancias)
                x=distancias[Aristamin]
                x1=x[0]
                u=x1[0]
                v=x1[1]
                if ((u not in V or v not in U) and v not in V) or ((u in V and v in U) and v not in V): # SÍ U NO SE ENCUENTRA EN EL CONJUNTO V LO GUARDAMOS COMO ARISTA PRIMARIA 
                    camino.append((u,v,Aristamin))
                    U.append(u)
                    V.append(v)
                    del distancias[Aristamin]
                else: del distancias[Aristamin]
            
            print('camino kruskal xxxxxxx', camino)
            
            
        def Kruskali (self, i):### Kruskal inverso 
            distancias={}
            camino={}
            caminoList=[]
            U=[]
            V=[]
            #####El primer paso es acomodar las distancias asignadas aleatoriamente a la lista de aristas 
            for j in range (len(self.aristas)):
                x=(self.aristas[j]); a=int(x[0]); b=int(x[1])  # se guarda distancia: c/arista
                distancias[(random.uniform(0,5))]=[(a, b)]
                U.append(a)
                V.append(b)
            camino=dict(distancias)
            ####El segundo paso es comparar 
            while len(distancias)!=0:
                Aristamax=max(distancias)
                x=camino[Aristamax]
                x1=x[0]
                u=x1[0]
                v=x1[1]
                del distancias[Aristamax]
                U.pop(U.index(u))
                V.pop(V.index(v))
                if v in V: # PARA QUE NO SE FORMEN CICLOS v NO SE PUEDE REPETIR EN V 
                    del camino[Aristamax]
                else:
                    caminoList.append((u,v,Aristamax)) #se gurardan las aristas
                    
            print('CAMINO kruskal inverso', caminoList)
            
        def Prim(self, i ): 
            ####inicializamos 
            distancias={} 
            camino=[]
            V=[]
            Visitados=[]
            
            k=0; j=0
            for o in range  (1,len(self.nodos)+1):
                distancias[o]=[]
            #####El primer paso es acomodar las distancias asignadas aleatoriamente a la lista de aristas
            while (len(self.aristas))>0:
                x=self.aristas[k]
                a=int(x[0]);b=int(x[1]);c=(random.uniform(0,5))
                V.append(a)
                
                distancias[a].append((b,c))
                self.aristas.pop(k)
                j=j+1;
            
            longaux=[]; n=0
            while len(distancias)>0: # el segundo paso es ir chechando que no se formen ciclos 
                p=V[n] 
                if p in distancias and len(distancias[p])!=0:               
                    w=distancias[p]
                    for l in range(len(distancias[p])):
                        w1=w[l]
                        lon=w1[1]
                        longaux.append(lon)
                    MIN=min(longaux); ### obtenemos el minimo del vector de de distancias del nodo que estamos explorando. 
                    indxMIN=longaux.index(MIN)
                    minx=w[indxMIN]
                    u=p; v=minx[0]
                    
                    if v not in Visitados: 
                        camino.append((u, v, MIN))
                        Visitados.append(v)
                        w.pop(indxMIN)
                    else:
                        w.pop(indxMIN)
                    longaux.clear()
                    if n<len(V):n=n+1
                    else: n=0
                    
                else:
                    if p in distancias:
                        del distancias[p] 
                        V.pop(V.index(p)) 
                    if n<len(V)+1:p=p+1
                    else: n=0
            
                print(camino)
                print(Visitados)
                
                
                    
                
                
                
                
                
            
            
            
                
                    
                    

            
                       
                    
                
                        
                        
                    
                        
                
                    
                    
                    
                
                    
                
                
                
                
                
            
            
        
            
            
                    
            
            
                
       
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
a.malla(4, 2, True) 
#a.gilbert(100, .30, False)
#a.erdosRenyi(100,200,False)
#a.geografico(30, 2, True)
#a.Barabasi(100, 3, False)
#a.DorogobsevM(30, False)D
a.Prim(1)
#a.saveRecursivo()
