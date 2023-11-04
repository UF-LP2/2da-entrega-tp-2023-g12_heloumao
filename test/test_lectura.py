import pytest

from library.cHospital import *

def test_leerEnfermero():
    enfermeros=readNurse()
    assert enfermeros[0].name=="Sheree" 

def test_leerPacientes():
    pacientes=readPatient(0,5)
    assert pacientes[0].name=="William"
    pacientes1=readPatient(5,1)
    assert pacientes1[0].name=="Morna"
    

