import tkinter as tk
from tkinter import filedialog
import os

def process_data(file_path):
    # Dictionary to hold the sum of values for each date
    date_sums = {}

    # Read and process the file
    with open(file_path, 'r') as file:
        for line in file:
            # Split the line into date and value
            date, value = line.split()
            value = float(value)
            
            # Sum the values for each date
            if date in date_sums:
                date_sums[date] += value
            else:
                date_sums[date] = value

    # Return the processed data
    return date_sums

def save_results(date_sums, output_file):
    # Save the results to a file
    with open(output_file, 'w') as file:
        for date, total in date_sums.items():
            file.write(f"{date}  {total:.2f}\n")

def select_file():
    # Create a GUI window
    root = tk.Tk()
    root.withdraw()  # Hide the main window

    # Open file dialog and return the selected file path
    file_path = filedialog.askopenfilename()
    return file_path

def generate_output_file_path(selected_file_path):
    # Generate the output file path
    if selected_file_path:
        directory, filename = os.path.split(selected_file_path)
        name, ext = os.path.splitext(filename)
        output_filename = f"{name}-earning{ext}"
        return os.path.join(directory, output_filename) if directory else output_filename
    return None

# Use the GUI to select the file
file_path = select_file()

# Process and save the results if a file was selected
if file_path:
    date_sums = process_data(file_path)
    output_file = generate_output_file_path(file_path)
    save_results(date_sums, output_file)
    print(f"Results saved to {output_file}")
