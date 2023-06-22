
import tkinter as tk

import socket

ventana = tk.Tk()
ventana.title("Direccion IP")
ventana.geometry("400x200")

a= socket.gethostbyname(socket.gethostname())

dir = "Direccion IP:", a


lblMensaje2 = tk.Label(ventana, text= dir, fg='blue', justify=tk.LEFT).pack()

ventana.mainloop()





