import pytest

from cEnfermero import cEnfermero
from lecturaArchivos import readNurse

def test_archivos():
    leido=readNurse()
    assert (leido[0].name=="Sheree")
