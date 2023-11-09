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

