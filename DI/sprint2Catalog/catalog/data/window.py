from tkinter import Canvas, Frame, Label, Scrollbar, ttk
import tkinter as tk
from tkinter import messagebox
from cell import Cell
from detail_window import DetailWindow



class MainWindow():

    def on_button_clicked(self, cell):
        DetailWindow(cell)


        
    # Inicializo una lista vacia de cell
    def __init__(self, root, json_data):
        root.title("Mi Mariposuario")
        root.geometry("400x300")
        self.cells = [] 

        #recorro cada cell
        for i in json_data:
            name = i.get("name")
            description = i.get("description")
            url = i.get("image_url")
            
            self.cells.append(Cell(name, description, url))

   
         
        #Información del desarrollador
        menubar = tk.Menu(root)
        ayuda_menu = tk.Menu(menubar, tearoff=False)
        ayuda_menu.add_command(label="Acerca de", command=self.acerca_de)
        menubar.add_cascade(label="Ayuda", menu=ayuda_menu)


        #Ventana principal
        self.canvas = Canvas(root, width=200, height=300)


        #Creo el scroll con canvas y tkinter para recorrer las imagenes con una barra
   
        self.scrollbar = Scrollbar(root, orient = "vertical", command = self.canvas.yview)
        self.scrollable_frame = Frame(self.canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(
                scrollregion = self.canvas.bbox("all")))

        self.canvas.create_window((0, 0), window = self.scrollable_frame, anchor = "nw")
        self.canvas.configure(yscrollcommand = self.scrollbar.set)

        for i, cell in enumerate(self.cells):
            self.add_item(cell,i)

        self.canvas.grid(row = 0, column = 0, sticky = "nsew")
        self.scrollbar.grid(row = 0, column = 1, sticky = "ns")


        
    def add_item(self, cell, i):

        frame = Frame(self.scrollable_frame)
        frame.pack(pady = 10, anchor="center")
        
        label = Label(frame, image = cell.image_tk, text = cell.title, compound = tk.BOTTOM)
        label.pack(anchor="center")
        label.bind("<Button-1>", lambda event, cell = cell: DetailWindow(cell) )

        #Este es mi mensage de ayuda
    def acerca_de(self):
        messagebox.showinfo("Acerca del desarrollador", "Este programa fue desarrollado por Alicia.")
