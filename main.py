from typing import Optional, Tuple, Union
import customtkinter
import calc.brinell as brinell, calc.vickers as vickers
from PIL import Image


brinell_instance = brinell.Brinell()
vickers_instance = vickers.Vickers()

image = customtkinter.CTkImage(light_image=Image.open("others/theme.png"))

class BrinellApp(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__()

        self.title("Calculadora de ensayos destructivos - Brinell")
        self.geometry("700x300")
        self.grid_columnconfigure((0, 3), weight=1)
        self.iconbitmap("others/icon.ico")

        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Resultado ensayo",corner_radius = 100, width=150)
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Fuerza",corner_radius = 100, width=150)
        self.entry3 = customtkinter.CTkEntry(self, placeholder_text="Diámetro identador",corner_radius = 100, width=150)
        self.entry4 = customtkinter.CTkEntry(self, placeholder_text="Diámetro huella",corner_radius = 100, width=150)
        self.entry5 = customtkinter.CTkEntry(self, placeholder_text="Constante ensayo",corner_radius = 100, width=150)
        self.entry1.grid(row=2, column=0, pady=10, padx=20)
        self.entry2.grid(row=5, column=0, pady=10, padx=20)
        self.entry3.grid(row=3, column=0, pady=10, padx=20)
        self.entry4.grid(row=4, column=0, pady=10, padx=20)
        self.entry5.grid(row=6, column=0, pady=10, padx=20)
        self.datos = customtkinter.CTkLabel(self, text="Datos", width=150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.res = customtkinter.CTkLabel(self, text="Resultados", width=150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.button = customtkinter.CTkButton(self, text="Calcular ensayo", command=self.calcular_ensayo,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=150)
        self.result1 = customtkinter.CTkLabel(self, text="Resultado ensayo", width=150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result2 = customtkinter.CTkLabel(self, text = "Diametro identador", width=150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result3 = customtkinter.CTkLabel(self, text = "Diametro huella", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.result4 = customtkinter.CTkLabel(self, text="Fuerza utilizada", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.result5 = customtkinter.CTkLabel(self, text="Fiabilidad", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.tema = customtkinter.CTkButton(self, image=image, text="Tema",   command=cambiar_apariencia ,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=5)
        self.button.grid(row=3, column=2, pady=10, padx=20)
        self.datos.grid(row=1, column=0, pady=10, padx=20)
        self.res.grid(row=1, column=3, pady=10, padx=20)
        self.result1.grid(row=2, column=3, pady=10, padx=20)
        self.result2.grid(row=3, column=3, pady=10, padx=20)
        self.result3.grid(row=4, column=3, pady=10, padx=20)
        self.result4.grid(row=5, column=3, pady=10, padx=20)
        self.result5.grid(row=6, column=3, pady=10, padx=20)
        self.tema.grid(row=6, column=2, pady=10, padx=20)
                        

    def calcular_ensayo(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso
        self.result_value = float(self.entry1.get().replace(",", ".")) if self.entry1.get() else None
        self.force_value = float(self.entry2.get().replace(",", ".")) if self.entry2.get() else None
        self.diameter_value = float(self.entry3.get().replace(",", ".")) if self.entry3.get() else None
        self.indentation_diameter_value = float(self.entry4.get().replace(",", ".")) if self.entry4.get() else None
        self.hardness_constant_value = float(self.entry5.get().replace(",", ".")) if self.entry5.get() else None

        # Pasar los valores a la función brinell.valores
        brinell.valores(brinell_instance, force=self.force_value, result=self.result_value,
                        diameter=self.diameter_value, indentation_diameter=self.indentation_diameter_value,
                        hardness_constant=self.hardness_constant_value)

        # Llamar a la función ensayo y obtener el resultado
        brinell.ensayo(brinell_instance)

        # Actualizar el widget result con el resultado de la función ensayo
        self.result1.configure(text=f"{brinell_instance.result} HB")
        self.result2.configure(text=f"{brinell_instance.diameter} mm")
        self.result3.configure(text=f"{brinell_instance.indentation_diameter} mm ")
        self.result4.configure(text=f"{brinell_instance.force} kp ")
        self.result5.configure(text='El ensayo es fiable' if brinell_instance.fiability else 'El ensayo no es fiable')

def cambiar_apariencia():
    global estado
    estado = not estado
    customtkinter.set_appearance_mode("light" if estado else "dark")

estado = False
# Crea la instancia de la aplicación Brinell después de haber definido la clase


class VickersApp(customtkinter.CTkToplevel):
    def __init__(self, *args, **kwargs):
        super().__init__()
        self.title("Calculadora de ensayos destructivos - Vickers")
        self.geometry("700x300")
        self.grid_columnconfigure((0, 3), weight=1)
        self.iconbitmap("others/icon.ico")

        self.entry1 = customtkinter.CTkEntry(self, placeholder_text="Resultado ensayo",corner_radius = 100, width=150)
        self.entry2 = customtkinter.CTkEntry(self, placeholder_text="Fuerza",corner_radius = 100, width=150)
        self.entry3 = customtkinter.CTkEntry(self, placeholder_text="Diámetro 1",corner_radius = 100, width=150)
        self.entry4 = customtkinter.CTkEntry(self, placeholder_text="Diámetro 2",corner_radius = 100, width=150)
        self.entry1.grid(row=2, column=0, pady=10, padx=20)
        self.entry2.grid(row=5, column=0, pady=10, padx=20)
        self.entry3.grid(row=3, column=0, pady=10, padx=20)
        self.entry4.grid(row=4, column=0, pady=10, padx=20)
        self.datos = customtkinter.CTkLabel(self, text="Datos", width=150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.res = customtkinter.CTkLabel(self, text="Resultados", width=150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.button = customtkinter.CTkButton(self, text="Calcular ensayo", command=self.calcular_ensayo,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=150)
        self.result1 = customtkinter.CTkLabel(self, text="Resultado ensayo", width=150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result2 = customtkinter.CTkLabel(self, text = "Diametro", width=150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result4 = customtkinter.CTkLabel(self, text="Fuerza utilizada", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.button.grid(row=3, column=2, pady=10, padx=20)
        self.datos.grid(row=1, column=0, pady=10, padx=20)
        self.res.grid(row=1, column=3, pady=10, padx=20)
        self.result1.grid(row=2, column=3, pady=10, padx=20)
        self.result2.grid(row=3, column=3, pady=10, padx=20)
        self.result4.grid(row=4, column=3, pady=10, padx=20)
        self.tema = customtkinter.CTkButton(self, image=image, text="Tema",    command=cambiar_apariencia ,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=5)
        self.tema.grid(row=5, column=3, pady=10, padx=20)
    def calcular_ensayo(self):
        result_value = float((self.entry1.get()).replace(",", ".")) if self.entry1.get() else None
        force_value = float(self.entry2.get().replace(",", ".")) if self.entry2.get() else None
        diameter_value_1 = float(self.entry3.get().replace(",", ".")) if self.entry3.get() else None
        diameter_value_2 = float(self.entry4.get().replace(",", ".")) if self.entry4.get() else None
            
        # Pasar los valores a la función Vickers.valores
        vickers.valores(vickers.vickers_instance, force=force_value, result=result_value,
                        diameter1= diameter_value_1, diameter2= diameter_value_2)
            
        # Llamar a la función ensayo y obtener el resultado
        vickers.ensayo(vickers.vickers_instance)
            
        # Actualizar el widget result con el resultado de la función ensayo
        self.result1.configure(text=f"{vickers.vickers_instance.result} HV")
        self.result2.configure(text=f"{vickers.vickers_instance.diameter} mm")
        self.result4.configure(text=f"{vickers.vickers_instance.force} kp ")

class MainApp(customtkinter.CTk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Calculadora de ensayos destructivos")
        self.geometry("700x275")
        self.grid_columnconfigure((0, 2), weight=1)
        self.iconbitmap("others/icon.ico")

        self.button1 = customtkinter.CTkButton(self, text="Ensayo Brinell", command=self.c_brinell,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=350)
        self.button2 = customtkinter.CTkButton(self, text="Ensayo Vickers", command=self.c_vickers,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=350)
        self.label = customtkinter.CTkLabel(self, text = "Calculadora de ensayos destructivos", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100)
        self.label2 = customtkinter.CTkLabel(self, text = "Por Juan Carlos Alonso Luengo", width=150, fg_color = ("#D7D7D7", "#555555"),corner_radius = 100, font=("", 10))
        self.button1.grid(column=0, row = 3, padx = 20, pady = 40, sticky = "nsew")
        self.button2.grid(column=2, row = 3, padx = 20, pady = 40)
        self.label.grid(column = 1, row = 0, padx = 20, pady = 20)
        self.label2.grid(column = 1, row = 5, padx = 20, pady = 60)
        self.tema = customtkinter.CTkButton(self, image=image, text="Tema",  command=cambiar_apariencia ,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color="#88D4B2", width=5)
        self.tema.grid(row=5, column=2, pady=10, padx=20)
        self.toplevel_window = None

    def c_brinell(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = BrinellApp(self)
        else:
            self.toplevel_window.focus()
    def c_vickers(self):
        if self.toplevel_window is None or not self.toplevel_window.winfo_exists():
            self.toplevel_window = VickersApp(self)
        else:
            self.toplevel_window.focus()


app = MainApp()
app.mainloop()
