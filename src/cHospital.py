from cPaciente import cPaciente
from cEnfermero import cEnfermero


class cHospital:
    def __init__(self, name:str, patients: list(cPaciente), nurses:list(cEnfermero)):
        self.name=name
        self.patients=patients
        self.nurses=nurses

    
