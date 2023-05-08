from tkinter import *
from tkinter import ttk
root = Tk()
frm = ttk.Frame(root, padding=10)
root.title("Inicio de sesion")
frm.grid()
ttk.Label(frm, text="Usuario").grid(column=0, row=0)
ttk.Label(frm, text="Contraseña").grid(column=0, row=1)

ttk.Entry(frm, text="").grid(column=1, row=0)
ttk.Entry(frm, text="").grid(column=1, row=1)
root.mainloop()
