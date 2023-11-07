import pytest
from library.cHospital import *
from src.cPaciente import *

def test_nursesByShifts():
    
    miHospital=cHospital("VL")
    assert miHospital.nurses[7].name=="Ekaterina"
    x=0
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1
    x=1
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1
    x=2
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1
    x=3
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1
    x=4
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1
    x=5
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1
    x=23
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==1

    x=6
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==2
    x=7
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==2
    x=8
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==2
    x=9
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==2

    x=10
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==5
    x=11
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==5
    x=12
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==5
    x=13
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==5
    x=14
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==5
    x=15
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==5
    
    x=16
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3
    x=17
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3
    x=18
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3
    x=19
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3
    x=20
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3
    x=21
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3
    x=22
    miHospital.setNursesONCALL(x)
    assert len(miHospital.nursesOnCall)==3

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
#    assert miHospital.patients[0].name=="Marys"
 #   assert miHospital.patients[1].name=="Dena"
  #  assert miHospital.patients[2].name=="Rand"  
   # assert miHospital.patients[3].name=="William"
  #  assert miHospital.patients[4].name=="Shelby"
    miHospital.patientsArrival()

    for x in miHospital.patients:  
        x.timeIncrement()

    miHospital.patients=miHospital.rearange(miHospital.patients)
   # assert miHospital.patients[0].name=="Hamilton"
    #assert miHospital.patients[1].name=="Hamilton"
#    assert miHospital.patients[2].name=="Hamilton"
 #   assert miHospital.patients[3].name=="Abie"
  #  assert miHospital.patients[4].name=="Hamilton"
   # assert miHospital.patients[5].name=="Perle"
#    assert miHospital.patients[6].name=="Morna"
 #   assert miHospital.patients[7].name=="Mischa"
  #  assert miHospital.patients[8].name=="Abie"
   # assert miHospital.patients[9].name=="Hamilton"


