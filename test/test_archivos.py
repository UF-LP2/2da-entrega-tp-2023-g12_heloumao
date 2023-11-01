import pytest
from src.cEtiqueta import cEtiqueta

def test_hospital():
    mietiqueta: cEtiqueta = cEtiqueta()
    assert mietiqueta.color == "blue" 
