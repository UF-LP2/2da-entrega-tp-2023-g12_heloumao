import cEtiqueta  
class cPaciente:
    def __init__(self, name:str, lastName:str, id: int, symptoms: [],  gender:str, age:int, priority:bool):
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
        def SET_SYMPTOMS(symptoms:list(str))->None:
            self.symptoms=symptoms
        def SET_PRIORITY(prio:bool)-> None:
            self.priority=prio
        def SET_GENDER(gender:str) ->None:
            self.gender=gender
        def SET_ID(id:int)->None:
            self.id=id
        
            
    
    

