import csv
from library.cEnfermero import cEnfermero
from src.cPaciente import cPaciente
def readPatient(atendidos:int, n:int)->[]:
    pacientes=[]
    with open("pacientes.csv") as file:
        reader=csv.reader(file)
        next(file)
        i = 0
        for x in reader:
            if i>=atendidos and i < (n + atendidos):
                pacienteAux=cPaciente(x[0],x[1],x[2],x[3],x[4],x[5],x[6],x[7],x[8])
                pacientes.append(pacienteAux)
            i=i+1 
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
def register (paciente:cPaciente)->None: #paso los pacientes atendidos a un archivo para no perderlos cada vez que corro el programa
    with open("registro.csv","a") as file:
        writer = csv.writer(file)
        writer.writerow([paciente.name,paciente.lastName,paciente.id,paciente.symptoms[0],paciente.symptoms[1],paciente.symptoms[2],paciente.gender,paciente.age, paciente.priority])
