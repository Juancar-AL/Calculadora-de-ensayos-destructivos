import customtkinter
import brinell
import tkinter as tk

def cambiar_apariencia():
    global estado
    estado = not estado
    customtkinter.set_appearance_mode("light" if estado else "dark")

def calcular_ensayo():
    # Verificar si los CTkEntry están vacíos y asignar None si es el caso
    result_value = float(entry1.get()) if entry1.get() else None
    force_value = float(entry2.get()) if entry2.get() else None
    diameter_value = float(entry3.get()) if entry3.get() else None
    indentation_diameter_value = float(entry4.get()) if entry4.get() else None
    hardness_constant_value = float(entry5.get()) if entry5.get() else None
    
    # Pasar los valores a la función brinell.valores
    brinell.valores(brinell.brinell_instance, force=force_value, result=result_value,
                    diameter=diameter_value, indentation_diameter=indentation_diameter_value,
                    hardness_constant=hardness_constant_value)
    
    # Llamar a la función ensayo y obtener el resultado
    brinell.ensayo(brinell.brinell_instance)
    
    # Actualizar el widget result con el resultado de la función ensayo
    result.configure(text=f"{brinell.brinell_instance.result} HB | {brinell.brinell_instance.diameter} mm | {brinell.brinell_instance.indentation_diameter} mm | {brinell.brinell_instance.force} kp | {'El ensayo es fiable' if brinell.brinell_instance.fiability else 'El ensayo no es fiable'}")

# Crear la ventana principal
root = customtkinter.CTk()
root.geometry("500x315")
root.title("Calculadora de ensayo Brinell")

# Widgets
frame3 = customtkinter.CTkLabel(root, width=500, height=50, text="Ensayo Brinell")
frame = customtkinter.CTkFrame(root)
frame2 = customtkinter.CTkFrame(root)
entry1 = customtkinter.CTkEntry(frame, placeholder_text="Resultado ensayo")
entry2 = customtkinter.CTkEntry(frame, placeholder_text="Fuerza")
entry3 = customtkinter.CTkEntry(frame, placeholder_text="Diámetro identador")
entry4 = customtkinter.CTkEntry(frame2, placeholder_text="Diámetro huella")
entry5 = customtkinter.CTkEntry(frame2, placeholder_text="Constante del ensayo")
frame_r = customtkinter.CTkFrame(root)
result = customtkinter.CTkLabel(frame_r, text="Resultado")
boton_tema = customtkinter.CTkButton(root, text="Tema", command=cambiar_apariencia, width=10)
etiqueta1 = customtkinter.CTkButton(master=root, text="Calcular ensayo", command=calcular_ensayo)

# Posicionamiento de los widgets
frame3.pack()
frame.pack(padx=0, pady=10, anchor=tk.S)
frame2.pack(padx=0, pady=5, anchor=tk.S)
entry1.pack(padx=5, pady=5, side="left")
entry2.pack(padx=5, pady=5, side="left")
entry3.pack(padx=5, pady=5, side="left")
entry4.pack(padx=5, pady=5, side="left")
entry5.pack(padx=5, pady=5, side="left")
etiqueta1.pack(padx=0.5, pady=10, anchor=tk.CENTER)
frame_r.pack(padx=0.5, pady=5, anchor=tk.CENTER)
result.pack(padx=7, anchor=tk.CENTER)
boton_tema.pack(padx=20, pady=5, side="right", anchor=tk.E)

estado = False

# Iniciar el bucle de eventos
root.mainloop()
