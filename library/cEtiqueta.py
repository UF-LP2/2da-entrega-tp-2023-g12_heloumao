from typing import Self


class Etiqueta:
    def __init__(self, color:str, maxTime:int):
        self.color=color
        self.maxTime=maxTime

    def __init__(self):
        self.color="blue"
        self.maxTime=240