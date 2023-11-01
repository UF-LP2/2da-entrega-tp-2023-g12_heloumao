import pytest
from src.cEnfermero import cEnfermero
from src.lecturaArchivos import *
from src.cEtiqueta import *
def test_hospital():
    mietiqueta: cEtiqueta = cEtiqueta()
    assert mietiqueta.color == "blue" 