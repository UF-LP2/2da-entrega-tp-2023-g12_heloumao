import pytest
from library.cHospital import *
from library.cEnfermero import cEnfermero

def test_diagnostico():
    pacientes=readPatient(0,5)
    enfermeros=readNurse()
    for i in range(len(pacientes)):
        enfermeros[0].createTag(pacientes[i])

    assert pacientes[0].tag.color=="yellow"
    assert pacientes[1].tag.color=="orange"
    assert pacientes[2].tag.color=="orange"
    assert pacientes[3].tag.color=="yellow"
    assert pacientes[4].tag.color=="orange"