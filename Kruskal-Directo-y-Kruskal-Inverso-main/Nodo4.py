'''
Created on 27 jun. 2021

@author: erido
'''

import csv

class Nodo2(object):
    N={}
 
def nuevoN(n):
    i=1
    for i in range(1,n+1):
        a=str(i)
        Nodo2.N[a,]=[]      
    
    nodos=list(Nodo2.N)
    with open("listNodos.csv", "w") as fichero:
        writer = csv.writer(fichero)
        writer.writerow(['Id'])
        writer.writerows(nodos)  
    return nodos    