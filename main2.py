from customtkinter import CTkEntry, CTkImage, CTk, CTkButton, CTkRadioButton, CTkCheckBox, CTkLabel, CTk, StringVar, IntVar, set_appearance_mode
from tkinter import END
from calc.brinell import Brinell, brinell_ensayo
from calc.vickers import Vickers, vickers_ensayo
from calc.traction import Traction, trac_ensayo
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
        self.geometry("800x300")
        self.grid_columnconfigure((0, 2), weight=2)
        self.grid_rowconfigure(1, weight=2)
        self.grid_rowconfigure((2, 3), weight=3)
        self.iconbitmap("others/icono.ico")
        self.resizable(False, False)

        # Se establecen las características de los componentes de la pantalla principal en la que se puede seleccionar que a que ensayo se quiere acceder
        self.brinell_button = CTkButton(self, text="Ensayo Brinell", command=self.mostrar_ensayo_b, corner_radius=100, fg_color=(
            "#7CC0A2", "#45B584"), text_color="#000000", hover_color="#88D4B2", width=200)
        self.vickers_button = CTkButton(self, text="Ensayo Vickers", command=self.mostrar_ensayo_v, corner_radius=100, fg_color=(
            "#7CC0A2", "#45B584"), text_color="#000000", hover_color="#88D4B2", width=200)
        self.traction_button = CTkButton(self, text="Ensayo de Tracción", command=self.mostrar_ensayo_t, corner_radius=100, fg_color=(
            "#7CC0A2", "#45B584"), text_color="#000000", hover_color="#88D4B2", width=200,)
        self.name = CTkLabel(self, text="Calculadora de ensayos destructivos", fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.autor = CTkLabel(self, text="Por Juan Carlos Alonso Luengo", fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100, width=600)
        self.tema = CTkButton(self, image=image, text="Tema",  command=cambiar_apariencia, fg_color=(
            "#353D3A", "#A4A7A6"), text_color="#FFFFFF", hover_color=("#5A6863", "#787878"), width=140, corner_radius=100)

        # WIDGETS DE LAS PANTALLAS DE LOS ENSAYOS

        # Etiquetas de texto que mostrarán los resultados de los ensayos
        self.resultado1 = CTkLabel(self, width=140, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado2 = CTkLabel(self, width=140, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado3 = CTkLabel(self, width=140, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado4 = CTkLabel(self, width=140, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado5 = CTkLabel(self, width=140, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)

        # Botones con diversas funciones. 1 - Calcula el ensayo 2- Cambia la apariencia 3 - Vuelve a la pantalla inicial
        self.boton = CTkButton(self, text="Calcular ensayo", corner_radius=100, fg_color=("#7CC0A2", "#45B584"), text_color="#000000",
                               hover_color="#88D4B2", width=160)
        self.tema_e = CTkButton(self, image=image, text="Tema", command=cambiar_apariencia, corner_radius=100, fg_color=("#7CC0A2", "#45B584"),
                                text_color="#000000", hover_color="#88D4B2", width=160)
        self.volver = CTkButton(self, text="Volver", command=self.mostrar_principal, corner_radius=100, fg_color=("#7CC0A2", "#45B584"),
                                text_color="#000000", hover_color="#88D4B2", width=160)

        # Campos en los que se pueden introducir los datos del problema
        self.entrada_datos_1 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_2 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_3 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_4 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_5 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_6 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_7 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_8 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_9 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_10 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_11 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_12 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_13 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))
        self.entrada_datos_14 = CTkEntry(self, corner_radius=100, width=160, fg_color=(
            "#D7D7D7", "#555555"))

        # Etiquetas con texto que solamente muestran ese texto
        self.datos = CTkLabel(self, text="Datos", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.resultados = CTkLabel(self, text="Resultados", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.error = CTkLabel(
            self, text="Has de rellenar al menos dos variables", text_color=("#45B584", "#45B584"))

        self.type = IntVar(value=0)
        self.casilla_tension = CTkRadioButton(
            self, text="Tension", command=self.color_change, variable=self.type, value=1, fg_color=("#7CC0A2", "#45B584"), width=140)
        self.casilla_fuerza = CTkRadioButton(
            self, text="Fuerza", command=self.color_change, variable=self.type, value=2, fg_color=("#7CC0A2", "#45B584"), width=140)
        self.casilla_deformacion_unitaria = CTkRadioButton(
            self, text="Deformación", command=self.color_change, variable=self.type, value=3, fg_color=("#7CC0A2", "#45B584"), width=140)
        self.casilla_area = CTkRadioButton(
            self, text="Area", command=self.color_change, variable=self.type, value=4, fg_color=("#7CC0A2", "#45B584"), width=140)
        self.casilla_modulo_young = CTkRadioButton(
            self, text="Modulo de Young", command=self.color_change, variable=self.type, value=5, fg_color=("#7CC0A2", "#45B584"), width=140)

        self.zona_proporcional = StringVar(value="off")
        self.casilla_proporcional = CTkCheckBox(self, text="Zona proporcional", command=self.color_change, variable=self.zona_proporcional,
                                                onvalue="on", offvalue="off", fg_color=("#7CC0A2", "#45B584"), hover_color=("#7CC0A2", "#45B584"))

    # Mediante el métido .grid muestra los elemetos de la pantalla principal, también se encarga de ocultar aquellos ensayos que puedan ensar abiertos
    def mostrar_principal(self):
        global ensayo_b, ensayo_v, ensayo_t
        if ensayo_b or ensayo_v or ensayo_t:
            self.ocultar_ensayo()
        self.brinell_button.grid(
            column=0, row=1, padx=20, pady=20, sticky="ns")
        self.vickers_button.grid(
            column=2, row=1, padx=20, pady=20, sticky="ns")
        self.traction_button.grid(
            column=3, row=1, padx=20, pady=20, sticky="ns")
        self.name.grid(column=0, row=0, padx=20, pady=20,
                       sticky="nsew", columnspan=4)
        self.autor.grid(column=0, row=2, padx=20, pady=20,
                        sticky="nsew", columnspan=3)
        self.tema.grid(row=2, column=3, pady=20, padx=20, sticky="nsew")

    # Hace que no aparezcan en pantalla los elementos de la pantalla principal
    def ocultar_principal(self):
        principal_list = [self.tema, self.brinell_button,
                          self.vickers_button, self.traction_button, self.name, self.autor]

        for i in principal_list:
            i.grid_forget()

    def mostrar_ensayo_b(self):
        global ensayo_b
        ensayo_b = True
        self.ocultar_principal()

        self.boton.configure(command=self.calcular_ensayo_b)

        self.entrada_datos_1.configure(placeholder_text="Resultado ensayo")
        self.entrada_datos_2.configure(placeholder_text="Diámetro indentador")
        self.entrada_datos_3.configure(placeholder_text="Diámetro huella")
        self.entrada_datos_4.configure(placeholder_text="Fuerza utilizada")
        self.entrada_datos_5.configure(
            placeholder_text="Constante ensayo")

        self.resultado1.configure(text="Resultado ensayo")
        self.resultado2.configure(text="Diametro indendador")
        self.resultado3.configure(text="Diametro huella")
        self.resultado4.configure(text="Fuerza utilizada")
        self.resultado5.configure(text="Fiabilidad")

        self.entrada_datos_1.grid(row=2, column=0, pady=10, padx=20)
        self.entrada_datos_2.grid(row=3, column=0, pady=10, padx=20)
        self.entrada_datos_3.grid(row=4, column=0, pady=10, padx=20)
        self.entrada_datos_4.grid(row=5, column=0, pady=10, padx=20)
        self.entrada_datos_5.grid(row=6, column=0, pady=10, padx=20)

        self.boton.grid(row=3, column=2, pady=10, padx=20)
        self.datos.grid(row=1, column=0, pady=10, padx=20)
        self.resultados.grid(row=1, column=3, pady=10, padx=20)
        self.error.grid(row=2, column=2, pady=10, padx=20)

        self.resultado1.grid(row=2, column=3, pady=10, padx=20)
        self.resultado2.grid(row=3, column=3, pady=10, padx=20)
        self.resultado3.grid(row=4, column=3, pady=10, padx=20)
        self.resultado4.grid(row=5, column=3, pady=10, padx=20)
        self.resultado5.grid(row=6, column=3, pady=10, padx=20)

        self.tema_e.grid(row=6, column=2, pady=10, padx=20)
        self.volver.grid(row=5, column=2, pady=10, padx=20)

    def mostrar_ensayo_v(self):
        global ensayo_v
        ensayo_v = True

        self.ocultar_principal()

        self.boton.configure(command=self.calcular_ensayo_v)

        self.entrada_datos_2.configure(placeholder_text="Diámetro 1")
        self.entrada_datos_3 .configure(placeholder_text="Diámetro 2")
        self.entrada_datos_1.configure(placeholder_text="Resultado ensayo")
        self.entrada_datos_4.configure(placeholder_text="Fuerza utilizada")

        self.resultado1.configure(text="Resultado ensayo")
        self.resultado2.configure(text="Diametro")
        self.resultado4.configure(text="Fuerza utilizada")
        self.error.grid(row=2, column=2, pady=10, padx=20)
        self.entrada_datos_1.grid(row=2, column=0, pady=10, padx=20)
        self.entrada_datos_2.grid(row=3, column=0, pady=10, padx=20)
        self.entrada_datos_3.grid(row=4, column=0, pady=10, padx=20)
        self.entrada_datos_4.grid(row=5, column=0, pady=10, padx=20)
        self.boton.grid(row=3, column=2, pady=10, padx=20)
        self.datos.grid(row=1, column=0, pady=10, padx=20)
        self.resultados.grid(row=1, column=3, pady=10, padx=20)
        self.resultado1.grid(row=2, column=3, pady=10, padx=20)
        self.resultado2.grid(row=3, column=3, pady=10, padx=20)
        self.resultado4.grid(row=4, column=3, pady=10, padx=20)
        self.tema_e.grid(row=5, column=2, pady=10, padx=20)
        self.volver.grid(row=4, column=2, pady=10, padx=20)

    def mostrar_ensayo_t(self):
        global ensayo_t
        ensayo_t = True
        self.ocultar_principal()
        self.boton.configure(command=self.calcular_ensayo_t)
        self.tema_e.configure(width=140)
        self.volver.configure(width=140)

        self.entrada_datos_1.configure(
            placeholder_text="Módulo de Young", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))
        self.entrada_datos_2.configure(
            placeholder_text="Fuerza utilizada", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))
        self.entrada_datos_3.configure(
            placeholder_text="Tension generada", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))
        self.entrada_datos_4.configure(
            placeholder_text="Longitud inicial", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))
        self.entrada_datos_5.configure(placeholder_text="Longitud final",
                                       text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))
        self.entrada_datos_6.configure(placeholder_text="Área",
                                       text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))
        self.entrada_datos_7.configure(
            placeholder_text="Deformación", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"))

        self.resultado1.configure(text="Resultado")

        self.boton.grid(row=3, column=4, pady=10, padx=20)

        self.casilla_tension.grid(row=2, column=1, pady=10, padx=20)
        self.casilla_fuerza.grid(row=3, column=1, pady=10, padx=20)
        self.casilla_deformacion_unitaria.grid(
            row=4, column=1, pady=10, padx=20)
        self.casilla_area.grid(row=5, column=1, pady=10, padx=20)
        self.casilla_modulo_young.grid(row=6, column=1, pady=10, padx=20)

        self.casilla_proporcional.grid(row=4, column=3, pady=10, padx=20)

        self.entrada_datos_1.grid(row=2, column=2, pady=10, padx=20)
        self.entrada_datos_2.grid(row=3, column=2, pady=10, padx=20)
        self.entrada_datos_3.grid(row=4, column=2, pady=10, padx=20)
        self.entrada_datos_4.grid(row=5, column=2, pady=10, padx=20)
        self.entrada_datos_5.grid(row=6, column=2, pady=10, padx=20)
        self.entrada_datos_6.grid(row=2, column=3, pady=10, padx=20)
        self.entrada_datos_7.grid(row=3, column=3, pady=10, padx=20)

        self.resultado1.grid(row=2, column=4, pady=10, padx=20)

        self.volver.grid(row=6, column=4, pady=10, padx=20)
        self.tema_e.grid(row=5, column=4, pady=10, padx=20)

    def ocultar_ensayo(self):
        global ensayo_b, ensayo_v, ensayo_t
        if ensayo_b:
            ensayo_b_list = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3, self.entrada_datos_4, self.entrada_datos_5, self.datos, self.resultados, self.error, self.boton,
                             self.resultado1, self.resultado2, self.resultado3, self.resultado4, self.resultado5, self.volver, self.tema_e]
            for i in ensayo_b_list:
                i.grid_forget()
            ensayo_b_list_delete = [self.entrada_datos_1, self.entrada_datos_2,
                                    self.entrada_datos_3, self.entrada_datos_4, self.entrada_datos_5]
            for i in ensayo_b_list_delete:
                i.delete(0, END)
            ensayo_b = False
        elif ensayo_v:
            ensayo_v_list = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3, self.entrada_datos_4, self.boton, self.datos, self.resultados, self.error,
                             self.resultado1, self.resultado2, self.resultado4, self.tema_e, self.volver]
            for i in ensayo_v_list:
                i.grid_forget()

            ensayo_v_list_delete = [self.entrada_datos_1,
                                    self.entrada_datos_2, self.entrada_datos_4]
            for i in ensayo_v_list_delete:
                i.delete(0, END)
            ensayo_v = False
        elif ensayo_t:
            ensayo_t_list = [self.boton, self.casilla_tension, self.casilla_fuerza, self.casilla_deformacion_unitaria, self.casilla_area, self.casilla_modulo_young, self.casilla_proporcional,
                             self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3, self.entrada_datos_4, self.entrada_datos_5, self.entrada_datos_6, self.entrada_datos_7, self.resultado1, self.volver, self.tema_e]
            for i in ensayo_t_list:
                i.grid_forget()
            ensayo_t_list_delete = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3,
                                    self.entrada_datos_4, self.entrada_datos_5, self.entrada_datos_6, self.entrada_datos_7]
            for i in ensayo_t_list_delete:
                i.delete(0, END)
            ensayo_t = False
        self.mostrar_principal()

    def calcular_ensayo_v(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso
        self.resultado = float((self.entrada_datos_1.get()).replace(
            ",", ".")) if self.entrada_datos_1.get() else "Error"
        self.fuerza = float(self.entrada_datos_4.get().replace(
            ",", ".")) if self.entrada_datos_4.get() else "Error"
        self.diameter_1 = float(self.entrada_datos_2.get().replace(
            ",", ".")) if self.entrada_datos_2.get() else "Error"
        self.diameter_2 = float(self.entrada_datos_3.get().replace(
            ",", ".")) if self.entrada_datos_3.get() else "Error"

        # Pasar los valores a la función v_valores
        valores(vickers_instance, fuerza=self.fuerza, result=self.resultado,
                diameter1=self.diameter_1, diameter2=self.diameter_2)

        # Llamar a la función ensayo y obtener el resultado
        vickers_ensayo(vickers_instance)

        # Actualizar el widget resultadocon el resultado de la función ensayo
        self.resultado1.configure(text=f"{vickers_instance.result} HV")
        self.resultado2.configure(text=f"{vickers_instance.diameter} mm")
        self.resultado4.configure(text=f"{vickers_instance.fuerza} kp ")

    def calcular_ensayo_b(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso
        self.resultado = float(self.entrada_datos_1.get().replace(
            ",", ".")) if self.entrada_datos_1.get() else "Error"
        self.diameter = float(self.entrada_datos_2.get().replace(
            ",", ".")) if self.entrada_datos_2.get() else "Error"
        self.indentation_diameter = float(
            self.entrada_datos_3.get().replace(",", ".")) if self.entrada_datos_3.get() else "Error"
        self.hardness_modulo_youngant = float(
            self.entrada_datos_5.get().replace(",", ".")) if self.entrada_datos_5.get() else "Error"
        self.fuerza = float(self.entrada_datos_4.get().replace(
            ",", ".")) if self.entrada_datos_4.get() else "Error"

        # Pasar los valores a la función valores
        valores(brinell_instance, fuerza=self.fuerza, result=self.resultado,
                diameter=self.diameter, indentation_diameter=self.indentation_diameter,
                hardness_modulo_youngant=self.hardness_modulo_youngant)

        # Llamar a la función ensayo y obtener el resultado
        brinell_ensayo(brinell_instance)

        # Actualizar el widget resultadocon el resultado de la función ensayo
        self.resultado1.configure(text=f"{brinell_instance.result} HB")
        self.resultado2.configure(text=f"{brinell_instance.diameter} mm")
        self.resultado3.configure(
            text=f"{brinell_instance.indentation_diameter} mm ")
        self.resultado4.configure(text=f"{brinell_instance.fuerza} kp ")
        self.resultado5.configure(
            text='El ensayo es fiable' if brinell_instance.fiabilidad else 'El ensayo no es fiable')

    def calcular_ensayo_t(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso
        modulo_young = float(self.entrada_datos_1.get().replace(
            ",", ".")) if self.entrada_datos_1.get() else "Error"
        fuerza = float(self.entrada_datos_2.get().replace(
            ",", ".")) if self.entrada_datos_2.get() else "Error"
        longitud_inicial = float(self.entrada_datos_4.get().replace(
            ",", ".")) if self.entrada_datos_4.get() else "Error"
        tension = float(self.entrada_datos_3.get().replace(
            ",", ".")) if self.entrada_datos_3.get() else "Error"
        longitud_final = float(self.entrada_datos_5.get().replace(
            ",", ".")) if self.entrada_datos_5.get() else "Error"
        area = float(self.entrada_datos_6.get().replace(
            ",", ".")) if self.entrada_datos_6.get() else "Error"
        deformacion_unitaria = float(self.entrada_datos_7.get().replace(
            ",", ".")) if self.entrada_datos_7.get() else "Error"

        # Pasar los valores a la función valores
        valores(traction_instance, modulo_young=modulo_young, fuerza=fuerza, tension=tension,
                longitud_inicial=longitud_inicial, longitud_final=longitud_final, area=area, deformacion_unitaria=deformacion_unitaria)

        # Llamar a la función ensayo, obtener el resultado y dejarlo en una variable
        result_trac = trac_ensayo(traction_instance, proportional=True if self.zona_proporcional.get() == 'on' else False,
                                  tension=True if self.type.get() == 1 else False, modulo_young=True if self.type.get() == 5 else False,
                                  fuerza=True if self.type.get() == 2 else False, deformacion_unitaria=True if self.type.get() == 3 else False,
                                  area=True if self.type.get() == 4 else False)
        # Actualizar el widget resultadocon el resultado de la función ensayo
        self.resultado1.configure(
            text=f"{result_trac if result_trac != None else 'Error'} ")

    def color_change(self):
        entry_list = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3,
                      self.entrada_datos_4, self.entrada_datos_5, self.entrada_datos_6, self.entrada_datos_7]
        for i in entry_list:
            i.configure(fg_color=(
                "#D7D7D7", "#555555"))
        if self.type.get() == 1 and self.zona_proporcional.get() == "on":
            for i in [self.entrada_datos_1, self.entrada_datos_7]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 1 and self.zona_proporcional.get() == "off":
            for i in [self.entrada_datos_2, self.entrada_datos_6]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 2 and self.zona_proporcional.get() == "off":
            for i in [self.entrada_datos_6, self.entrada_datos_3]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 2 and self.zona_proporcional.get() == "on":
            self.casilla_proporcional.toggle()
            for i in [self.entrada_datos_3, self.entrada_datos_6]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 3 and self.zona_proporcional.get() == "on":
            for i in [self.entrada_datos_1, self.entrada_datos_3]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 3 and self.zona_proporcional.get() == "off":
            for i in [self.entrada_datos_4, self.entrada_datos_5]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 4 and self.zona_proporcional.get() == "off":
            for i in [self.entrada_datos_2, self.entrada_datos_3]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 4 and self.zona_proporcional.get() == "on":
            self.casilla_proporcional.toggle()
            for i in [self.entrada_datos_2, self.entrada_datos_3]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 5 and self.zona_proporcional.get() == "on":
            for i in [self.entrada_datos_3, self.entrada_datos_7]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))
        elif self.type.get() == 5 and self.zona_proporcional.get() == "off":
            self.casilla_proporcional.toggle()
            for i in [self.entrada_datos_3, self.entrada_datos_7]:
                i.configure(fg_color=(
                    "#A1E2C6", "#A1E2C6"))


def cambiar_apariencia():
    global tema_interfaz
    set_appearance_mode("light" if tema_interfaz else "dark")
    tema_interfaz = not tema_interfaz


def valores(self, **kwargs):
    if ensayo_b or ensayo_t:
        for key, value in kwargs.items():
            if value is not None:
                setattr(self, key, value)
    else:  # Este método es especial para
        for key, value in kwargs.items():
            if value is not None:
                if key == 'diameter2' and kwargs.get('diameter2') is not None:
                    # Si se dan dos valores para el diámetro, se calcula la media
                    self.diameter = (
                        kwargs['diameter1'] + kwargs['diameter2']) / 2
                elif key == 'diameter1':
                    # Si solo se da un valor para el diámetro, se asigna directamente
                    self.diameter = kwargs['diameter1']
                else:
                    setattr(self, key, value)


app = MainApp()
app.mostrar_principal()
set_appearance_mode("light")
app.mainloop()

# Por Juan Carlos Alonso Luengo
