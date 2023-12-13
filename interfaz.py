import tkinter as tk
import random

#clase paciente simplificada
class Patient:
    def __init__(self, color, max_time):
        self.color = color
        self.max_time = max_time
        self.remaining_time = max_time

#clase que representa la cola de pacientes
class HospitalQueue:
    def __init__(self):
        self.colors = ["red", "orange", "yellow", "green", "blue"]
        self.patients = []
        self.assisted_patients = []
        self.minutes_passed = 0

    def generate_patients(self):
        # Generar nro random entre 1 y 5 para ir agregando
        num_patients = random.randint(1, 5)
        
        for _ in range(num_patients):
            # Generacion random de color para cada paciente junto su tiempo max
            color = random.choice(self.colors)
            #a cada color le coresponde un t max
            max_time = {"red": 0, "orange": 10, "yellow": 60, "green": 120, "blue": 240}[color]
            patient = Patient(color, max_time)
            self.patients.append(patient)

    #ordena cola por tiempo restante
    def update_queue(self):
        self.patients.sort(key=lambda x: x.remaining_time)

    #para aumentar el tiempo
    def increase_time(self):
        assisted = []
        for patient in self.patients:   #si le quedan mas de 5 minutos se los resto
            if patient.remaining_time > 5:
                patient.remaining_time -= 5
            else:   #sino lo agrego a la fila de pacientese asistidos
                patient.remaining_time = 0
                assisted.append(patient)

        for patient in assisted:    #elimino los pacientes sistidos de la cola y los agrego a la de asistidos
            self.patients.remove(patient)
            self.assisted_patients.append(patient)

        self.minutes_passed += 5    #incremento el tiempo

#interfaaz
def update_display():
    canvas.delete("all")

    # Labal de "Minutes passed"
    canvas.create_text(canvas_width // 2, 20, text=f"Minutes Passed: {hospital_queue.minutes_passed}", font=("Helvetica", 14))

    # Mostrar los bloques de pacientes en filas
    row = 1
    for i, patient in enumerate(hospital_queue.patients):
        #genero el tamaño y color de los cuadrados en base al ancho y alto del canvas
        x = i % (canvas_width // 50) * 50
        y = (i // (canvas_width // 50)) * 50 + 50
        canvas.create_rectangle(x, y, x + 40, y + 40, fill=patient.color) #lleno con color correspondienete
        canvas.create_text(x + 20, y + 20, text=str(patient.remaining_time))    #agrego etiqueta de tiempo restante

    #Para mostrar los pacientes asistidos al fondo con etiqueta de assisted
    row = (len(hospital_queue.patients) // (canvas_width // 50)) + 2
    for i, patient in enumerate(hospital_queue.assisted_patients):
        x = i % (canvas_width // 50) * 50
        y = row * 50
        if i > 0 and i % (canvas_width // 50) == 0:
            row += 1
        canvas.create_rectangle(x, y, x + 40, y + 40, fill=patient.color)
        canvas.create_text(x + 20, y + 20, text="Assisted") 

def button_pressed():   #conecto botn y metodos
    hospital_queue.increase_time()
    hospital_queue.update_queue()
    hospital_queue.generate_patients()
    update_display()    #actualizo

# Inicialización de la cola y llegada de pacientes
hospital_queue = HospitalQueue()
hospital_queue.generate_patients()

# Creación GUI
root = tk.Tk()
root.title("Hospital Queue")

canvas_width = 1300
canvas_height = 600  
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)  
canvas.pack()

#generacion del boton 
button = tk.Button(root, text="Increase Time", command=button_pressed)
button.pack()

update_display()

root.mainloop()
