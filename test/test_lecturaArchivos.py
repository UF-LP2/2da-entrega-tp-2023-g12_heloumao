from cEnfermero import cEnfermero
from lecturaArchivos import readNurse
import pytest

def test_archivos():
    leido=readNurse()
    assert (leido[0].name=="Sheree")
