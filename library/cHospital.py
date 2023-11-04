from src.cPaciente import cPaciente
import library.cEnfermero as cEnfermero
import random
import binarytree
from binarytree import build
import datetime
from datetime import now
from src.archivos import readNurse
from src.archivos import register

class cHospital:
    def __init__(self, name:str, patients= None, nursesOnCall=None):  #ctor
        self.name=name
        self.patients=patients
        self.nurses=readNurse()
        self.nursesOnCall=nursesOnCall
    
    def shifts(self):   #segun la hora determino cuantos enfermeros están de turno
        x = datetime.datetime.now()
        if x.hour()<23 and x.hour()>=16:
            return 3
        elif x.hour()>=10 and x.hour()<16:
            return 5
        elif x.hour()>=6 and x.hoour()<10:
            return 2
        else:
            return 1
    
    def defineShift(self)->str:
        x = datetime.datetime.now()
        shiftaux =""
        if x.hour()<23 and x.hour()>=16:
            shiftaux= "evening"
        elif x.hour()>=10 and x.hour()<16:
            shiftaux= "rush hour"
        elif x.hour()>=6 and x.hoour()<10:
            shiftaux= "morning"
        else:
            return "night"
        
    def GET_NURSE_ONCALL(self)->list(cEnfermero):
        shiftaux=self.defineShift()
        retorno = []
        for x in self.nurses():
            if x.shift== shiftaux:
                retorno.append(x)
        return retorno

    #segun la hora del día voy a completar mi lista de enfermeros que estan de tuno de manera aleatoria
    def nursesONCALL(self)->None:
        aux = self.shifts()
        cant=self.GET_NURSES_ONCALL()
        for i in range(aux):
            x=random.randrange(cant)
            self.nursesOnCall.append(self.nurses[x])
    

    def mergeQueues(self,pacientes: [], urgents:[])->list(cPaciente):
        return (urgents + pacientes)


    def rearange(self,pacientes: []) ->list(cPaciente):#MERGE SORT
        if len(pacientes)==1:
            return pacientes
        else:
            mid=len(pacientes)//2
            half1=pacientes[:mid]
            half2=pacientes[mid:]

            array1 = self.rearange(half1)
            array2 = self.rearange(half2)

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
    
   
   #pacientes que bajo del archivo para que sean atendidos por color segun canatidad de enfermeros
    def GET_PATIENTS(self)->list(cPaciente):
        cantidad=len(self.nursesOnCall)*2
        i=0
        while i < cantidad:
            self.patients.append()
        register(self.patients)

  
    #con los enfermeros del archivo de pacientes total voy a bajar esa cantidad de pacientes 
    def urgents(self,urgents:list(cPaciente)) -> list (cPaciente):  #INSERTION SORT
        for i in range(1,len(urgents),1):
            j=i-1
            current= urgents[i]
            while j>=0 and urgents[j].GET_EDAD()>current.GET_EDAD():
                urgents[j+1]= urgents[j]
                j=j-1
            urgents[j+1]=current
        return urgents





