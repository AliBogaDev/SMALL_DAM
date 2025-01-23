import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from cell import Cell
from tkinter import messagebox


class DetailWindow:

    def on_boton_clicked(self, cell):
        message = "Mariposa: "+cell.title
        messagebox.showinfo("Información: "+message)

    def __init__(self, cell): #Ventana principal
        #Defino las varialbles para guardar los argumentos
        root = tk.Toplevel()
        label1 = ttk.Label(root, text=cell.title)
        label2 = ttk.Label(root, image=cell.image_tk)
        label3 = ttk.Label(root, text=cell.description, wraplength=160)

        label1.pack(side="top")
        label2.pack()
        label3.pack() #Muestra la información al clickear en la imagen

