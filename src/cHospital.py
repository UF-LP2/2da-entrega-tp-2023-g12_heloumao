import cPaciente
import cEnfermero
import random
from binarytree import build
import binarytree


class cHospital:
    def __init__(self, name:str, patients: [], nurses:[]):
        self.name=name
        self.patients=patients
        self.nurses=nurses


    def crearArbol()->binarytree:
        nodes=[14,12,16,10,13,15,17,8,11,None, None, None, None,None, None,6,9,None,None,4,7,None, None, 2,5,None,None, 1,3,None,None]
        binary_tree=build(nodes)
        return binary_tree
    
    def shifts():
        x=random.randrange(23)
        if x<23 and x>=16:
            return 3
        elif x>=10 and x<16:
            return 5
        elif x>=6 and x<10:
            return 2
        else:
            return 1
    
    #def register (pac:cPaciente, pacientes:list(cPaciente), urgents:list(cPaciente))->list(cPaciente):  #LO TENEMOS QUE ARMAR CON EL RECORRIDO DEL ARBOL 

    def mergeQueues(pacientes: [], urgents:[])->list(cPaciente):
        return (urgents+ pacientes)


    def rearrange(pacientes: []) ->list(cPaciente):#MERGE SORT
        if len(pacientes)==1:
            return pacientes
        else:
            mid=len(pacientes)//2
            half1=pacientes[:mid]
            half2=pacientes[mid:]

            array1 = rearrange(half1)
            array2 = rearrange(half2)

            i=j=k=0

            while i<len(array1) and j<len(array2):  
                if array1.GET_LEFT_TIME() < array2[j].GET_LEFT_TIME():  #mando al que menos tiempo le queda
                    pacientes[k]= array1[i]
                    i+=1
                elif array1.GET_LEFT_TIME() > array2[j].GET_LEFT_TIME():
                    pacientes[k]= array2[j]
                    j+=1
                else: #les queda  a los dos el mismo tiempo
                    if array1[i].GET_PRIORITY() and array2[j].GET_PRIORITY() or not(array1[i].GET_PRIORITY()) and not(array2[j].GET_PRIORITY()):
                        #cuando les queda el mismo tiempo de espera y ambos o ninguno es prioritario (not(nor)); entonces clasifico por edad
                        if array1[i].GET_EDAD() < array2[j].GET_EDAD():
                                pacientes[k]=array2[j]  #el mayor va a ser atendido primero
                                j+=1
                        else:
                            pacientes[k]=array1[i]
                            i+=1
                    elif array1[i].GET_PRIORITARIO():   #si array1 es prioritario
                        pacientes[k]=array1[i]
                        i+=1
                    else:   #si array2 es prioritario
                        pacientes[k]=array2[j]
                        j+=1
            
            #una vez ordenado completo con array 1 si el mientras terminó por el array 2; y completo el array 2 si el moientras terminó por array 1 
            while i< len(array1):
                pacientes[k]=array1[i]
                i+=1
                k+=1
            while j< len(array2):
                pacientes[k]=array2[j]
                j+=1
                k+=1

                return pacientes
    

    def urgents(urgents:list(cPaciente)) -> list (cPaciente):  #INSERTION SORT
        for i in range(1,len(urgents),1):
            j=i-1
            current= urgents[i]
            while j>=0 and urgents[j].GET_EDAD()>current.GET_EDAD():
                urgents[j+1]= urgents[j]
                j=j-1
            urgents[j+1]=current
        return urgents





