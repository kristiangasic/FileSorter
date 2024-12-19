import os
import shutil
from tkinter import Tk, filedialog, Label, Button, Entry, StringVar, Listbox, MULTIPLE, Toplevel, Radiobutton, IntVar
from datetime import datetime

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

                # Handle specific naming patterns if required
                if "invoice" in file.lower():
                    invoice_number = file.split("_")[0] if "_" in file else "UNKNOWN"
                    new_name = f"{invoice_number}_Invoice_{creation_date}.{file_ext}"

                new_path = os.path.join(destination_folder, new_name)

                # Avoid overwriting files
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

    selected_extensions = [file_extensions_listbox.get(i) for i in file_extensions_listbox.curselection()]
    if not selected_extensions:
        print("Please select at least one file extension.")
        return

    sort_files(directory, selected_extensions, custom_folder.get())

def show_language_selection():
    def set_language():
        language = language_var.get()
        if language == 1:
            language_text.set("Welcome! This is an Open Source project. For custom features, you can opt for a paid version. Author: github.com/kristiangasic")
        elif language == 2:
            language_text.set("Willkommen! Dies ist ein Open-Source-Projekt. Für benutzerdefinierte Funktionen können Sie eine kostenpflichtige Version wählen. Autor: github.com/kristiangasic")
        elif language == 3:
            language_text.set("Bienvenue! Ceci est un projet Open Source. Pour des fonctionnalités personnalisées, vous pouvez opter pour une version payante. Auteur: github.com/kristiangasic")
        language_window.destroy()

    language_window = Toplevel(root)
    language_window.title("Select Language")
    language_window.geometry("400x200")

    Label(language_window, text="Please select your language / Sprache wählen / Choisissez votre langue:").pack(pady=10)

    language_var = IntVar(value=1)
    Radiobutton(language_window, text="English", variable=language_var, value=1).pack(anchor="w")
    Radiobutton(language_window, text="Deutsch", variable=language_var, value=2).pack(anchor="w")
    Radiobutton(language_window, text="Français", variable=language_var, value=3).pack(anchor="w")

    Button(language_window, text="Confirm", command=set_language).pack(pady=20)

# GUI Setup
root = Tk()
root.title("Custom File Sorter")
root.geometry("500x600")

selected_directory = StringVar()
custom_folder = StringVar()
language_text = StringVar()

show_language_selection()

Label(root, textvariable=language_text, wraplength=480, justify="left").pack(pady=10)

Label(root, text="Select a Directory:").pack(pady=5)
Button(root, text="Browse", command=select_directory).pack(pady=5)
Label(root, textvariable=selected_directory).pack(pady=5)

Label(root, text="Select File Extensions (e.g., pdf, txt, jpg, zip, rar, mp3, mp4):").pack(pady=5)
file_extensions_listbox = Listbox(root, selectmode=MULTIPLE, height=15)
file_extensions_listbox.pack(pady=5)
for ext in ["pdf", "jpg", "png", "mp4", "txt", "php", "js", "zip", "rar", "mp3", "mp4"]:
    file_extensions_listbox.insert("end", ext)

Label(root, text="Set Custom Destination Folder (optional):").pack(pady=5)
Button(root, text="Set Folder", command=set_custom_folder).pack(pady=5)
Label(root, textvariable=custom_folder).pack(pady=5)

Button(root, text="Start Sorting", command=start_sorting).pack(pady=20)

root.mainloop()
