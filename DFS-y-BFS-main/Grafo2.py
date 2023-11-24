'''
Created on 27 abr. 2021

@author: erido
'''

import csv

from numpy.random.mtrand import randint
from random import randrange
from numpy import random, int0, append
from cmath import sqrt
from xmlrpc.client import boolean
from pickle import TRUE
from turtledemo.penrose import star
from _tracemalloc import start
from distutils.command.clean import clean
from _operator import index
from Arista2  import aristasMalla, aristaErdosRenyi , aristaBarbasi,\
    aristasDorogobsev, aristasGeografico, aristasGilbert
from Nodo2 import nuevoN
from test.pydoc_mod import nodoc_func


class Grafo2():
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
        

## A L G O R I T M O S   P R O Y E C T O 2
        def bfs(self, x):# Busqueda a lo ancho 
            Todos=[];vecinos=[]; i=1  #pila de nodos reconocidos 
            vecinos.append(x) 
            new=lista(self.aristas) #lista de coordenadas 
            while True:
                x=vecinos[0]
                if (x in new)==True: 
                    while i<len(new)-1:
                        num=int(new[i])
                        if num==x:
                            if i%2!=0:i2=i+1
                            if i%2==0:i2=i-1
                            a=new[i]; b=new[i2]; vecinos.append(b);
                            a=str(a);b=str(b)
                            if b not in Todos:Todos.append(b);self.arbol[a,b,]=[]
                            if i>i2:
                                new.pop(i2)
                                new.pop(i2)
                            else:
                                new.pop(i)
                                new.pop(i)
                            i=i-1
                        i=i+1
                if len(vecinos)>0 & x not in new:
                    if(len(new)>0): 
                        n=randrange(1,len(new))
                        vecinos.append(new[n])
                vecinos.pop(0);i=1
                if len(vecinos)==0:break    
            with open("bfsMalla30.csv", "w") as fichero:
                    writer = csv.writer(fichero)
                    writer.writerow(['Source', 'Target'])
                    writer.writerows(self.arbol) 
            
        def dfsit(self, n0):# Bunqueda en lo profundo metodo iterativo 
            camino=[]; Todos=[]; #cola 
            n0=int(n0) #nodo iniciador
            new=lista(self.aristas) 
            camino.append(n0)
            i=1;         
            
            while len(camino)>0 and len(new)>0:#Se busca el primer camino      
                num=int(new[i])             
                if num==camino[-1]:
                    a=new[i]; b=new[i+1];  
                    if b not in Todos:
                        camino.append(b)
                        Todos.append(b);self.arbol[a,b,]=[]; print('se guarda', a, b);
                    new.pop(i)
                    new.pop(i)
                    if i>=len(new):
                        i=i-2 
                        print("hola1")
                    
                        
                else:
                    print('holi')
                    if i<len(new)-2:i=i+2
                    else: i=1; camino.pop()

      
            print(self.arbol)
            with open("dfsiterativoMalla30.csv", "w") as fichero:
                    writer = csv.writer(fichero)
                    writer.writerow(['Source', 'Target'])
                    writer.writerows(self.arbol) 
            
        def dfsrec1(self, x): #Busqueda en lo profundo recursivo 
            
            i=0
            dict(self.aristas)
            while i<=len(self.aristas)-1:
                arista=self.aristas[i]
                a=int(arista[0]); b=int(arista[1]) 
                if a==x: 
                    self.arbol[a,b,]=[]
                 
                    self.aristas.pop(i)
                    self.dfsrec1(b)
                    i=0
                else: i=i+1
            
            
                    
        def saveRecursivo(self):
            with open("bfsrecursivomalla30.csv", "w") as fichero:
                    writer = csv.writer(fichero)
                    writer.writerow(['Source', 'Target'])
                    writer.writerows(self.arbol) 
            
            
        def Gv(self):
            lista1= ['graph name {']
            lista2= self.nodos
            lista3= self.aristas
            Gv=lista1+ lista2+ lista3
            
            print(Gv)

            
            
                    
            
            
                
       
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
