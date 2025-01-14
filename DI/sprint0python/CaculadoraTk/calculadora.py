from tkinter import *
from math import *

from operaciones import suma, resta, multiplicacion, division #llamo a los métodos

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600") #Creo tamaño de la vetana

#Salida de la calculadora
salida = Entry(
    ventana, #se muestra dentro de la ventana
    font=("Arial", 20, "bold"), #la fuente
    width=20, #ancho de la  vetana
    bd=22, #grasor del  borde
    bg="pink", #blcolor
    insertwidth=4, #la linea que parpadea dentro de la ventana del la calculadora
    justify="center" # justificación
)
salida.place(x=10,y=60)

ancho_boton =11
alto_boton =3

#Creo los botones: el texto que se muestra en el boton, anchura y altura  y lo posiciono con place
Boton0 = Button(ventana, text="0", width=ancho_boton, height= alto_boton).place(x=17,y=180)


"""
def solicitar_numeros(): #creo otra función
    num1 = int(input("1º número: "))
    num2 = int(input("2º número: "))
    return num1, num2

def realizar_operacion(operacion, num1, num2): #utilizo los métodos dentro de una nueva función que llamaré más tarde
    if operacion == "suma":
        return suma(num1, num2)
    elif operacion == "resta":
        return resta(num1, num2)
    elif operacion == "multiplicacion":
        return multiplicacion(num1, num2)
    elif operacion == "division":
        if num2 == 0:
            return "Error: División por cero"
        else:
            return division(num1, num2)
    else:
        return "Operación no reconocida"

respuesta = 's'

while respuesta.lower() == 's':
    num1, num2 = solicitar_numeros()
    operacion = input("¿Qué operación desea realizar? (\n- Suma \n- Resta \n- Multiplicación \n- Division ")
    resultado = realizar_operacion(operacion.lower(), num1, num2)
    print("El resultado es: " + str(resultado))
    respuesta = input("¿Desea realizar otra operación (s/n)? ")
"""
ventana.mainloop() #Abrir ventana