from src.lecturaArchivos import *
# def main() -> None:
#   print("Hello World")
from src.cHospital import *
if __name__ == "__main__":
  enfermeros=[]
  enfermeros=readNurse()
  print(enfermeros[0].name)
  bt = crearArbol()
  print(bt)
  print(bt.values)
  print("hello world")