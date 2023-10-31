from cEtiqueta import cEtiqueta
class cPaciente:
    def __init__(self, name:str, lastName:str, id: int, symptoms: list (str),  gender:str, age:int, priority:bool):
        self.name= name
        self.lastName=lastName
        self.id=id
        self.symptoms=symptoms
        self.tag=cEtiqueta()
        self.diagnosis=""
        self.survives=True
        self.timeLeft=0
        self.timePassed=0
        self.gender=gender
        self.priority=priority
        self.age=age
    
    

