import tkinter as tk
import random

class Patient:
    def __init__(self, color, max_time):
        self.color = color
        self.max_time = max_time
        self.remaining_time = max_time

class HospitalQueue:
    def __init__(self):
        self.sequence = ["red", "orange", "yellow", "green", "blue"]
        self.patients = []
        self.assisted_patients = []
        self.minutes_passed = 0

    def generate_patients(self):
        # Generate a random number of patients (between 1 and 5)
        num_patients = random.randint(1, 5)
        
        for _ in range(num_patients):
            # Generate a random color for each new patient
            color = random.choice(self.sequence)
            max_time = {"red": 0, "orange": 10, "yellow": 60, "green": 120, "blue": 240}[color]
            patient = Patient(color, max_time)
            self.patients.append(patient)

    def update_queue(self):
        self.patients.sort(key=lambda x: x.remaining_time)

    def increase_time(self):
        assisted = []
        for patient in self.patients:
            if patient.remaining_time > 5:
                patient.remaining_time -= 5
            else:
                patient.remaining_time = 0
                assisted.append(patient)

        for patient in assisted:
            self.patients.remove(patient)
            self.assisted_patients.append(patient)

        self.minutes_passed += 5

def update_display():
    canvas.delete("all")

    # Display minutes passed label
    canvas.create_text(canvas_width // 2, 20, text=f"Minutes Passed: {hospital_queue.minutes_passed}", font=("Helvetica", 12))

    # Display patients
    row = 1
    for i, patient in enumerate(hospital_queue.patients):
        x = i % (canvas_width // 50) * 50
        y = (i // (canvas_width // 50)) * 50 + 50
        canvas.create_rectangle(x, y, x + 40, y + 40, fill=patient.color)
        canvas.create_text(x + 20, y + 20, text=str(patient.remaining_time))

    # Display assisted patients at the bottom
    row = (len(hospital_queue.patients) // (canvas_width // 50)) + 2
    for i, patient in enumerate(hospital_queue.assisted_patients):
        x = i % (canvas_width // 50) * 50
        y = row * 50
        if i > 0 and i % (canvas_width // 50) == 0:
            row += 1
        canvas.create_rectangle(x, y, x + 40, y + 40, fill=patient.color)
        canvas.create_text(x + 20, y + 20, text="Assisted")

def button_pressed():
    hospital_queue.increase_time()
    hospital_queue.update_queue()
    hospital_queue.generate_patients()
    update_display()

# Initialize the hospital queue and generate initial patients
hospital_queue = HospitalQueue()
hospital_queue.generate_patients()

# Create the GUI
root = tk.Tk()
root.title("Hospital Queue")

canvas_width = 1400
canvas_height = 800  # Increased canvas height
canvas = tk.Canvas(root, width=canvas_width, height=canvas_height)  # Increased canvas height
canvas.pack()

button = tk.Button(root, text="Increase Time", command=button_pressed)
button.pack()

update_display()

root.mainloop()
