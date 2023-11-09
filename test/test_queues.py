import pytest
from library.cHospital import *
from src.cPaciente import *

def test_queuesIS():
    miHospital=cHospital("VL")
    miHospital.setNursesONCALL(15)
    miHospital.patientsArrival()
    paciente1=miHospital.patients[0]
    paciente2=miHospital.patients[1]
    paciente3=miHospital.patients[2]
    paciente4=miHospital.patients[3]
    paciente5=miHospital.patients[4]

    assert paciente1.name=="Marys"
    assert paciente2.name=="Dena"
    assert paciente3.name=="Rand"  
    assert paciente4.name=="William"
    assert paciente5.name=="Shelby" 

def test_queuesMS():
    miHospital=cHospital("VL")
    miHospital.setNursesONCALL(15)
    miHospital.patientsArrival()
    
    for x in miHospital.patients:   #para simular el paso del tiempo
        x.timeIncrement()
    assert miHospital.patients[0].name=="Marys"
    assert miHospital.patients[1].name=="Dena"
    assert miHospital.patients[2].name=="Rand"  
    assert miHospital.patients[3].name=="William"
    assert miHospital.patients[4].name=="Shelby" 

    miHospital.patients=miHospital.rearange(miHospital.patients)
    assert miHospital.patients[0].name=="Rand"
    assert miHospital.patients[1].name=="Marys"
    assert miHospital.patients[2].name=="Dena"  
    assert miHospital.patients[3].name=="Shelby"
    assert miHospital.patients[4].name=="William"
    miHospital.patientsArrival()

    assert miHospital.patients[0].name=="Rand"
    assert miHospital.patients[1].name=="Marys"
    assert miHospital.patients[2].name=="Dena"  
    assert miHospital.patients[3].name=="Shelby"
    assert miHospital.patients[4].name=="William"
    assert miHospital.patients[5].name=="Perle"
    assert miHospital.patients[6].name=="Morna"
    assert miHospital.patients[7].name=="Mischa"
    assert miHospital.patients[8].name=="Abie"
    assert miHospital.patients[9].name=="Hamilton"
    for x in miHospital.patients:  
        x.timeIncrement()

    miHospital.patients=miHospital.rearange(miHospital.patients)
    assert miHospital.patients[0].name=="Perle"
    assert miHospital.patients[1].name=="Rand"
    assert miHospital.patients[2].name=="Marys"
    assert miHospital.patients[3].name=="Dena"
    assert miHospital.patients[4].name=="Morna"
    assert miHospital.patients[5].name=="Abie"
    assert miHospital.patients[6].name=="Mischa"
    assert miHospital.patients[7].name=="Shelby"
    assert miHospital.patients[8].name=="William"
    assert miHospital.patients[9].name=="Hamilton"
