from typing import Optional, Tuple, Union
from customtkinter import *
from tkinter import *
from calc.brinell import Brinell, brinell_valores, brinell_ensayo
from calc.vickers import Vickers, vickers_valores, vickers_ensayo
from PIL import Image

image = CTkImage(light_image=Image.open("others/theme.png"))

estado = False
ensayo_b = False
ensayo_v = False

brinell_instance = Brinell()
vickers_instance = Vickers()

class MainApp(CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Calculadora de ensayos destructivos")
        self.geometry("700x300")
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0,2), weight=2)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure((2,3), weight=3)
        self.iconbitmap("others/icon.ico")
        self.resizable(False, False)

        self.frame = CTkFrame(self)
        self.button1 = CTkButton(self, text="Ensayo Brinell",command=self.mostrar_ensayo_b, corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2",width=150,)
        self.button2 = CTkButton(self, text="Ensayo Vickers",command=self.mostrar_ensayo_v, corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2",width=150,)
        self.label = CTkLabel(self, text = "Calculadora de ensayos destructivos", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.label2 = CTkLabel(self, text = "Por Juan Carlos Alonso Luengo", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.tema = CTkButton(self, image=image, text="Apariencia",  command=cambiar_apariencia, fg_color = ("#353D3A", "#A4A7A6"), text_color = "#FFFFFF", hover_color=("#5A6863", "#787878"), width=150, corner_radius=100)


        self.result1 = CTkLabel(self, width=150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result3 = CTkLabel(self, text = "Diametro huella", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.result4 = CTkLabel(self, text="Fuerza utilizada", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.result5 = CTkLabel(self, text="Fiabilidad", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100) 

        self.button = CTkButton(self, text="Calcular ensayo", corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=150)
        self.entry3 = CTkEntry(self, corner_radius = 100, width=150)
        self.entry4 = CTkEntry(self, corner_radius = 100, width=150)
        self.result2 = CTkLabel(self, width=150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)


        self.entry1 = CTkEntry(self ,corner_radius = 100, width=150)
        self.entry2 = CTkEntry(self, placeholder_text="Fuerza",corner_radius = 100, width=150)
        self.entry5 = CTkEntry(self, placeholder_text="Constante ensayo",corner_radius = 100, width=150)
        self.tema_e = CTkButton(self, image=image, text="Tema", command=cambiar_apariencia ,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=5)
        self.back = CTkButton(self, text="Volver", command=self.mostrar_principal,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=5)
        self.datos = CTkLabel(self, text="Datos", width=150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.res = CTkLabel(self, text="Resultados", width=150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.error = CTkLabel(self, text="Has de rellenar al menos dos variables", text_color="red")
    def ocultar_principal(self):
        self.tema.grid_forget()
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.label.grid_forget()
        self.label2.grid_forget()
    def mostrar_principal(self):
        global ensayo_b, ensayo_v
        if ensayo_b:
            self.ocultar_ensayo_b()
            ensayo_b = False
        elif ensayo_v:
            self.ocultar_ensayo_v()
            ensayo_v = False
        self.button1.grid(column=0, row = 1, padx = 20, pady = 20, sticky = "nsew")
        self.button2.grid(column=2, row = 1, padx = 20, pady = 20, sticky = "nsew")
        self.label.grid(column = 0, row = 0, padx = 20, pady = 20, sticky = "nsew", columnspan = 3)
        self.label2.grid(column = 0, row = 2, padx = 20, pady = 20, sticky = "nsew", columnspan = 2)
        self.tema.grid(row=2, column=2, pady=20, padx=20, sticky = "nsew")


    def ocultar_ensayo_b(self):
        self.entry1.grid_forget()
        self.entry2.grid_forget()
        self.entry3.grid_forget()
        self.entry4.grid_forget()
        self.entry5.grid_forget()
        self.datos.grid_forget()
        self.res.grid_forget()
        self.error.grid_forget()
        self.button.grid_forget()
        self.result1.grid_forget()
        self.result2.grid_forget()
        self.result3.grid_forget()
        self.result4.grid_forget()
        self.result5.grid_forget()
        self.tema_e.grid_forget()
        self.back.grid_forget()
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.entry4.delete(0, END)
        self.entry5.delete(0, END)

    def mostrar_ensayo_b(self):
        global ensayo_b
        ensayo_b = True
        self.button.configure(command = self.calcular_ensayo_b)
        self.entry1.configure(placeholder_text="Resultado ensayo")
        self.entry2.configure(placeholder_text="Fuerza utilizada")
        self.entry3.configure(placeholder_text="Diámetro identador")
        self.entry4.configure(placeholder_text="Diámetro huella")
        self.entry5.configure(placeholder_text="Constante ensayo")
        self.result1.configure(text="Resultado ensayo")
        self.result2.configure(text = "Diametro indendador")
        self.result3.configure(text="Diametro huella")
        self.result4.configure(text="Fuerza utilizada")
        self.result5.configure(text="Fiabilidad")
        self.entry1.grid(row=2, column=0, pady=10, padx=20)
        self.entry2.grid(row=5, column=0, pady=10, padx=20)
        self.entry3.grid(row=3, column=0, pady=10, padx=20)
        self.entry4.grid(row=4, column=0, pady=10, padx=20)
        self.entry5.grid(row=6, column=0, pady=10, padx=20)
        self.button.grid(row=3, column=2, pady=10, padx=20)
        self.datos.grid(row=1, column=0, pady=10, padx=20)
        self.res.grid(row=1, column=3, pady=10, padx=20)
        self.error.grid(row = 2, column= 2, pady=10, padx=20)
        self.result1.grid(row=2, column=3, pady=10, padx=20)
        self.result2.grid(row=3, column=3, pady=10, padx=20)
        self.result3.grid(row=4, column=3, pady=10, padx=20)
        self.result4.grid(row=5, column=3, pady=10, padx=20)
        self.result5.grid(row=6, column=3, pady=10, padx=20)
        self.tema_e.grid(row=6, column=2, pady=10, padx=20)
        self.back.grid(row=5, column=2, pady=10, padx=20)
        self.ocultar_principal()
            
    def mostrar_ensayo_v(self):
        global ensayo_v
        ensayo_v = True
        self.button.configure(command = self.calcular_ensayo_v)
        self.entry3.configure(placeholder_text="Diámetro 1")
        self.entry4 .configure(placeholder_text="Diámetro 2")
        self.entry1.configure(placeholder_text="Resultado ensayo")
        self.entry2.configure(placeholder_text="Fuerza utilizada")
        self.result1.configure(text="Resultado ensayo")
        self.result2.configure(text = "Diametro")
        self.result4.configure(text="Fuerza utilizada")
        self.error.grid(row = 2, column= 2, pady=10, padx=20)
        self.entry1.grid(row=2, column=0, pady=10, padx=20)
        self.entry2.grid(row=5, column=0, pady=10, padx=20)
        self.entry3.grid(row=3, column=0, pady=10, padx=20)
        self.entry4.grid(row=4, column=0, pady=10, padx=20)
        self.button.grid(row=3, column=2, pady=10, padx=20)
        self.datos.grid(row=1, column=0, pady=10, padx=20)
        self.res.grid(row=1, column=3, pady=10, padx=20)
        self.result1.grid(row=2, column=3, pady=10, padx=20)
        self.result2.grid(row=3, column=3, pady=10, padx=20)
        self.result4.grid(row=4, column=3, pady=10, padx=20)
        self.tema_e.grid(row=5, column=2, pady=10, padx=20)
        self.back.grid(row=4, column=2, pady=10, padx=20)
        self.ocultar_principal()
    
    def ocultar_ensayo_v(self):
        self.entry1.grid_forget()
        self.entry2.grid_forget()
        self.entry3.grid_forget()
        self.entry4.grid_forget()
        self.button.grid_forget()
        self.datos.grid_forget()
        self.res.grid_forget()
        self.error.grid_forget()
        self.result1.grid_forget()
        self.result2.grid_forget()
        self.result4.grid_forget()
        self.tema_e.grid_forget()
        self.back.grid_forget()
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry4.delete(0, END)

    def calcular_ensayo_v(self):
        
        self.result_value = float((self.entry1.get()).replace(",", ".")) if self.entry1.get() else None
        self.force_value = float(self.entry2.get().replace(",", ".")) if self.entry2.get() else None
        self.diameter_value_1 = float(self.entry3.get().replace(",", ".")) if self.entry3.get() else None
        self.diameter_value_2 = float(self.entry4.get().replace(",", ".")) if self.entry4.get() else None
            
        # Pasar los valores a la función v_valores
        vickers_valores(vickers_instance, force=self.force_value, result=self.result_value,
                        diameter1= self.diameter_value_1, diameter2= self.diameter_value_2)
            
        # Llamar a la función ensayo y obtener el resultado
        vickers_ensayo(vickers_instance)
        

        # Actualizar el widget result con el resultado de la función ensayo
        self.result1.configure(text=f"{vickers_instance.result} HV")
        self.result2.configure(text=f"{vickers_instance.diameter} mm")
        self.result4.configure(text=f"{vickers_instance.force} kp ")

    def calcular_ensayo_b(self):
            # Verificar si los CTkEntry están vacíos y asignar None si es el caso
            self.result_value = float(self.entry1.get().replace(",", ".")) if self.entry1.get() else None
            self.force_value = float(self.entry2.get().replace(",", ".")) if self.entry2.get() else None
            self.diameter_value = float(self.entry3.get().replace(",", ".")) if self.entry3.get() else None
            self.indentation_diameter_value = float(self.entry4.get().replace(",", ".")) if self.entry4.get() else None
            self.hardness_constant_value = float(self.entry5.get().replace(",", ".")) if self.entry5.get() else None


            # Pasar los valores a la función valores
            brinell_valores(brinell_instance, force=self.force_value, result=self.result_value,
                            diameter=self.diameter_value, indentation_diameter=self.indentation_diameter_value,
                            hardness_constant=self.hardness_constant_value)

            # Llamar a la función ensayo y obtener el resultado
            brinell_ensayo(brinell_instance)

            # Actualizar el widget result con el resultado de la función ensayo
            self.result1.configure(text=f"{brinell_instance.result} HB")
            self.result2.configure(text=f"{brinell_instance.diameter} mm")
            self.result3.configure(text=f"{brinell_instance.indentation_diameter} mm ")
            self.result4.configure(text=f"{brinell_instance.force} kp ")
            self.result5.configure(text='El ensayo es fiable' if brinell_instance.fiability else 'El ensayo no es fiable')
def cambiar_apariencia():
    global estado
    set_appearance_mode("light" if estado else "dark")
    estado = not estado

app = MainApp()
app.mostrar_principal()
app.mainloop()