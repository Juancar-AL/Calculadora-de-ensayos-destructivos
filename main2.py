from typing import Optional, Tuple, Union
from customtkinter import *
from tkinter import *
from calc.brinell import Brinell, brinell_valores, brinell_ensayo
from calc.vickers import Vickers, vickers_valores, vickers_ensayo
from calc.traction import Traction, trac_valores, trac_ensayo
from PIL import Image

image = CTkImage(light_image=Image.open("others/theme.png"))

tema_interfaz = False
ensayo_b = False
ensayo_v = False
ensayo_t = False

brinell_instance = Brinell()
vickers_instance = Vickers()
traction_instance = Traction()

class MainApp(CTk):
    def __init__(self) -> None:
        super().__init__()

        self.title("Calculadora de ensayos destructivos")
        self.geometry("700x300")
        #grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure((0,2), weight=2)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure((2,3), weight=3)
        self.iconbitmap("others/icon.ico")
        self.resizable(False, False)


        #Se establecen las características de los componentes de la pantalla principal en la que se puede seleccionar que a que ensayo se quiere acceder
        self.brinell_button = CTkButton(self, text = "Ensayo Brinell", command = self.mostrar_ensayo_b, corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color = "#88D4B2", width = 150)
        self.vickers_button = CTkButton(self, text = "Ensayo Vickers", command = self.mostrar_ensayo_v, corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color = "#88D4B2", width = 150)
        self.traction_button = CTkButton(self, text = "Ensayo de Tracción", command = self.mostrar_ensayo_t, corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color = "#88D4B2", width = 150,)
        self.name= CTkLabel(self, text = "Calculadora de ensayos destructivos", fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.author = CTkLabel(self, text = "Por Juan Carlos Alonso Luengo", fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.tema = CTkButton(self, image = image, text = "Apariencia",  command = cambiar_apariencia, fg_color = ("#353D3A", "#A4A7A6"), text_color = "#FFFFFF", hover_color = ("#5A6863", "#787878"), width = 150, corner_radius = 100)

        # WIDGETS DE LAS PANTALLAS DE LOS ENSAYOS

        #Etiquetas de texto que mostrarán los resultados de los ensayos
        self.result1 = CTkLabel(self, width = 150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result2 = CTkLabel(self, width = 150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result3 = CTkLabel(self, width = 150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result4 = CTkLabel(self, width = 150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100)
        self.result5 = CTkLabel(self, width = 150, fg_color = ("#D7D7D7", "#555555"), corner_radius = 100) 

        #Botones con diversas funciones. 1 - Calcula el ensayo 2- Cambia la apariencia 3 - Vuelve a la pantalla inicial
        self.button = CTkButton(self, text = "Calcular ensayo", corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color = "#88D4B2", width = 150)
        self.tema_e = CTkButton(self, image = image, text = "Tema", command = cambiar_apariencia ,corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color = "#88D4B2", width = 5)
        self.back = CTkButton(self, text = "Volver", command = self.mostrar_principal, corner_radius = 100, fg_color = ("#7CC0A2", "#45B584"), text_color = "#000000", hover_color = "#88D4B2", width = 5)
        
        #Campos en los que se pueden introducir los datos del problema
        self.entry1 = CTkEntry(self, corner_radius = 100, width = 150)
        self.entry2 = CTkEntry(self, corner_radius = 100, width = 150)
        self.entry3 = CTkEntry(self, corner_radius = 100, width = 150)
        self.entry4 = CTkEntry(self, corner_radius = 100, width = 150)
        self.entry5 = CTkEntry(self, corner_radius = 100, width = 150)
        self.entry6 = CTkEntry(self, corner_radius = 100, width = 150)
        self.entry7 = CTkEntry(self, corner_radius = 100, width = 150)
        
        #Etiquetas con texto que solamente muestran ese texto
        self.datos = CTkLabel(self, text = "Datos", width = 150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.res = CTkLabel(self, text = "Resultados", width = 150, fg_color = ("#7CC0A2", "#45B584"), corner_radius = 100)
        self.error = CTkLabel(self, text = "Has de rellenar al menos dos variables", text_color = ("#7CC0A2", "#45B584"))
    
        self.type = IntVar(value = 0)
        self.tension_checkbox = CTkRadioButton(self, text = "Tensión", command = self.color_change, variable = self.type, value = 1, fg_color = ("#7CC0A2", "#45B584"))
        self.force_checkbox = CTkRadioButton(self, text = "Force", command = self.color_change, variable = self.type, value = 2, fg_color = ("#7CC0A2", "#45B584"))
        self.elong_checkbox = CTkRadioButton(self, text = "Deformación", command = self.color_change, variable = self.type, value = 3, fg_color = ("#7CC0A2", "#45B584"))
        self.area_checkbox = CTkRadioButton(self, text = "Area", command = self.color_change, variable = self.type, value = 4, fg_color = ("#7CC0A2", "#45B584"))
        self.const_checkbox = CTkRadioButton(self, text = "Constante", command = self.color_change, variable = self.type, value = 5, fg_color = ("#7CC0A2", "#45B584"))
        
        self.proportional_zone = StringVar(value = "off")
        self.proportional_checkbox = CTkCheckBox(self, text = "Zona proporcional", command =  self.color_change, variable = self.proportional_zone, onvalue = "on", offvalue = "off" , fg_color = ("#7CC0A2", "#45B584"), hover_color = ("#7CC0A2", "#45B584"))    
    
    #Mediante el métido .grid muestra los elemetos de la pantalla principal, también se encarga de ocultar aquellos ensayos que puedan ensar abiertos
    def mostrar_principal(self):
        global ensayo_b, ensayo_v, ensayo_t
        if ensayo_b:
            self.ocultar_ensayo_b()
            ensayo_b = False
        elif ensayo_v:
            self.ocultar_ensayo_v()
            ensayo_v = False
        elif ensayo_t:
            self.ocultar_ensayo_t()
            ensayo_t = False
        self.brinell_button.grid(column = 0, row = 1, padx = 20, pady = 20, sticky = "ns")
        self.vickers_button.grid(column = 2, row = 1, padx = 20, pady = 20, sticky = "ns")
        self.traction_button.grid(column = 3, row = 1, padx = 20, pady = 20, sticky = "ns")
        self.name.grid(column = 0, row = 0, padx = 20, pady = 20, sticky = "nsew", columnspan = 4)
        self.author.grid(column = 0, row = 2, padx = 20, pady = 20, sticky = "nsew", columnspan = 3)
        self.tema.grid(row = 2, column = 3, pady=20, padx=20, sticky = "nsew")
    
    #Hace que no aparezcan en pantalla los elementos de la pantalla principal        
    def ocultar_principal(self):
        self.tema.grid_forget()
        self.brinell_button.grid_forget()
        self.vickers_button.grid_forget()
        self.traction_button.grid_forget()
        self.name.grid_forget()
        self.author.grid_forget()

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
        self.ocultar_principal()
        
        self.button.configure(command = self.calcular_ensayo_b)
        
        self.entry1.configure(placeholder_text = "Resultado ensayo")
        self.entry2.configure(placeholder_text = "Fuerza utilizada")
        self.entry3.configure(placeholder_text = "Diámetro identador")
        self.entry4.configure(placeholder_text = "Diámetro huella")
        self.entry5.configure(placeholder_text = "Constante ensayo")
        
        self.result1.configure(text = "Resultado ensayo")
        self.result2.configure(text = "Diametro indendador")
        self.result3.configure(text = "Diametro huella")
        self.result4.configure(text = "Fuerza utilizada")
        self.result5.configure(text = "Fiabilidad")
        
        self.entry1.grid(row = 2, column = 0, pady = 10, padx = 20)
        self.entry2.grid(row = 5, column = 0, pady = 10, padx = 20)
        self.entry3.grid(row = 3, column = 0, pady = 10, padx = 20)
        self.entry4.grid(row = 4, column = 0, pady = 10, padx = 20)
        self.entry5.grid(row = 6, column = 0, pady = 10, padx = 20)
        
        self.button.grid(row = 3, column = 2, pady = 10, padx = 20)
        self.datos.grid(row = 1, column = 0, pady = 10, padx = 20)
        self.res.grid(row = 1, column = 3, pady = 10, padx = 20)
        self.error.grid(row = 2, column = 2, pady = 10, padx = 20)
        
        self.result1.grid(row = 2, column = 3, pady = 10, padx = 20)
        self.result2.grid(row = 3, column = 3, pady = 10, padx = 20)
        self.result3.grid(row = 4, column = 3, pady = 10, padx = 20)
        self.result4.grid(row = 5, column = 3, pady = 10, padx = 20)
        self.result5.grid(row = 6, column = 3, pady = 10, padx = 20)
        
        self.tema_e.grid(row = 6, column = 2, pady = 10, padx = 20)
        self.back.grid(row = 5, column = 2, pady = 10, padx = 20)
            
    def mostrar_ensayo_v(self):
        global ensayo_v
        ensayo_v = True
        
        self.ocultar_principal()
        
        self.button.configure(command = self.calcular_ensayo_v)
        self.entry3.configure(placeholder_text = "Diámetro 1")
        self.entry4 .configure(placeholder_text = "Diámetro 2")
        self.entry1.configure(placeholder_text = "Resultado ensayo")
        self.entry2.configure(placeholder_text = "Fuerza utilizada")
        self.result1.configure(text = "Resultado ensayo")
        self.result2.configure(text = "Diametro")
        self.result4.configure(text = "Fuerza utilizada")
        self.error.grid(row = 2, column = 2, pady = 10, padx = 20)
        self.entry1.grid(row = 2, column = 0, pady = 10, padx = 20)
        self.entry2.grid(row = 5, column = 0, pady = 10, padx = 20)
        self.entry3.grid(row = 3, column = 0, pady = 10, padx = 20)
        self.entry4.grid(row = 4, column = 0, pady = 10, padx = 20)
        self.button.grid(row = 3, column = 2, pady = 10, padx = 20)
        self.datos.grid(row = 1, column = 0, pady = 10, padx = 20)
        self.res.grid(row = 1, column = 3, pady = 10, padx = 20)
        self.result1.grid(row = 2, column = 3, pady = 10, padx = 20)
        self.result2.grid(row = 3, column = 3, pady = 10, padx = 20)
        self.result4.grid(row = 4, column = 3, pady = 10, padx = 20)
        self.tema_e.grid(row = 5, column = 2, pady = 10, padx = 20)
        self.back.grid(row = 4, column = 2, pady = 10, padx = 20)

    
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

    def mostrar_ensayo_t(self):
        global ensayo_t
        ensayo_t = True
        self.ocultar_principal()
        self.button.configure(command = self.calcular_ensayo_t)
        self.tema_e.configure(width = 150)
        self.back.configure(width = 150)
        
        self.entry1.configure(placeholder_text = "Módulo de Young")
        self.entry2.configure(placeholder_text = "Fuerza utilizada")
        self.entry3.configure(placeholder_text = "Tensión generada")
        self.entry4.configure(placeholder_text = "Longitud inicial")
        self.entry5.configure(placeholder_text = "Longitud final")
        self.entry6.configure(placeholder_text = "Área")
        self.entry7.configure(placeholder_text = "Deformación unitaria")
        
        self.result1.configure(text = "Resultado")
        
        
        self.button.grid(row = 3, column = 4, pady = 10, padx = 20)
        self.tension_checkbox.grid(row = 2, column = 3, pady = 10, padx = 20)
        self.force_checkbox.grid(row = 3, column = 3, pady = 10, padx = 20)
        self.elong_checkbox.grid(row = 4, column = 3, pady = 10, padx = 20)
        self.area_checkbox.grid(row = 5, column = 3, pady = 10, padx = 20)  
        self.const_checkbox.grid(row = 6, column = 3, pady = 10, padx = 20)       
        
        self.proportional_checkbox.grid(row = 4, column = 1, pady = 10, padx = 20) 
        
        self.entry1.grid(row = 2, column = 0, pady = 10, padx = 20)
        self.entry2.grid(row = 3, column = 0, pady = 10, padx = 20)
        self.entry3.grid(row = 4, column = 0, pady = 10, padx = 20)
        self.entry4.grid(row = 5, column = 0, pady = 10, padx = 20)
        self.entry5.grid(row = 6, column = 0, pady = 10, padx = 20)
        self.entry6.grid(row = 2, column = 1, pady = 10, padx = 20)
        self.entry7.grid(row = 3, column = 1, pady = 10, padx = 20)
        
        self.result1.grid(row = 2, column = 4, pady = 10, padx = 20)
        
        self.back.grid(row = 5, column = 4, pady = 10, padx = 20)
        self.tema_e.grid(row = 4, column = 4, pady = 10, padx = 20)
        
    def ocultar_ensayo_t(self):
        self.button.grid_forget()
        self.tension_checkbox.grid_forget()
        self.force_checkbox.grid_forget()
        self.elong_checkbox.grid_forget()
        self.area_checkbox.grid_forget()
        self.const_checkbox.grid_forget()
        self.proportional_checkbox.grid_forget()
        self.entry1.grid_forget()
        self.entry2.grid_forget()
        self.entry3.grid_forget()
        self.entry4.grid_forget()
        self.entry5.grid_forget()
        self.entry6.grid_forget()
        self.entry7.grid_forget()
        self.result1.grid_forget()
        self.back.grid_forget()
        self.tema_e.grid_forget()

    def calcular_ensayo_v(self):
        
        self.result_value = float((self.entry1.get()).replace(",", ".")) if self.entry1.get() else None
        self.force_value = float(self.entry2.get().replace(",", ".")) if self.entry2.get() else None
        self.diameter_value_1 = float(self.entry3.get().replace(",", ".")) if self.entry3.get() else None
        self.diameter_value_2 = float(self.entry4.get().replace(",", ".")) if self.entry4.get() else None
            
        # Pasar los valores a la función v_valores
        vickers_valores(vickers_instance, force = self.force_value, result = self.result_value,
                        diameter1= self.diameter_value_1, diameter2= self.diameter_value_2)
        
        print(vickers_instance)
        # Llamar a la función ensayo y obtener el resultado
        #vickers_ensayo(vickers_instance)
		
        print(vickers_instance)
		
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
        brinell_valores(brinell_instance, force = self.force_value, result = self.result_value,
                        diameter = self.diameter_value, indentation_diameter = self.indentation_diameter_value,
                        hardness_constant = self.hardness_constant_value)

        # Llamar a la función ensayo y obtener el resultado
        brinell_ensayo(brinell_instance)

        # Actualizar el widget result con el resultado de la función ensayo
        self.result1.configure(text=f"{brinell_instance.result} HB")
        self.result2.configure(text=f"{brinell_instance.diameter} mm")
        self.result3.configure(text=f"{brinell_instance.indentation_diameter} mm ")
        self.result4.configure(text=f"{brinell_instance.force} kp ")
        self.result5.configure(text='El ensayo es fiable' if brinell_instance.fiability else 'El ensayo no es fiable')
        
    def calcular_ensayo_t(self):
            
        const_value = float(self.entry1.get().replace(",", ".")) if self.entry1.get() else None
        force_value = float(self.entry2.get().replace(",", ".")) if self.entry2.get() else None
        long1_value = float(self.entry4.get().replace(",", ".")) if self.entry4.get() else None
        tension_value = float(self.entry3.get().replace(",", ".")) if self.entry3.get() else None
        long2_value = float(self.entry5.get().replace(",", ".")) if self.entry5.get() else None
        area_value = float(self.entry6.get().replace(",", ".")) if self.entry6.get() else None
        elong_value = float(self.entry7.get().replace(",", ".")) if self.entry7.get() else None
        
        trac_valores(traction_instance, const = const_value, force = force_value, tension = tension_value, long1 = long1_value, long2 = long2_value, area = area_value, elong = elong_value)
        
        self.result1.configure(text=f"{trac_ensayo(traction_instance, proportional = True if self.proportional_zone.get() == 'on' else False, tens = True if self.type.get() == 1 else False, const = True if self.type.get() == 5 else False, force = True if self.type.get() == 2 else False, elong = True if self.type.get() == 3 else False, area = True if self.type.get() == 4 else False)} ")
        
    def color_change(self):
        self.entry1.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Módulo de Young")
        self.entry2.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Fuerza utilizada")
        self.entry3.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Tensión generada")
        self.entry4.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Longitud inicial")
        self.entry5.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Longitud final")
        self.entry6.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Área")
        self.entry7.configure(fg_color = "#f0f0f0", state = "disabled", placeholder_text = "Deformación unitaria")
        if self.type.get() == 1 and self.proportional_zone.get() == "on":
            self.entry1.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Módulo de Young")
            self.entry7.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Deformación unitaria")
        elif self.type.get() == 1 and self.proportional_zone.get() == "off":
            self.entry2.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Fuerza utilizada")
            self.entry6.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Área")
        elif self.type.get() == 2 and self.proportional_zone.get() == "off":
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
            self.entry6.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Área")
        elif self.type.get() == 2 and self.proportional_zone.get() == "on":
            self.proportional_checkbox.toggle()
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
            self.entry6.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Área")
        elif self.type.get() == 3 and self.proportional_zone.get() == "on":
            self.entry1.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Módulo de Young")  
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
        elif self.type.get() == 3 and self.proportional_zone.get() == "off":
            self.entry4.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Longitud inicial")
            self.entry5.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Deformación unitaria")
        elif self.type.get() == 4 and self.proportional_zone.get() == "off":
            self.entry2.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Fuerza utilizada")
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
        elif self.type.get() == 4 and self.proportional_zone.get() == "on":
            self.proportional_checkbox.toggle()
            self.entry2.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Fuerza utilizada")
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
        elif self.type.get() == 5 and self.proportional_zone.get() == "on":
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
            self.entry7.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Deformación unitaria")
        elif self.type.get() == 5 and self.proportional_zone.get() == "off":
            self.proportional_checkbox.toggle()
            self.entry3.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Tensión generada")
            self.entry7.configure(fg_color = ("#A1E2C6", "#A1E2C6"), state = "normal", placeholder_text = "Deformación unitaria")
        

            

def cambiar_apariencia():
    global tema_interfaz
    set_appearance_mode("light" if tema_interfaz else "dark")
    tema_interfaz = not tema_interfaz

app = MainApp()
app.mostrar_principal()
app.mainloop()

#Por Juan Carlos Alonso Luengo