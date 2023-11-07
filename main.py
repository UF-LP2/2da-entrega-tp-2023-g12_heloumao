from library.cHospital import *
# def main() -> None:
#   print("Hello World")

if __name__ == "__main__":
  enfermeros=[]
  enfermeros=readNurse()
  
 # enfermeros[0].createTag(pacientes[0])
 # print(pacientes[0].tag.color)
 # miHospital=cHospital("VL")
 # miHospital.setNursesONCALL(5)
 # miHospital.patientsArrival()
 # print(miHospital.patients[0].name)
  miHospital=cHospital("VL")
  miHospital.setNursesONCALL(15)
  miHospital.patientsArrival()
  for x in miHospital.patients:   #para simular el paso del tiempo
    x.timeIncrement()
  miHospital.patients=miHospital.rearange(miHospital.patients)
  print("- - - - HOSPITAL - - - -")
  for x in miHospital.patients:
    print(x.name)
  print(miHospital.patients[2].priority)

  
  

