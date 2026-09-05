from PIL import Image, ImageOps
import tkinter as tk
from tkinter import filedialog, messagebox

def resize_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.jpeg *.png *.bmp *.webp")])
    if not file_path:
        return
    try:
        img = Image.open(file_path)
        img = ImageOps.contain(img, (256, 256))
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG file", "*.png"), ("JPEG file", "*.jpg")])
        if save_path:
            img.save(save_path)
            messagebox.showinfo("Success", "Image saved successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title("Image Resizer")
root.geometry("256x256")
btn = tk.Button(root, text="Select and Shrink Image", command=resize_image)
btn.pack(expand=True)
root.mainloop()
