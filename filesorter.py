import os
import shutil
from tkinter import filedialog, StringVar, IntVar, Toplevel
import customtkinter as ctk
from datetime import datetime
import webbrowser

available_extensions = ["pdf", "jpg", "png", "mp4", "txt", "php", "js", "zip", "rar", "mp3", "doc", "docx", "xls", "xlsx", "ppt", "pptx"]

def get_creation_date(file_path):
    return datetime.fromtimestamp(os.path.getctime(file_path)).strftime("%Y-%m-%d")

def sort_files(directory, file_extensions, custom_folder):
    destination_folder = custom_folder if custom_folder else os.path.join(os.path.expanduser("~"), "Desktop", "Sorted_Files")
    os.makedirs(destination_folder, exist_ok=True)

    for root, _, files in os.walk(directory):
        for file in files:
            file_ext = file.split(".")[-1].lower()

            if file_ext in file_extensions:
                creation_date = get_creation_date(file_path := os.path.join(root, file))
                new_name = f"{creation_date}_{file}"

                if "invoice" in file.lower():
                    invoice_number = file.split("_")[0] if "_" in file else "UNKNOWN"
                    new_name = f"{invoice_number}_Invoice_{creation_date}.{file_ext}"

                new_path = os.path.join(destination_folder, new_name)

                counter = 1
                while os.path.exists(new_path):
                    new_name = f"{creation_date}_{counter}_{file}"
                    new_path = os.path.join(destination_folder, new_name)
                    counter += 1

                shutil.move(file_path, new_path)
                print(f"Moved: {file_path} -> {new_path}")

def select_directory():
    directory = filedialog.askdirectory()
    if directory:
        selected_directory.set(directory)

def set_custom_folder():
    folder = filedialog.askdirectory()
    if folder:
        custom_folder.set(folder)

def start_sorting():
    directory = selected_directory.get()
    if not directory:
        print("Please select a directory.")
        return

    selected_extensions = list(extension_var.get())
    if not selected_extensions:
        print("Please select at least one file extension.")
        return

    sort_files(directory, selected_extensions, custom_folder.get())

def show_language_selection():
    def set_language(language):
        if language == "English":
            language_text.set("Welcome! This is an Open Source project. For custom features, you can opt for a paid version. Author: github.com/kristiangasic")
        elif language == "Deutsch":
            language_text.set("Willkommen! Dies ist ein Open-Source-Projekt. Für benutzerdefinierte Funktionen können Sie eine kostenpflichtige Version wählen. Autor: github.com/kristiangasic")
        elif language == "Français":
            language_text.set("Bienvenue! Ceci est un projet Open Source. Pour des fonctionnalités personnalisées, vous pouvez opter pour une version payante. Auteur: github.com/kristiangasic")
        language_window.destroy()

    language_window = Toplevel(root)
    language_window.title("Select Language")
    language_window.geometry("400x250")
    language_window.configure(bg="#2e2e2e")

    ctk.CTkLabel(language_window, text="Please select your language:", 
                 font=("Helvetica", 12, "bold"), text_color="white", bg_color="#2e2e2e").pack(pady=10)

    language_var = StringVar(value="English")
    language_dropdown = ctk.CTkOptionMenu(language_window, values=["English", "Deutsch", "Français"], variable=language_var,
                                           font=("Helvetica", 10), fg_color="#2e2e2e", button_color="#4CAF50")
    language_dropdown.pack(pady=10)

    ctk.CTkButton(language_window, text="Confirm", command=lambda: set_language(language_var.get()), font=("Helvetica", 12), 
                  fg_color="#2e2e2e", bg_color="#4CAF50").pack(pady=20)

def open_donate_page():
    coffee_url = "https://buymeacoffee.com/kristiangasic"
    webbrowser.open(coffee_url)

root = ctk.CTk()
root.title("Custom File Sorter v1.3.0 - Kristian Gasic")
root.geometry("600x700")
root.configure(bg="#2e2e2e")

selected_directory = StringVar()
custom_folder = StringVar()
language_text = StringVar()

show_language_selection()

frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#333333")
frame.pack(pady=20, padx=20, fill="both", expand=True)

ctk.CTkLabel(frame, textvariable=language_text, wraplength=540, justify="left", font=("Helvetica", 12), text_color="white", bg_color="#333333").pack(pady=20)

ctk.CTkLabel(frame, text="Select a Directory:", font=("Helvetica", 12, "bold"), text_color="white", bg_color="#333333").pack(pady=5)
ctk.CTkButton(frame, text="Browse", command=select_directory, font=("Helvetica", 12), fg_color="#4CAF50", bg_color="#4CAF50").pack(pady=5)
ctk.CTkLabel(frame, textvariable=selected_directory, font=("Helvetica", 10), text_color="white", bg_color="#333333").pack(pady=5)

ctk.CTkLabel(frame, text="Select File Extensions:", font=("Helvetica", 12, "bold"), text_color="white", bg_color="#333333").pack(pady=5)

extension_var = StringVar(value=[])
extension_dropdown = ctk.CTkOptionMenu(frame, values=available_extensions, variable=extension_var, font=("Helvetica", 10), fg_color="#4CAF50", button_color="#4CAF50")
extension_dropdown.pack(pady=5)

ctk.CTkLabel(frame, text="Set Custom Destination Folder (optional):", font=("Helvetica", 12, "bold"), text_color="white", bg_color="#333333").pack(pady=5)
ctk.CTkButton(frame, text="Set Folder", command=set_custom_folder, font=("Helvetica", 12), fg_color="#4CAF50", bg_color="#4CAF50").pack(pady=5)
ctk.CTkLabel(frame, textvariable=custom_folder, font=("Helvetica", 10), text_color="#4CAF50", bg_color="#333333").pack(pady=5)

ctk.CTkButton(frame, text="Start Sorting", command=start_sorting, font=("Helvetica", 14, "bold"), fg_color="#4CAF50", bg_color="#4CAF50").pack(pady=20)

footer_frame = ctk.CTkFrame(root, corner_radius=10, fg_color="#333333")
footer_frame.pack(side="bottom", fill="both", padx=20, pady=20)

ctk.CTkButton(footer_frame, text="Buy Me a Coffee", command=open_donate_page, font=("Helvetica", 12), fg_color="#4CAF50", bg_color="#4CAF50").pack(pady=5)

root.mainloop()
