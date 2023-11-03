import csv
from src.cPaciente import cPaciente
from library.cEnfermero import cEnfermero

def readPatient():
    pacientes=[]
    with open("pacientes.csv") as file:
        reader=csv.reader(file)
        next(file)
        cont=0
        aux:[]
        for x in reader:
            pacienteAux=cPaciente(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
            pacientes.append(pacienteAux)   #PREGUNTAR A VALEN CÓMO LO PENSÓ
    file.close()

    return pacientes

def readNurse():
    enfermeros=[]
    with open("enfermeros.csv") as file:
        next(file)
        reader=csv.reader(file)
        
        for x in reader:
            enfermeroAux=cEnfermero(x[0],x[1],x[2],x[3],x[4])
            enfermeros.append(enfermeroAux)
    file.close()

    return enfermeros
