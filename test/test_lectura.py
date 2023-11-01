
from src.cEnfermero import cEnfermero
from src.lecturaArchivos import *
    
def test_archivos():
    leido=readNurse()
    assert leido[0].name=="Sheree"
