#class cArbolSintomas:
class cNode:
    def __init__(self, val, name,left=None,  rigth=None):
        super().__init__(val,left,rigth)
        self.name=name