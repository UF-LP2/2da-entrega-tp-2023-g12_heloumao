from library.cEtiqueta import cEtiqueta  

class cPaciente:
    def __init__(self, name:str, lastName:str, id: int, symptom1: str, symptom2: str,symptom3: str, gender:str, age:int, priority:bool):
        self.name= name
        self.lastName=lastName
        self.id=id
        symptoms=[]
        symptoms.append(symptom1)
        symptoms.append(symptom2)
        symptoms.append(symptom3)
        self.symptoms=symptoms
        self.tag=cEtiqueta()
        self.diagnosis=""
        self.survives=True
        self.remainingTime=0
        self.timePassed=0
        self.gender=gender
        self.priority=priority
        self.age=age

        def remainingTime(self)->None:
            self.remainingTime = self.tag.maxTime-self.timePassed
        
        def timeIncrement(self)->None:
            self.timePassed = self.timePassed + 5

        def GET_EDAD()->int:
            return self.age
        def GET_NAME()-> str:
            return self.name
        def GET_LAST_NAME() ->str:
            return self.lastName
        def GET_SYMPTOMS()->list:
            return self.symptoms
        def GET_PRIORITY()-> bool:
            return self.priority
        def GET_GENDER() ->str:
            return self.gender
        def GET_ID()->int:
            return self.id
        
        def SET_EDAD(age:int)->None:
             self.age=age
        def SET_NAME(name:str)->None:
             self.name=name
        def SET_LAST_NAME(lastName:str) ->None:
            self.lastName=lastName
        
        def SET_PRIORITY(prio:bool)-> None:
            self.priority=prio
        def SET_GENDER(gender:str) ->None:
            self.gender=gender
        def SET_ID(id:int)->None:
            self.id=id
        
            
    
    

