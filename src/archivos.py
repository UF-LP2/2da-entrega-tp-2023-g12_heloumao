import csv
from src.cPaciente import cPaciente
from library.cEnfermero import cEnfermero

def readPatient(atendidos:int, n:int)->list(cPaciente):
    pacientes=[]
    with open("pacientes.csv") as file:
        reader=csv.reader(file)
        next(file)
        i = 0
        while x in reader and i > atendidos and i < (n + atendidos):
            pacienteAux=cPaciente(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
            x+=1
            i+=1 
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

 #acá van a llegar los pacientes ya ordenados 
    def register (pacientes:[])->None: #paso los pacientes atendidos a un archivo para no perderlos cada vez que corro el programa
        with open("registro.csv","a") as file:
            writer = csv.writer(file)
            for row in pacientes: 
                writer.writerow(row.name,row.lastName,row.id,row.symptoms[0],row.sympotms[1],row.symptoms[2],row.gender, row.age,row.priority)
