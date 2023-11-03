import pytest
from library.cEtiqueta import cEtiqueta

def test_hospital():
    mietiqueta: cEtiqueta = cEtiqueta()
    assert mietiqueta.color == "blue" 
