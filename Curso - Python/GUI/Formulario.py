from tkinter import *
from tkinter import ttk
root = Tk()
root.geometry("500x400")
root.title("Formulario")

panel_main = ttk.Frame(root, padding=10)
panel_main.grid()

panel_izq = ttk.Frame(panel_main,padding=10,border=1, relief=SUNKEN)
panel_izq.grid(column=0,row=0)

panel_der = ttk.Frame(panel_main,padding=10)
panel_der.grid(column=1,row=0)

panel_bajo = ttk.Frame(panel_main,padding=10)
panel_bajo.grid(column=0,row=1,columnspan=2)

panel_aficiones = ttk.Frame(panel_bajo,padding=5,border=1, relief=SUNKEN)

panel_aficiones.grid(column=0,row=0,columnspan=2)


#p1 = PanedWindow()
#p1.pack(fill=BOTH, expand=1)

#left = Label(p1, text="Left Panel")
#p1.add(left)




ttk.Label(panel_izq, text="Nombre:").grid(column=0, row=0, pady=10)
ttk.Label(panel_izq, text="A. Paterno:").grid(column=0, row=1,pady=10)
ttk.Label(panel_izq, text="A. Materno:").grid(column=0, row=2,pady=10)
ttk.Label(panel_izq, text="Correo:").grid(column=0, row=3,pady=10)
ttk.Label(panel_izq, text="Movil:").grid(column=0, row=4,pady=10)

ttk.Entry(panel_izq, text="").grid(column=1, row=0)
ttk.Entry(panel_izq, text="").grid(column=1, row=1)
ttk.Entry(panel_izq, text="").grid(column=1, row=2)
ttk.Entry(panel_izq, text="").grid(column=1, row=3)
ttk.Entry(panel_izq, text="").grid(column=1, row=4)

ttk.Radiobutton(panel_der, text="Estudiante").grid(column=0, row=0,pady=2,padx=2)
ttk.Radiobutton(panel_der, text="Empleado").grid(column=0, row=1,pady=2,padx=2)
ttk.Radiobutton(panel_der, text="Desempleado").grid(column=0, row=2,pady=2,padx=2)



ttk.Label(panel_aficiones, text="Aficiones:").grid(column=0, row=0)

ttk.Checkbutton(panel_aficiones, text="Leer").grid(column=0, row=1)
ttk.Checkbutton(panel_aficiones, text="Musica").grid(column=1, row=1)
ttk.Checkbutton(panel_aficiones, text="VideoJuegos").grid(column=2, row=1)

ttk.Combobox(panel_bajo,values=['Estados (32)']).grid(column=2, row=0,padx=20)

ttk.Button(panel_bajo, text="Guardar").grid(column=0, row=1,pady=10)
ttk.Button(panel_bajo, text="Cancelar").grid(column=1, row=1,pady=10)

root.mainloop()