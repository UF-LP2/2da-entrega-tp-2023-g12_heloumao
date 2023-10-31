import csv
import cPaciente

def readPatient():
    pacientes=[cPaciente]
    with open("pacientes.csv") as file:
        reader=csv.reader(file)
        next(file)

        for x in reader:
            pacienteAux=cPaciente(x[0],x[1]x[2],x[3],x[4],x[5])
            pacientes.append(pacienteAux)
    file.close()
    return pacientes

def readNurse():
    enfermeros=[cEnfermero]
    with open("enfermeros.csv") as file:
        reader=csv.reader(file)
        next(file)

        for x in reader:
            enfermeroAux(x[0],x[1]x[2],x[3],x[4],x[5])
            enfermeros.append(enfermeroAux)
    file.close()
    return enfermeros


