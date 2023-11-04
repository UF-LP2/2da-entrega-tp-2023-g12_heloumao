
global maxOrange
maxOrange = 10
global maxGreen
maxGreen =120
global maxYellow
maxYellow=60
global maxBlue
maxBlue=240


class cEtiqueta:
    def __init__(self, color="blue", maxTime=maxBlue):
        self.color=color
        self.maxTime=maxTime
    
    @staticmethod
    def GET_MAX_TIME(self, color:str)->int:
        color = color.lower()
        if color== "blue":
            return maxBlue
        elif color== "orange":
            return maxOrange
        elif color== "green":
            return maxGreen
        elif color== "yellow":
            return maxYellow
        elif color== "red":
            return 0
        else: 
            raise Exception ("Invalid color")
