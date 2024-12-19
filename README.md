# File Sorter with GUI

## Overview
This is an **Open Source** Python project that provides a graphical user interface (GUI) for sorting files based on their extensions. The script allows users to select directories, define specific file types to sort, and organize files into folders with customized naming patterns. The program supports multiple languages (English, German, and French) and includes advanced customization options.

**Author:** [Kristian Gasic](https://github.com/kristiangasic)

---

## Features

1. **Custom File Extensions:**
   - Select specific file types (e.g., PDF, MP3, MP4, ZIP, RAR).
   - Sort files by extensions into categorized folders.

2. **Custom Destination Folder:**
   - Option to set a custom folder for sorted files.
   - Default location: Desktop in a folder named `Sorted_Files`.

3. **Automatic Naming:**
   - Files are renamed with their creation date as a prefix (e.g., `2023-01-01_filename.pdf`).
   - Special naming for invoices (e.g., `InvoiceNumber_Invoice_Date.pdf`).

4. **Multilingual Support:**
   - Languages: English, German, French.
   - Language selection displayed on startup.

5. **Open Source:**
   - This project is open source and free to use.
   - Paid versions with additional features are available upon request.

---

## How It Works

### Steps:

1. **Select a Directory:**
   - Choose the folder you want to organize.

2. **Choose File Extensions:**
   - Select the file types to sort (e.g., PDFs, images, videos, compressed files).

3. **Set a Custom Folder (Optional):**
   - Define a destination folder where sorted files will be saved.
   - If not set, files are saved to the Desktop.

4. **Start Sorting:**
   - Click the `Start Sorting` button to begin.
   - Files will be moved and renamed based on the defined settings.

5. **Language Support:**
   - Choose your preferred language at startup.

---

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/kristiangasic/FileSorter.git
   cd FileSorter
   ```

2. Install required dependencies:

   ```bash
   pip install tkinter customtkinter
   ```

3. Run the script:

   ```bash
   python filesorter.py
   ```

---

## Create an Executable (Windows)

1. Install PyInstaller:

   ```bash
   pip install pyinstaller
   ```

2. Generate the executable:

   ```bash
   pyinstaller --noconfirm --onefile --windowed filesorter.py
   ```

3. The `.exe` file will be located in the `dist` folder.

4. Optionally, add a custom icon:

   ```bash
   pyinstaller --noconfirm --onefile --windowed --icon=icon.ico filesorter.py
   ```

---

## Example Use Case

1. Select a folder containing unsorted files (e.g., `Downloads`).
2. Choose to sort only `PDF` and `MP4` files.
3. Set a custom destination folder, such as `C:/SortedFiles`.
4. Run the script to organize your files with names based on their creation date.

---

## Contributing

Feel free to contribute to this project by submitting issues or pull requests on [GitHub](https://github.com/kristiangasic).


---


[![Buy Me A Coffee](https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png)](https://www.buymeacoffee.com/kristiangasic)



## Support

For questions or support, contact the author on GitHub or request a paid version for more advanced features.

