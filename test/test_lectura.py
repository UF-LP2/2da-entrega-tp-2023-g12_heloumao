import pytest
from library.cEnfermero import cEnfermero
from src.lecturaArchivos import *
from library.cEtiqueta import *

def test_leerEnfermero():
    enfermeros=readNurse()
    assert enfermeros[0].name=="Sheree" 

def test_leerPaciente():
    pacientes=readPatient()
    assert pacientes[0].name=="William"
    assert pacientes[4].symptoms[1]==""
    assert pacientes[50].symptoms[0]=="unconscious"
    assert pacientes[23].tag.color=="blue"
