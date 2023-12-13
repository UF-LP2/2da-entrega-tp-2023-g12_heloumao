from library.cEtiqueta import cEtiqueta  

class cPaciente:
    def __init__(self, name:str, lastName:str, id: int, symptom1: str, symptom2: str,symptom3: str, gender:str, age:int, priority:bool,remainingTime=0,timePassed=0):
        self.name= name
        self.lastName=lastName
        self.id=id
        symptom=[]
        symptom.append(symptom1)
        symptom.append(symptom2)
        symptom.append(symptom3)
        self.symptoms=symptom
        etiqueta=cEtiqueta
        self.tag=etiqueta
        self.diagnosis=""
        self.survives=True
        self.remainingTime=remainingTime
        self.timePassed=timePassed
        self.gender=gender
        self.priority=priority
        self.age=age

    def setRemainingTime(self)->None:
        self.remainingTime = self.tag.maxTime-self.timePassed
        
    def timeIncrement(self)->None:
        self.timePassed = self.timePassed + 5
        self.setRemainingTime()


    def GET_EDAD(self)->int:
        return self.age
    def GET_NAME(self)-> str:
        return self.name
    def GET_LAST_NAME(self) ->str:
        return self.lastName
    def GET_SYMPTOMS(self)->list:
        return self.symptoms
    def GET_PRIORITY(self)-> bool:
        return self.priority
    def GET_GENDER(self) ->str:
        return self.gender
    def GET_ID(self)->int:
        return self.id
        
    def SET_EDAD(self,age:int)->None:
        self.age=age
    def SET_NAME(self,name:str)->None:
        self.name=name
    def SET_LAST_NAME(self,lastName:str) ->None:
        self.lastName=lastName
        
    def SET_PRIORITY(self,prio:bool)-> None:
        self.priority=prio
    def SET_GENDER(self,gender:str) ->None:
        self.gender=gender
    def SET_ID(self,id:int)->None:
        self.id=id
        
            
    
    

