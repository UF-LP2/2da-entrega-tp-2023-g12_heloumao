from src.cPaciente import cPaciente
from library.cArbolSintomas import tree
from library.cEtiqueta import cEtiqueta

class cEnfermero:

    def __init__(self, name:str, id:int, lastName:str, shift:str, available:bool):
        self.name=name
        self.lastName=lastName
        self.id=id
        self.shift=shift
        self.avaible=available
    
    def escolor(self,aux:str)->bool:
        if aux =="red" or aux =="yellow" or aux =="orange" or aux =="green" or aux == "blue":
            return True
        return False
    
    def diagnosis(self,paciente,arbol): #comparo los sintomas del paciente con los nodos del arbol hasta encontrar su hoja correspondiente (color)
        if self.escolor(arbol.name):
            return arbol
        for x in paciente.symptoms:
            if x==arbol.name:
                return self.diagnosis(paciente,arbol.left)
        return self.diagnosis(paciente,arbol.rigth)
    
    def createTag(self,paciente)->None:
        arbol=tree()
        arbolDiagnostico = self.diagnosis(paciente,arbol)
        tiempoMax = cEtiqueta.GET_MAX_TIME(arbolDiagnostico.name)
        paciente.tag = cEtiqueta(arbolDiagnostico.name,tiempoMax)
        paciente.remainingTime=tiempoMax




   
    
    
