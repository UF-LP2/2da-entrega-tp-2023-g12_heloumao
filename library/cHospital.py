
from library.cEnfermero import *
import random
from src.archivos import readNurse
from src.archivos import readPatient
from src.archivos import register



class cHospital:
    def __init__(self, name:str):  #ctor
        self.name=name
        self.patients:cPaciente=[] #pacientes en standby
        self.nurses=readNurse()
        self.nursesOnCall:cEnfermero=[]
        self.atendidos = 0 #cantidad de pacientes atenidos
        self.registrados=0
    
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
            shiftaux= "afternoon"
        elif x>=6 and x<10:
            shiftaux= "morning"
        else:
            shiftaux= "night"
        return shiftaux
    
    def GET_NURSE_ONCALL(self,x:int)->[]:
        shiftaux=self.defineShift(x)
        retorno = []
        for j in range(len(self.nurses)):
            if self.nurses[j].shift == shiftaux:
                retorno.append(self.nurses[j])
        return retorno

    #segun la hora del día voy a completar mi lista de enfermeros que estan de tuno de manera aleatoria
    def setNursesONCALL(self,x:int)->None:
        aux = self.cantEnfermeros(x)
        nursesOnCall=[]
        enfermeros=self.GET_NURSE_ONCALL(x)
        for i in range(0,aux):
            j=random.randrange(0,len(enfermeros),1)
            nursesOnCall.append(enfermeros[j])
        self.nursesOnCall=nursesOnCall
    
    #con los enfermeros del archivo de pacientes total voy a bajar esa cantidad de pacientes 

    def patientsArrival(self) -> None:  #INSERTION SORT
        newPatients = readPatient(self.atendidos, len(self.nursesOnCall))

        self.atendidos=self.atendidos + (len(self.nursesOnCall))
        for i in range(len(newPatients)):
            self.nursesOnCall[i].createTag(newPatients[i-1])#le cargo la etiqueta al paciente
        
        for i in range(1,len(newPatients),1):
            j=i-1
            current = newPatients[i]
            while j>=0 and newPatients[j].tag.maxTime>current.tag.maxTime:
                newPatients[j+1]= newPatients[j]
                j=j-1
            newPatients[j+1]=current
        self.pacientesActuales(newPatients)
        self.patients=self.patients+newPatients

        return #pasan a la sala de espera del medico
    
   
    def rearange(self,patients):#MERGE SORT

        if len(patients)<=1:
            return patients
        else:
            mid=int(len(patients)/2)
            half1=patients[:mid]
            half2=patients[mid:]

            array1 = self.rearange(half1)
            array2 = self.rearange(half2)

            i=j=k=0

            while i<len(array1) and j<len(array2):  
                if array1[i].remainingTime < array2[j].remainingTime:  #mando al que menos tiempo le queda
                    patients[k]= array1[i]
                    i+=1
                elif array1[i].remainingTime > array2[j].remainingTime:
                    patients[k]= array2[j]
                    j+=1
                else: #les queda  a los dos el mismo tiempo
                    if ((array1[i].priority=="True" and array2[j].priority=="True") or (array1[i].priority=="False" and array2[j].priority=="False")):
                        #cuando les queda el mismo tiempo de espera y ambos o ninguno es prioritario (not(nor)); entonces clasifico por edad
                        if array1[i].age < array2[j].age:
                            patients[k]=array2[j]  #el mayor va a ser atendido primero
                            j+=1
                        else:
                            patients[k]=array1[i]
                            i+=1
                    elif array1[i].priority=="True":   #si array1 es prioritario
                        patients[k]=array1[i]
                        i+=1
                    else:   #si array2 es prioritario
                        patients[k]=array2[j]
                        j+=1
                 
                k+=1
            
            #una vez ordenado completo con array 1 si el mientras terminó por el array 2; y completo el array 2 si el moientras terminó por array 1 
            while i< len(array1):
                patients[k]=array1[i]
                i+=1
                k+=1
            while j< len(array2):
                patients[k]=array2[j]
                j+=1
                k+=1
        
 
        return patients
    
   

    def organize(self, hora)->None:
        i=0
        while i<12: #para llegar a la hora
            #ordena por color
            minutos=5*i
            if i==0:
                print("\n")
                print(f"Hora: {hora}: {minutos}, Enfermeros: {self.cantEnfermeros(hora)}")
            else:
                print("\n")
                print(f"Hora: {hora}: {minutos}")

            self.patientsArrival()
       
            for x in range(len(self.patients)):   #para simular el paso del tiempo
                self.patients[x].timeIncrement()

            self.patients=self.rearange(self.patients)
            j=cont=0
               
            while j<len(self.patients)  :
                if self.patients[j].remainingTime<=5:
                    register(self.patients[j],self.registrados)
                    self.registrados+=1
                    cont+=1
                j+=1
            
            self.patients=self.patients[cont:]
            
            i+=1

    def laborDay(self): #simulacion del dia que pasa para ver como se manejan enfermeros en distintos turnos
        for i in range(0,24,1):
            self.setNursesONCALL(i)
            self.organize(i)
 

    def pacientesActuales(self, pacientes):
        cont=0
        print("Pacientes ingresados en los ultimos 5 minutos")
        for x in pacientes:
            cont+=1
            print(f"{cont} - Nombre: {x.name}; Id: {x.id}; Color: {x.tag.color}; Tiempo restante: {x.remainingTime}")