import tkinter as tk
from tkinter import messagebox, filedialog
import qrcode
from PIL import Image, ImageTk

class QRCodeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Generador de Código QR")

        # Etiqueta y entrada para los datos del código QR
        self.label = tk.Label(root, text="Introduce los datos para el código QR:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, width=50)
        self.entry.pack(pady=10)

        # Botón para generar el código QR
        self.generate_button = tk.Button(root, text="Generar QR", command=self.generate_qr)
        self.generate_button.pack(pady=10)

        # Botón para guardar el código QR
        self.save_button = tk.Button(root, text="Guardar QR", command=self.save_qr)
        self.save_button.pack(pady=10)

        # Área para mostrar la imagen del código QR
        self.qr_image_label = tk.Label(root)
        self.qr_image_label.pack(pady=10)

        self.qr_image = None

    def generate_qr(self):
        data = self.entry.get()
        if not data:
            messagebox.showwarning("Advertencia", "Por favor, introduce los datos para el código QR.")
            return

        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )
        qr.add_data(data)
        qr.make(fit=True)

        img = qr.make_image(fill_color="black", back_color="white")
        self.qr_image = img
        img_filename = "qrcode.png"
        img.save(img_filename)

        # Mostrar la imagen en la aplicación
        self.display_qr(img_filename)

    def display_qr(self, img_filename):
        image = Image.open(img_filename)
        photo = ImageTk.PhotoImage(image)

        self.qr_image_label.config(image=photo)
        self.qr_image_label.image = photo

    def save_qr(self):
        if self.qr_image:
            file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
            if file_path:
                self.qr_image.save(file_path)
                messagebox.showinfo("Éxito", f"Código QR guardado como {file_path}")
        else:
            messagebox.showwarning("Advertencia", "Primero genera un código QR antes de intentar guardarlo.")

if __name__ == "__main__":
    root = tk.Tk()
    app = QRCodeApp(root)
    root.mainloop()
