from library.cHospital import *
# def main() -> None:
#   print("Hello World")

if __name__ == "__main__":
  enfermeros=[]
  enfermeros=readNurse()
  print(enfermeros[0].name)
  pacientes=[]
  pacientes=readPatient(0,5)
  enfermeros[0].createTag(pacientes[0])
  print(pacientes[0].tag.color)
