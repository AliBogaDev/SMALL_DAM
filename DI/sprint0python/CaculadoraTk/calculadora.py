
from tkinter import *
from math import *




#Defino la función para la entrada de números que aceptará una variable
def btnClick(num):
    global operador
    operador = operador + str(num)
    input_text.set(operador)

#Defino la funcíon que realizará la operación
def operation():
    global operador
    try:
        opera=str(eval(operador))
        input_text.set(opera)
    except:
        opera=("ERRORCITO")
        operador=""

#Defino la función que limpia la pantalla para realizar nuevos calculos
def clear():
    global operador
    operador=("")
    input_text.set("0")

ventana = Tk()
ventana.title("CALCULADORA")
ventana.geometry("392x600") #Creo tamaño de la vetana

# Variables para la función click_botton, importante ponelo debajo de la ventana para llamarla
input_text = StringVar()
operador =""





#Tamaño de los botones
ancho_boton = 11
alto_boton =3

#Defino el color del fondo de la calculadora, el color de los botobes esta definido en ella misma
ventana.configure(background="SkyBlue1")

#Creo los botones: el texto que se muestra en el boton, anchura y altura  y lo posiciono con place. LLamo tambien a la función de Click del botón
Boton_0 = Button(ventana, text="0", width=ancho_boton, height= alto_boton, command=lambda:btnClick(0), bg="grey").place(x=17,y=180)
Boton_1 = Button(ventana, text="1", width=ancho_boton, height= alto_boton, command=lambda:btnClick(1), bg="grey").place(x=107,y=180)
Boton_2 = Button(ventana, text="2", width=ancho_boton, height= alto_boton, command=lambda:btnClick(2), bg="grey").place(x=197,y=180)
Boton_3 = Button(ventana, text="3", width=ancho_boton, height= alto_boton, command=lambda:btnClick(3), bg="grey").place(x=287,y=180)
Boton_4 = Button(ventana, text="4", width=ancho_boton, height= alto_boton, command=lambda:btnClick(4), bg="grey").place(x=17,y=240)
Boton_5 = Button(ventana, text="5", width=ancho_boton, height= alto_boton, command=lambda:btnClick(5), bg="grey").place(x=107,y=240)
Boton_6 = Button(ventana, text="6", width=ancho_boton, height= alto_boton, command=lambda:btnClick(6),  bg="grey").place(x=197,y=240)
Boton_7 = Button(ventana, text="7", width=ancho_boton, height= alto_boton, command=lambda:btnClick(7), bg="grey").place(x=287,y=240)
Boton_8= Button(ventana, text="8", width=ancho_boton, height= alto_boton, command=lambda:btnClick(8), bg="grey").place(x=17,y=300)
Boton_9= Button(ventana, text="9", width=ancho_boton, height= alto_boton, command=lambda:btnClick(9), bg="grey").place(x=107,y=300)
Boton_pi = Button(ventana, text="π", width=ancho_boton, height= alto_boton, command=lambda:btnClick("pi"), bg="grey").place(x=197,y=300)
Boton_coma = Button(ventana, text=",", width=ancho_boton, height= alto_boton, command=lambda:btnClick(","), bg="grey").place(x=287,y=300)
Boton_mas = Button(ventana, text="+", width=ancho_boton, height= alto_boton, command=lambda:btnClick("+"), bg="grey").place(x=17,y=360)
Boton_menos = Button(ventana, text="-", width=ancho_boton, height= alto_boton, command=lambda:btnClick("-"), bg="grey").place(x=107,y=360)
Boton_por= Button(ventana, text="*", width=ancho_boton, height= alto_boton, command=lambda:btnClick("*"), bg="grey").place(x=197,y=360)
Boton_div= Button(ventana, text="/", width=ancho_boton, height= alto_boton, command=lambda:btnClick("/"), bg="grey").place(x=287,y=360)
Boton_raiz = Button(ventana, text="√", width=ancho_boton, height= alto_boton, command=lambda:btnClick("sqrt("), bg="grey").place(x=17,y=420)
Boton_par1= Button(ventana, text="(", width=ancho_boton, height= alto_boton, command=lambda:btnClick("("), bg="grey").place(x=107,y=420)
Boton_par2 = Button(ventana, text=")", width=ancho_boton, height= alto_boton, command=lambda:btnClick(")"), bg="grey").place(x=197,y=420)
Boton_mod = Button(ventana, text="%", width=ancho_boton, height= alto_boton, command=lambda:btnClick("%"),bg="grey").place(x=287,y=420)
Boton_log = Button(ventana, text="ln", width=ancho_boton, height= alto_boton, command=lambda:btnClick("log("), bg="grey").place(x=17,y=480)
Boton_lim = Button(ventana, text="C", width=ancho_boton, height= alto_boton, command=clear, bg="grey").place(x=107,y=480)
Boton_pot = Button(ventana, text="EXP", width=ancho_boton, height= alto_boton, command=lambda:btnClick("**"), bg="grey").place(x=197,y=480)
Boton_res = Button(ventana, text="=", width=ancho_boton, height= alto_boton, command=operation, bg="grey").place(x=287,y=480)

#Salida de la calculadora
salida = Entry(
    ventana, #se muestra dentro de la ventana
    font=("Arial", 20, "bold"), #la fuente
    width=20, #ancho de la  vetana
    bd=22, #grasor del  borde
    bg="light blue", #blcolor
    insertwidth=4, #la linea que parpadea dentro de la ventana del la calculadora
    justify="left", # justificación de la linea que parpadea
    textvariable=input_text #variable que muestra el texto en la ventana
)
salida.place(x=22,y=65)
#Limpiar pantalla
clear()
#Abrir ventana
ventana.mainloop() 