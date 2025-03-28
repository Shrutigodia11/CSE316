import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import random

# ===========================
# Module 1: AI-Based Scheduler
# ===========================
def train_ml_scheduler(training_data):
    """ Dummy ML training function (Replace this with an actual ML model) """
    model = {"average": sum(training_data) / len(training_data)}
    return model

def predict_schedule(model, disk_requests):
    """ Predicts an optimal schedule (Sorted order for simplicity) """
    return sorted(disk_requests)

# ===========================
# Module 2: Simulation & Visualization
# ===========================
def simulate_disk_movement(initial_position, schedule):
    """ Simulates disk head movement and calculates total movement """
    positions = [initial_position] + schedule
    distances = [abs(positions[i+1] - positions[i]) for i in range(len(positions)-1)]
    total_movement = sum(distances)
    return positions, total_movement

def visualize_movement(positions):
    """ Plots disk head movement """
    steps = list(range(len(positions)))
    plt.figure("Disk Head Movement")
    plt.plot(steps, positions, marker='o', linestyle='-', color='b')
    plt.title("Disk Head Movement Simulation")
    plt.xlabel("Step")
    plt.ylabel("Disk Cylinder")
    plt.grid(True)
    plt.show()

# ===========================
# Module 3: GUI & Performance Analysis
# ===========================
def run_simulation():
    """ Handles user input, runs AI-based scheduling, and displays results """
    try:
        initial = int(initial_entry.get())
        requests = list(map(int, request_entry.get().split(',')))
    except Exception:
        messagebox.showerror("Input Error", "Enter valid integers (comma-separated for disk requests).")
        return

    # Train ML model with random data (can be replaced with real data)
    training_data = [random.randint(0, 200) for _ in range(10)]
    model = train_ml_scheduler(training_data)

    # Predict optimal schedule
    schedule = predict_schedule(model, requests)

    # Simulate disk head movement
    positions, total_movement = simulate_disk_movement(initial, schedule)

    # Display results
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"Optimal Schedule: {schedule}\n")
    result_text.insert(tk.END, f"Total Head Movement: {total_movement}\n")

    # Visualize disk movement
    visualize_movement(positions)

# GUI Setup
root = tk.Tk()
root.title("AI-Based Disk Scheduling Simulator")

# Labels & Inputs
tk.Label(root, text="Initial Head Position:").grid(row=0, column=0, padx=5, pady=5, sticky="e")
initial_entry = tk.Entry(root)
initial_entry.grid(row=0, column=1, padx=5, pady=5)

tk.Label(root, text="Disk Requests (comma-separated):").grid(row=1, column=0, padx=5, pady=5, sticky="e")
request_entry = tk.Entry(root)
request_entry.grid(row=1, column=1, padx=5, pady=5)

# Run Simulation Button
run_button = tk.Button(root, text="Run Simulation", command=run_simulation)
run_button.grid(row=2, column=0, columnspan=2, pady=10)

# Result Display
result_text = tk.Text(root, height=8, width=50)
result_text.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

root.mainloop()
