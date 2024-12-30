import tkinter as tk

def calculate():
    try:
        feet = float(entry.get())
        football_fields = feet / 360
        result_label.config(text=f"Result: {football_fields:.2f} football fields")
    except ValueError:
        result_label.config(text="Please enter a valid number")

root = tk.Tk()
root.title("Feet to Football Fields")
root.iconphoto(True, tk.PhotoImage(file="icon.png"))
root.geometry("400x200")
title_label = tk.Label(root, text="Feet to Football Fields", font=("Arial", 18))
title_label.pack(pady=10)
input_frame = tk.Frame(root)
input_frame.pack(pady=10)
feet_label = tk.Label(input_frame, text="Feet:", font=("Arial", 14))
feet_label.pack(side=tk.LEFT, padx=5)
entry = tk.Entry(input_frame, font=("Arial", 14))
entry.pack(side=tk.LEFT, padx=5)
calculate_button = tk.Button(root, text="Convert", font=("Arial", 14), command=calculate)
calculate_button.pack(pady=10)
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack(pady=10)
root.mainloop()

