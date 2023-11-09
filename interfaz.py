import tkinter as tk
from src.archivos import readPatient
from library.cEtiqueta import cEtiqueta
from src.cPaciente import *
import random


class HospitalInterface:
    def __init__(self, master):
        self.master = master
        self.master.title("Hospital Interface")
        self.pacientes=readPatient(0,100)

        self.time_label = tk.Label(master, text="Tiempo: 00:00")
        self.time_label.pack()

        self.nurses_label = tk.Label(master, text="Enfermeros: 0")
        self.nurses_label.pack()

        self.next_button = tk.Button(master, text="Avanzar 5 minutos", command=self.advance_time)
        self.next_button.pack()

        self.current_time = 0  # Representa el tiempo en minutos
        self.nurses = 2  # Cantidad de enfermeros
        self.turno = "dia"  # Configura los turnos (por ejemplo, día y noche)



        # Configura la interfaz para mostrar pacientes
        self.patient_widgets = []
        for paciente in self.pacientes:
            paciente_widget = tk.Label(master, text=f"P{paciente.id}", bg="blue")
            paciente_widget.pack()
            self.patient_widgets.append(paciente_widget)

    def advance_time(self):
        self.current_time += 5
        self.update_interface()

    def update_interface(self):
    # ... (código existente)

    # Calcula la cantidad de pacientes basándose en la cantidad de enfermeros
        num_pacientes = min(self.nurses, len(self.pacientes))

    # Actualiza los colores de los pacientes y muestra el color asignado
        for paciente_widget, paciente in zip(self.patient_widgets[:num_pacientes], self.pacientes[:num_pacientes]):
            nuevo_color = self.assign_color()  # Función para asignar un nuevo color
            paciente_widget.config(bg=nuevo_color)

    def assign_color(self):
        # Esta función simula la asignación de colores según alguna lógica específica
        return random.choice(["rojo", "amarillo", "verde"])

# Crear la aplicación
root = tk.Tk()
app = HospitalInterface(root)

# Ejecutar la aplicación
root.mainloop()