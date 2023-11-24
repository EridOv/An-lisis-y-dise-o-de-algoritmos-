'''
Created on 9 abr. 2021

@author: erido
'''
import csv

class Nodo(object):
    N={}
def nuevoN(n):
    i=1
    for i in range(1,n+1):
        a=str(i)
        Nodo.N[a,]=[]      
    
    nodos=list(Nodo.N)
    with open("listNodos.csv", "w") as fichero:
        writer = csv.writer(fichero)
        writer.writerow(['Id'])
        writer.writerows(nodos)     






    
    
        



