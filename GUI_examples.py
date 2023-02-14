#*******************************************************************************
#* EJEMPLO DE WIDGETS DE INTERFACE GRAFICA CON TKINTER
#* DESARROLLADOR: Necrovalle
#* VERSION: 0.1 ALPHA
#* REPOSITORIO:
#* URL: https://github.com/Necrovalle/ejemplo.git
#* Notas: Solo se utilizan widgets nativos de la libreria
#*******************************************************************************

#***************************************************************** IMPORTACIONES
from tkinter import *		    # Widgets estandar
from tkinter import ttk		    # Widgets nuevos del 8.5+
from tkinter import messagebox  # Ventana de mensajes
#******************************************************** DECLARACIONES GLOBALES

#************************************************************* FUNCIONES PROPIAS
def fcnClick0():
    lbl0.config(text='Diste click :)')
    
def fcnMensaje():
    messagebox.showinfo(message="Notificacion importante aqui", title="Aviso...")
    
def fcnCaptura():
    txtEnt = ent0.get()
    lbl2.config(text=txtEnt)
    ent0.delete(0, END)
    
def Opcion1():
    if Opc1.get():
        lbl4.config(text='Opcion 1 seleccionada')
    else:
        lbl4.config(text='Opcion 1 deseleccionada')

#********************************************************************* PRINCIPAL
# Creacion y configuracion de la ventana principal
window = Tk()                       # Ventana principal
Opc1 = IntVar()                     #Variable para capturar checkbutton
window.geometry('1000x600+10+10')   # Configuracion de tamaño y posicion
window.resizable(False, False)      # Condiciones de retamaño 
window.title('Ejemplos de widgets en TKinter')# Titulo en la ventana
window.iconbitmap('pyWin.ico') # Icono de la ventana principal

vlist = ["Opcion1", "Opcion2", "Opcion3", "Opcion4", "Opcion5"]

# Creacion de los elementos (widgets)
lbl0 = Label (window, text='Mensaje en una etiqueta')
btn0 = Button(window, text=" Click  me!!!  ", command = fcnClick0)
lbl1 = Label (window, text='Ventana de mensaje:')
btn1 = Button(window, text='MsgBox aqui', command = fcnMensaje)
ent0 = Entry (window, width=19)
btn2 = Button(window, text='Capturar Ent', command = fcnCaptura)
lbl2 = Label (window, text='...')
lbl3 = Label (
    window, text='Texto modificado',
    font=("Verdana 12 bold"), 
    fg="blue")
che0 = Checkbutton(window, text = 'Seleccion 1', variable=Opc1 ,command=Opcion1)
lbl4 = Label (window, text='...')
cmb0 = ttk.Combobox(window, values = vlist, width=29)
cmb0.set("Selecciona...")

#Posicionamiento de los widgetsen la ventana
lbl0.place(x=20, y=12)
btn0.place(x=190, y=10)
lbl1.place(x=20, y=62)
btn1.place(x=190, y=60)
ent0.place(x=20, y=115)
btn2.place(x=190, y=110)
lbl2.place(x=20, y=150)
lbl3.place(x=20, y=190)
che0.place(x=20, y=230)
lbl4.place(x=20, y=260)
cmb0.place(x=20, y=290)

# Fuincion loop de manejo de eventos de la ventana
window.mainloop()
#*************************************************************** FINAL DE SCRIPT
# cmd /k cd "$(CURRENT_DIRECTORY)" && python "$(FILE_NAME)"