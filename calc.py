import customtkinter, random

root = customtkinter.CTk()
root.geometry("400x500")
root.title("Calculadora de ensayos destructivos")
def actualizar_etiqueta():
    etiqueta1.configure(state="disabled")

etiqueta1 = customtkinter.CTkButton(master=root, text="¡Hola mundo!")
etiqueta1.place(x=100, y=70)

root.after(2000, actualizar_etiqueta)

root.mainloop()


