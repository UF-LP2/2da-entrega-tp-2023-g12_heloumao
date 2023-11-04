from src.cPaciente import cPaciente
import cArbolSintomas
import cEtiqueta
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
    
    def diagnosis(self,paciente:cPaciente): #comparo los sintomas del paciente con los nodos del arbol hasta encontrar su hoja correspondiente (color)
        arbol=cArbolSintomas.tree()
        if self.escolor(arbol.name):
            return arbol
        for x in paciente.symptoms:
            if x==arbol.name:
                return self.diagnosis(arbol.left)
        return self.diagnosis(arbol.rigth)
    
    def createTag(self,paciente:cPaciente)->None:
        arbol = self.diagnosis(self,paciente)
        tiempoMax = cEtiqueta.GET_MAX_TIME(arbol.name)
        paciente.tag = cEtiqueta(arbol.name,tiempoMax)




   
    
    
