from src.cPaciente import cPaciente
from src.cPaciente import remainingTime
from src.cPaciente import timeIncrement
import library.cEnfermero as cEnfermero
from library.cEnfermero import createTag
import random
import binarytree
from binarytree import build
import datetime
from datetime import now
from src.archivos import readNurse
from src.archivos import register
from src.archivos import readPatient

class cHospital:
    def __init__(self, name:str, patients= None, nursesOnCall=None):  #ctor
        self.name=name
        self.patients=patients  #pacientes en standby
        self.nurses=readNurse()
        self.nursesOnCall=nursesOnCall
        self.atendidos = 0 #cantidad de pacientes atenidos
    
    def cantEnfermeros(self, x:int):   #segun la hora determino cuantos enfermeros están de turno
        if x<23 and x>=16:
            return 3
        elif x>=10 and x<16:
            return 5
        elif x>=6 and x<10:
            return 2
        else:
            return 1
    
    def defineShift(self,x:int)->str:
        shiftaux =""
        if x<23 and x>=16:
            shiftaux= "evening"
        elif x>=10 and x<16:
            shiftaux= "rush hour"
        elif x>=6 and x<10:
            shiftaux= "morning"
        else:
            return "night"
        
    def GET_NURSE_ONCALL(self,x:int)->list(cEnfermero):
        shiftaux=self.defineShift(x)
        retorno = []
        for j in self.nurses():
            if j.shift()== shiftaux:
                retorno.append(j)
        return retorno

    #segun la hora del día voy a completar mi lista de enfermeros que estan de tuno de manera aleatoria
    def nursesONCALL(self,x:int)->None:
        aux = self.cantEnfermeros(x)
        enfermeros=self.GET_NURSE_ONCALL(x)
        for i in range(aux):
            j=random.randrange(len(enfermeros))
            self.nursesOnCall.append(enfermeros[j])
    
    #con los enfermeros del archivo de pacientes total voy a bajar esa cantidad de pacientes 

    def patientsArrival(self) -> None:  #INSERTION SORT
        newPatients = readPatient(self.atendidos, len(self.nursesOnCall))

        self.atendidos=self.atendidos + len(self.nursesOnCall)
        for i in newPatients:
            createTag(newPatients[i-1])#le cargo la etiqueta al paciente
        self.patients.append(newPatients)
        for i in range(1,len(self.patients),1):
   
            j=i-1
            current = self.patients[i]
            while j>=0 and self.patients[j].tag.maxTime>current.tag.maxTime:
                self.patients[j+1]= self.patients[j]
                j=j-1
            self.patients[j+1]=current
        return #pasan a la sala de espera del medico
    
   
    def rearange(self) ->None:#MERGE SORT
        for x in self.patients:
            self.patients[x].setRemainingTime()

        if len(self.patients)==1:
            return self.patients
        else:
            mid=len(self.patients)//2
            half1=self.patients[:mid]
            half2=self.patients[mid:]

            array1 = self.rearange(half1)
            array2 = self.rearange(half2)

            i=j=k=0

            while i<len(array1) and j<len(array2):  
                if array1[i].remainingTime < array2[j].remainingTime:  #mando al que menos tiempo le queda
                    self.patients[k]= array1[i]
                    i+=1
                elif array1[i].remainingTime > array2[j].remainingTime:
                    self.patients[k]= array2[j]
                    j+=1
                else: #les queda  a los dos el mismo tiempo
                    if array1[i].GET_PRIORITY() and array2[j].GET_PRIORITY() or not(array1[i].GET_PRIORITY()) and not(array2[j].GET_PRIORITY()):
                        #cuando les queda el mismo tiempo de espera y ambos o ninguno es prioritario (not(nor)); entonces clasifico por edad
                        if array1[i].GET_EDAD() < array2[j].GET_EDAD():
                                self.patients[k]=array2[j]  #el mayor va a ser atendido primero
                                j+=1
                        else:
                            self.patients[k]=array1[i]
                            i+=1
                    elif array1[i].GET_PRIORITARIO():   #si array1 es prioritario
                        self.patients[k]=array1[i]
                        i+=1
                    else:   #si array2 es prioritario
                        self.patients[k]=array2[j]
                        j+=1
            
            #una vez ordenado completo con array 1 si el mientras terminó por el array 2; y completo el array 2 si el moientras terminó por array 1 
            while i< len(array1):
                self.patients[k]=array1[i]
                i+=1
                k+=1
            while j< len(array2):
                self.patients[k]=array2[j]
                j+=1
                k+=1

        return 
    
   

    def organize(self)->None:
        i=0
        while i<12: #para llegar a la hora
            #ordena por color
            self.patientsArrival()
       
            for x in self.patients:   #para simular el paso del tiempo
                self.patients[x].timeIncrement()

            self.rearange()
            register(self.patients.pop(0))
            del(self.patients)  #quiero vaciar la lista pero no sé si se hace así
            i+=1

    def laborDay(self): #simulacion del dia que pasa para ver como se manejan enfermeros en distintos turnos
        for i in range(0,23,1):
            self.nursesONCALL(i)
            self.organize()
