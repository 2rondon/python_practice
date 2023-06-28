from tkinter import *
from tkinter.ttk import *

index=Tk()
index.title("login")
index.geometry("300x150")
index.resizable(width=False, height=False)

lusu=Label(index, text="Ingresar Usuario:")
lusu.pack()

user=StringVar()
eusu=Entry(index, width=30, textvariable=user)
eusu.pack()

lusu=Label(index, text="Contraseña:")
lusu.pack()

pas=StringVar()
epas=Entry(index, width=30, show='*', textvariable=pas )
epas.pack()

def ingresar():
    if user.get()=="maria" and pas.get()=="123456":
       index.title("Correcto")
    else:
       index.title("incorrecto")




bl=Button(index, text="Entrar", command=ingresar)
bl.pack()


index.mainloop()
