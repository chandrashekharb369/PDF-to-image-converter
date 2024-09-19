import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2image import convert_from_path
from PIL import Image

def select_pdf():
    pdf_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if pdf_path:
        pdf_entry.delete(0, tk.END)
        pdf_entry.insert(0, pdf_path)

def convert_pdf_to_images():
    pdf_path = pdf_entry.get()
    if not pdf_path:
        messagebox.showerror("Error", "Please select a PDF file.")
        return

    output_dir = filedialog.askdirectory()
    if not output_dir:
        messagebox.showerror("Error", "Please select an output directory.")
        return

    try:
        images = convert_from_path(pdf_path)
        for i, image in enumerate(images):
            image.save(f"{output_dir}/page_{i+1}.jpeg", "JPEG")
        messagebox.showinfo("Success", f"PDF converted to images successfully in {output_dir}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

# Create the main application window
root = tk.Tk()
root.title("PDF to JPEG Converter")

# Create and place widgets in the window
tk.Label(root, text="Select PDF File:").grid(row=0, column=0, padx=10, pady=10)

pdf_entry = tk.Entry(root, width=50)
pdf_entry.grid(row=0, column=1, padx=10, pady=10)

select_button = tk.Button(root, text="Browse...", command=select_pdf)
select_button.grid(row=0, column=2, padx=10, pady=10)

convert_button = tk.Button(root, text="Convert to JPEG", command=convert_pdf_to_images)
convert_button.grid(row=1, column=0, columnspan=3, pady=20)

# Run the application
root.mainloop()
