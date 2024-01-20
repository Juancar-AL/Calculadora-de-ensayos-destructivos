from customtkinter import CTkEntry, CTkImage, CTk, CTkButton, CTkRadioButton, CTkCheckBox, CTkLabel, CTk, StringVar, IntVar, set_appearance_mode
from tkinter import END
from calc.brinell import Brinell, brinell_ensayo
from calc.vickers import Vickers, vickers_ensayo
from calc.traction import Traction, trac_ensayo
from calc.charpy import Charpy, charpy_ensayo
from PIL import Image

image = CTkImage(light_image=Image.open("others/theme.png"))

tema_interfaz = False
ensayo = False


brinell_instance = Brinell()
vickers_instance = Vickers()
traction_instance = Traction()
charpy_instance = Charpy()


class MainApp(CTk):
    def __init__(self) -> None:
        super().__init__()

        # Datos básicos de la pantalla (Dimensiones, título, distribución de casillas, icono...)
        self.title("Calculadora de ensayos destructivos")
        self.geometry("1000x400")
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
            "#7CC0A2", "#45B584"), text_color="#000000", hover_color="#88D4B2", width=200)
        self.charpy_button = CTkButton(self, text="Ensayo Charpy", command=self.mostrar_ensayo_c, corner_radius=100, fg_color=(
            "#7CC0A2", "#45B584"), text_color="#000000", hover_color="#88D4B2", width=200)
        self.name = CTkLabel(self, text="Calculadora de ensayos destructivos", fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.autor = CTkLabel(self, text="Por Juan Carlos Alonso Luengo", fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100, width=600)
        self.tema = CTkButton(self, image=image, text="Tema",  command=cambiar_apariencia, fg_color=(
            "#353D3A", "#A4A7A6"), text_color="#FFFFFF", hover_color=("#5A6863", "#787878"), width=200, corner_radius=100)

        # WIDGETS DE LAS PANTALLAS DE LOS ENSAYOS

        # Etiquetas de texto que mostrarán los resultados de los ensayos
        self.resultado1 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado2 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado3 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado4 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado5 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado6 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado7 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado8 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado9 = CTkLabel(self, width=200, fg_color=(
            "#D7D7D7", "#555555"), corner_radius=100)
        self.resultado10 = CTkLabel(self, width=200, fg_color=(
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

        # Etiquetas con texto que solamente muestran ese texto
        self.datos = CTkLabel(self, text="Datos", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.resultados = CTkLabel(self, text="Resultados", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.altura = CTkLabel(self, text="Altura (m)", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.angulos = CTkLabel(self, text="Ángulos", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.energia = CTkLabel(self, text="Energía", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.lados = CTkLabel(self, text="Lados (mm)", width=160, fg_color=(
            "#7CC0A2", "#45B584"), corner_radius=100)
        self.error = CTkLabel(
            self, text="Has de rellenar al menos dos variables", text_color=("#45B584", "#45B584"))

        # Casillas para marcar las diferentes opciones de cálculo del ensayo de tracción
        # Variable que almacena que casilla está marcada
        self.type = IntVar(value=0)
        self.casilla_tension = CTkRadioButton(
            self, text="Tension", command=self.color_change, variable=self.type, value=1, fg_color=("#7CC0A2", "#45B584"), width=200)
        self.casilla_fuerza = CTkRadioButton(
            self, text="Fuerza", command=self.color_change, variable=self.type, value=2, fg_color=("#7CC0A2", "#45B584"), width=200)
        self.casilla_deformacion_unitaria = CTkRadioButton(
            self, text="Deformación", command=self.color_change, variable=self.type, value=3, fg_color=("#7CC0A2", "#45B584"), width=200)
        self.casilla_area = CTkRadioButton(
            self, text="Area", command=self.color_change, variable=self.type, value=4, fg_color=("#7CC0A2", "#45B584"), width=200)
        self.casilla_modulo_young = CTkRadioButton(
            self, text="Modulo de Young", command=self.color_change, variable=self.type, value=5, fg_color=("#7CC0A2", "#45B584"), width=200)

        # Casilla para indicar en el ensayo de tracción si se encuentra en la zona proporcionañ
        # Variable que almacena el estado de la casilla
        self.zona_proporcional = StringVar(value="off")
        self.casilla_proporcional = CTkCheckBox(self, text="Zona proporcional", command=self.color_change, variable=self.zona_proporcional,
                                                onvalue="on", offvalue="off", fg_color=("#7CC0A2", "#45B584"), hover_color=("#7CC0A2", "#45B584"))

    # Mediante el métido .grid muestra los elemetos de la pantalla principal, también se encarga de ocultar aquellos ensayos que puedan ensar abiertos
    def mostrar_principal(self):

        global ensayo

        # Comprueba si algún ensayo se está mostrando y llama a la función que los oculta
        if ensayo:
            self.ocultar_ensayo()

        # Ordena en casillas y hace que parezcan en pantalla los elementos  de la pantalla principal
        self.brinell_button.grid(
            column=0, row=1, padx=20, pady=20, sticky="ns")
        self.vickers_button.grid(
            column=2, row=1, padx=20, pady=20, sticky="ns")
        self.traction_button.grid(
            column=3, row=1, padx=20, pady=20, sticky="ns")
        self.charpy_button.grid(
            column=4, row=1, padx=20, pady=20, sticky="ns")
        self.name.grid(column=0, row=0, padx=20, pady=20,
                       sticky="nsew", columnspan=5)
        self.autor.grid(column=0, row=2, padx=20, pady=20,
                        sticky="nsew", columnspan=4)
        self.tema.grid(row=2, column=4, pady=20, padx=20, sticky="nsew")

    # Hace que no aparezcan en pantalla los elementos de la pantalla principal
    def ocultar_principal(self):
        principal_list = [self.tema, self.brinell_button,
                          self.vickers_button, self.traction_button, self.charpy_button, self.name, self.autor]

        # Bucle que itera sobre los elementos de la lista aplicandoles el método .grid_forget() para eliminarlos de la pantalla
        for i in principal_list:
            i.grid_forget()

    # Configura y muestra los elementos de la pantalla del ensayo Brinell
    def mostrar_ensayo_b(self):
        # Establece la variable ensayo como verdadera que es la que indica la existencia de un ensayo en pantalla
        global ensayo
        ensayo = True

        self.ocultar_principal()

        # Configuraciones de los elementos de la pantalla del ensayo Brinell

        # Cambia la función que ha de llamar el botón
        self.boton.configure(command=self.calcular_ensayo_b)

        self.entrada_datos_1.configure(
            placeholder_text="Resultado ensayo", width=200)
        self.entrada_datos_2.configure(
            placeholder_text="Diámetro indentador", width=200)
        self.entrada_datos_3.configure(
            placeholder_text="Diámetro huella", width=200)
        self.entrada_datos_4.configure(
            placeholder_text="Fuerza utilizada", width=200)
        self.entrada_datos_5.configure(
            placeholder_text="Constante ensayo", width=200)

        self.resultado1.configure(text="Resultado ensayo", width=200)
        self.resultado2.configure(text="Diametro indendador", width=200)
        self.resultado3.configure(text="Diametro huella", width=200)
        self.resultado4.configure(text="Fuerza utilizada", width=200)
        self.resultado5.configure(text="Fiabilidad", width=200)

        # Después de realizar los cambios muestra los elementos en pantalla
        self.entrada_datos_1.grid(
            row=2, column=0, pady=15, padx=20, sticky="ew")
        self.entrada_datos_2.grid(
            row=3, column=0, pady=15, padx=20, sticky="ew")
        self.entrada_datos_3.grid(
            row=4, column=0, pady=15, padx=20, sticky="ew")
        self.entrada_datos_4.grid(
            row=5, column=0, pady=15, padx=20, sticky="ew")
        self.entrada_datos_5.grid(
            row=6, column=0, pady=15, padx=20, sticky="ew")

        self.boton.grid(row=3, column=2, pady=15, padx=20, sticky="ew")
        self.datos.grid(row=1, column=0, pady=15, padx=20, sticky="ew")
        self.resultados.grid(row=1, column=3, pady=15, padx=20, sticky="ew")
        self.error.grid(row=2, column=2, pady=15, padx=20, sticky="ew")

        self.resultado1.grid(row=2, column=3, pady=15, padx=20, sticky="ew")
        self.resultado2.grid(row=3, column=3, pady=15, padx=20, sticky="ew")
        self.resultado3.grid(row=4, column=3, pady=15, padx=20, sticky="ew")
        self.resultado4.grid(row=5, column=3, pady=15, padx=20, sticky="ew")
        self.resultado5.grid(row=6, column=3, pady=15, padx=20, sticky="ew")

        self.tema_e.grid(row=5, column=2, pady=15, padx=20, sticky="ew")
        self.volver.grid(row=6, column=2, pady=15, padx=20, sticky="ew")

    # Configura y muestra los elementos de la pantalla del ensayo Vickers

    def mostrar_ensayo_v(self):
        # Establece la variable ensayo como verdadera que es la que indica la existencia de un ensayo en pantalla
        global ensayo
        ensayo = True

        self.ocultar_principal()

        # Configuraciones de los elementos de la pantalla del ensayo Brinell

        # Cambia la función que ha de llamar el botón
        self.boton.configure(command=self.calcular_ensayo_v)

        self.entrada_datos_2.configure(
            placeholder_text="Diámetro 1", width=200)
        self.entrada_datos_3 .configure(
            placeholder_text="Diámetro 2", width=200)
        self.entrada_datos_1.configure(
            placeholder_text="Resultado ensayo", width=200)
        self.entrada_datos_4.configure(
            placeholder_text="Fuerza utilizada", width=200)

        self.resultado1.configure(text="Resultado ensayo", width=200)
        self.resultado2.configure(text="Diametro", width=200)
        self.resultado4.configure(text="Fuerza utilizada", width=200)

        # Después de realizar los cambios muestra los elementos en pantalla
        self.boton.grid(row=3, column=2, pady=20, padx=20, sticky="ew")

        self.entrada_datos_1.grid(
            row=2, column=0, pady=20, padx=20, sticky="ew")
        self.entrada_datos_2.grid(
            row=3, column=0, pady=20, padx=20, sticky="ew")
        self.entrada_datos_3.grid(
            row=4, column=0, pady=20, padx=20, sticky="ew")
        self.entrada_datos_4.grid(
            row=5, column=0, pady=20, padx=20, sticky="ew")

        self.error.grid(row=2, column=2, pady=20, padx=20, sticky="ew")
        self.datos.grid(row=1, column=0, pady=20, padx=20, sticky="ew")
        self.resultados.grid(row=1, column=3, pady=20, padx=20, sticky="ew")

        self.resultado1.grid(row=2, column=3, pady=20, padx=20, sticky="ew")
        self.resultado2.grid(row=3, column=3, pady=20, padx=20, sticky="ew")
        self.resultado4.grid(row=4, column=3, pady=20, padx=20, sticky="ew")

        self.tema_e.grid(row=5, column=2, pady=20, padx=20, sticky="ew")
        self.volver.grid(row=5, column=3, pady=20, padx=20, sticky="ew")

    def mostrar_ensayo_t(self):
        # Establece la variable ensayo como verdadera que es la que indica la existencia de un ensayo en pantalla
        global ensayo
        ensayo = True

        self.ocultar_principal()

        # Configuraciones de los elementos de la pantalla del ensayo Brinell

        # Cambia la función que ha de llamar el botón
        self.boton.configure(command=self.calcular_ensayo_t)

        self.tema_e.configure(width=200)
        self.volver.configure(width=200)

        self.entrada_datos_1.configure(
            placeholder_text="Módulo de Young", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)
        self.entrada_datos_2.configure(
            placeholder_text="Fuerza utilizada", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)
        self.entrada_datos_3.configure(
            placeholder_text="Tension generada", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)
        self.entrada_datos_4.configure(
            placeholder_text="Longitud inicial", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)
        self.entrada_datos_5.configure(placeholder_text="Longitud final",
                                       text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)
        self.entrada_datos_6.configure(placeholder_text="Área",
                                       text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)
        self.entrada_datos_7.configure(
            placeholder_text="Deformación", text_color=("#36454F", "#000000"), placeholder_text_color=("#36454F", "#000000"), width=200)

        self.resultado1.configure(text="Resultado", width=200)

        # Después de realizar los cambios muestra los elementos en pantalla
        self.boton.grid(row=2, column=3, pady=10, padx=20, sticky="ew")

        self.casilla_tension.grid(
            row=1, column=2, pady=10, padx=20,)
        self.casilla_fuerza.grid(
            row=2, column=2, pady=10, padx=20)
        self.casilla_deformacion_unitaria.grid(
            row=3, column=2, pady=10, padx=20)
        self.casilla_area.grid(row=4, column=2, pady=10, padx=20)
        self.casilla_modulo_young.grid(
            row=5, column=2, pady=10, padx=20)

        self.casilla_proporcional.grid(
            row=3, column=1, pady=10, padx=20, sticky="ew")

        self.entrada_datos_1.grid(
            row=1, column=0, pady=10, padx=20, sticky="ew")
        self.entrada_datos_2.grid(
            row=2, column=0, pady=10, padx=20, sticky="ew")
        self.entrada_datos_3.grid(
            row=3, column=0, pady=10, padx=20, sticky="ew")
        self.entrada_datos_4.grid(
            row=4, column=0, pady=10, padx=20, sticky="ew")
        self.entrada_datos_5.grid(
            row=5, column=0, pady=10, padx=20, sticky="ew")
        self.entrada_datos_6.grid(
            row=1, column=1, pady=10, padx=20, sticky="ew")
        self.entrada_datos_7.grid(
            row=2, column=1, pady=10, padx=20, sticky="ew")

        self.resultado1.grid(row=1, column=3, pady=10, padx=20, sticky="ew")

        self.resultados.grid(row=0, column=3, pady=10, padx=20, sticky="ew")
        self.datos.grid(row=0, column=0, columnspan=3,
                        padx=20, pady=10, sticky="ew")

        self.volver.grid(row=5, column=3, pady=10, padx=20, sticky="ew")
        self.tema_e.grid(row=4, column=3, pady=10, padx=20, sticky="ew")

    def mostrar_ensayo_c(self):
        # Establece la variable ensayo como verdadera que es la que indica la existencia de un ensayo en pantalla
        global ensayo
        ensayo = True

        self.ocultar_principal()

        # Configuraciones de los elementos de la pantalla del ensayo Brinell

        # Cambia la función que ha de llamar el botón
        self.boton.configure(command=self.calcular_ensayo_c)

        self.tema_e.configure(width=100)
        self.volver.configure(width=100)

        self.entrada_datos_1.configure(
            placeholder_text="1", width=100)
        self.entrada_datos_2.configure(
            placeholder_text="2", width=100)
        self.entrada_datos_3.configure(
            placeholder_text="Alfa", width=100)
        self.entrada_datos_4.configure(
            placeholder_text="Beta", width=100)
        self.entrada_datos_5.configure(
            placeholder_text="1", width=100)
        self.entrada_datos_6.configure(
            placeholder_text="2", width=100)
        self.entrada_datos_7.configure(
            placeholder_text="Var. Energía", width=100)
        self.entrada_datos_8.configure(
            placeholder_text="Resultado", width=100)
        self.entrada_datos_9.configure(
            placeholder_text="Area (mm^2)", width=100)
        self.entrada_datos_10.configure(
            placeholder_text="Lado", width=100)
        self.entrada_datos_11.configure(
            placeholder_text="Secc.", width=100)
        self.entrada_datos_12.configure(
            placeholder_text="Masa (kg)", width=100)
        self.entrada_datos_13.configure(
            placeholder_text="Brazo (m)", width=100)

        self.resultado1.configure(text="Altura 1", width=100)
        self.resultado2.configure(text="Altura 2", width=100)
        self.resultado3.configure(text="Energía 1", width=100)
        self.resultado4.configure(text="Energía 2", width=100)
        self.resultado5.configure(
            text="Variación Energía", width=100)
        self.resultado6.configure(text="Lado", width=100)
        self.resultado7.configure(text="Entalla", width=100)
        self.resultado8.configure(text="Área", width=100)
        self.resultado9.configure(text="Masa", width=100)
        self.resultado10.configure(text="Resultado", width=100)

        # Después de realizar los cambios muestra los elementos en pantalla
        self.altura.grid(row=1, column=0,
                         columnspan=2, pady=10, padx=20, sticky="ew")
        self.angulos.grid(row=3, column=0,
                          columnspan=2, pady=10, padx=20, sticky="ew")
        self.energia.grid(row=5, column=0,
                          columnspan=2, pady=10, padx=20, sticky="ew")
        self.lados.grid(row=3, column=2,
                        columnspan=2, pady=10, padx=20, sticky="ew")

        self.entrada_datos_1.grid(row=2, column=0, pady=10, padx=20)
        self.entrada_datos_2.grid(row=2, column=1, pady=10, padx=20)
        self.entrada_datos_3.grid(row=4, column=0, pady=10, padx=20)
        self.entrada_datos_4.grid(row=4, column=1, pady=10, padx=20)
        self.entrada_datos_5.grid(row=6, column=0, pady=10, padx=20)
        self.entrada_datos_6.grid(row=6, column=1, pady=10, padx=20)
        self.entrada_datos_7.grid(
            row=6, column=2, pady=10, padx=0)
        self.entrada_datos_8.grid(
            row=1, column=2, columnspan=2, pady=10, padx=20, sticky="ew")
        self.entrada_datos_9.grid(
            row=2, column=2, columnspan=2, pady=10, padx=20, sticky="ew")
        self.entrada_datos_10.grid(row=4, column=2, pady=10, padx=20)
        self.entrada_datos_11.grid(row=4, column=3, pady=10, padx=20)
        self.entrada_datos_12.grid(
            row=5, column=2, columnspan=2, pady=10, padx=20, sticky="ew")
        self.entrada_datos_13.grid(
            row=6, column=3, pady=10, padx=0)

        self.boton.grid(row=2, column=4, pady=10, padx=20)
        self.volver.grid(row=5, column=4, pady=10, padx=20)
        self.tema_e.grid(row=4, column=4, pady=10, padx=20)
        self.resultados.grid(row=0, column=5, columnspan=2,
                             pady=10, padx=20, sticky="ew")
        self.datos.grid(row=0, column=0, columnspan=4,
                        sticky="ew", pady=10, padx=20)

        self.resultado1.grid(row=2, column=5, pady=10, padx=20)
        self.resultado2.grid(row=2, column=6, pady=10, padx=20)
        self.resultado3.grid(row=3, column=5, pady=10, padx=20)
        self.resultado4.grid(row=3, column=6, pady=10, padx=20)
        self.resultado5.grid(row=4, column=5, columnspan=2,
                             sticky="ew", pady=10, padx=20)
        self.resultado6.grid(row=5, column=5, pady=10, padx=20)
        self.resultado7.grid(row=5, column=6, pady=10, padx=20)
        self.resultado8.grid(row=6, column=5, pady=10, padx=20)
        self.resultado9.grid(row=6, column=6, pady=10, padx=20)
        self.resultado10.grid(row=1, column=5, columnspan=2,
                              sticky="ew", pady=10, padx=20)

    # Hace que los elementos que aparezcan en pantalla sean eliminados de esta y se borren los datos de las entradas de texto
    def ocultar_ensayo(self):
        global ensayo
        lista_widgets = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3, self.entrada_datos_4,
                         self.entrada_datos_5, self.entrada_datos_6, self.entrada_datos_7, self.entrada_datos_8,
                         self.entrada_datos_9, self.entrada_datos_10, self.entrada_datos_11, self.entrada_datos_12,
                         self.entrada_datos_13, self.boton, self.tema_e, self.volver, self.resultado1, self.resultado2,
                         self.resultado3, self.resultado4, self.resultado5, self.resultado6, self.resultado7, self.resultado8,
                         self.resultado9, self.resultado10, self.resultados, self.datos, self.error, self.casilla_area,
                         self.casilla_deformacion_unitaria, self.casilla_fuerza, self.casilla_modulo_young, self.casilla_proporcional,
                         self.casilla_tension, self.lados, self.energia, self.altura, self.angulos]

        for i in lista_widgets:
            i.grid_forget()

        input_list_delete = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3, self.entrada_datos_4,
                             self.entrada_datos_5, self.entrada_datos_6, self.entrada_datos_7, self.entrada_datos_8,
                             self.entrada_datos_9, self.entrada_datos_10, self.entrada_datos_11, self.entrada_datos_12, self.entrada_datos_13]

        for i in input_list_delete:
            i.delete(0, END)
        ensayo = False
        self.mostrar_principal()

    def calcular_ensayo_v(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso sino, asignarlos a una variable
        self.resultado = float((self.entrada_datos_1.get()).replace(
            ",", ".")) if self.entrada_datos_1.get() else None
        self.fuerza = float(self.entrada_datos_4.get().replace(
            ",", ".")) if self.entrada_datos_4.get() else None
        self.diametro_1 = float(self.entrada_datos_2.get().replace(
            ",", ".")) if self.entrada_datos_2.get() else None
        self.diametro_2 = float(self.entrada_datos_3.get().replace(
            ",", ".")) if self.entrada_datos_3.get() else None

        # Función que pasa los valores de las variables declaradas anteriormente a la instancia
        valores(vickers_instance, fuerza=self.fuerza, result=self.resultado,
                diametro1=self.diametro_1, diametro2=self.diametro_2)

        # Calcula los datos del ensayo
        vickers_ensayo(vickers_instance)

        # Actualizar el widget resultadocon el resultado de la función ensayo
        self.resultado1.configure(text=f"{vickers_instance.resultado} HV")
        self.resultado2.configure(text=f"{vickers_instance.diametro} mm")
        self.resultado4.configure(text=f"{vickers_instance.fuerza} kp ")

    def calcular_ensayo_b(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso sino, asignarlos a una variable
        self.resultado = float(self.entrada_datos_1.get().replace(
            ",", ".")) if self.entrada_datos_1.get() else None
        self.diametro = float(self.entrada_datos_2.get().replace(
            ",", ".")) if self.entrada_datos_2.get() else None
        self.huella_diametro = float(
            self.entrada_datos_3.get().replace(",", ".")) if self.entrada_datos_3.get() else None
        self.hardness_modulo_youngant = float(
            self.entrada_datos_5.get().replace(",", ".")) if self.entrada_datos_5.get() else None
        self.fuerza = float(self.entrada_datos_4.get().replace(
            ",", ".")) if self.entrada_datos_4.get() else None

        # Función que pasa los valores de las variables declaradas anteriormente a la instancia
        valores(brinell_instance, fuerza=self.fuerza, result=self.resultado,
                diametro=self.diametro, huella_diametro=self.huella_diametro,
                hardness_modulo_youngant=self.hardness_modulo_youngant)

        # Llamar a la función ensayo y obtener el resultado
        brinell_ensayo(brinell_instance)

        # Muestra los resultados del ensayo en las etiquetas de texto destinadas a ello
        self.resultado1.configure(text=f"{brinell_instance.result} HB")
        self.resultado2.configure(text=f"{brinell_instance.diametro} mm")
        self.resultado3.configure(
            text=f"{brinell_instance.huella_diametro} mm ")
        self.resultado4.configure(text=f"{brinell_instance.fuerza} kp ")
        self.resultado5.configure(
            text='El ensayo es fiable' if brinell_instance.fiabilidad else 'El ensayo no es fiable')

    # Toma los datos de los inputs del ensayo de traccion los actualiza en la clase, los calcula y los muestra
    def calcular_ensayo_t(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso sino, asignarlos a una variable
        modulo_young = float(self.entrada_datos_1.get().replace(
            ",", ".")) if self.entrada_datos_1.get() else None
        fuerza = float(self.entrada_datos_2.get().replace(
            ",", ".")) if self.entrada_datos_2.get() else None
        longitud_inicial = float(self.entrada_datos_4.get().replace(
            ",", ".")) if self.entrada_datos_4.get() else None
        tension = float(self.entrada_datos_3.get().replace(
            ",", ".")) if self.entrada_datos_3.get() else None
        longitud_final = float(self.entrada_datos_5.get().replace(
            ",", ".")) if self.entrada_datos_5.get() else None
        area = float(self.entrada_datos_6.get().replace(
            ",", ".")) if self.entrada_datos_6.get() else None
        deformacion_unitaria = float(self.entrada_datos_7.get().replace(
            ",", ".")) if self.entrada_datos_7.get() else None

        # Función que pasa los valores de las variables declaradas anteriormente a la instancia

        valores(traction_instance, modulo_young=modulo_young, fuerza=fuerza, tension=tension,
                longitud_inicial=longitud_inicial, longitud_final=longitud_final, area=area, deformacion_unitaria=deformacion_unitaria)

        # Llamar a la función ensayo, obtener el resultado y dejarlo en una variable
        result_trac = trac_ensayo(traction_instance, proportional=True if self.zona_proporcional.get() == 'on' else False,
                                  tension=True if self.type.get() == 1 else False, modulo_young=True if self.type.get() == 5 else False,
                                  fuerza=True if self.type.get() == 2 else False, deformacion_unitaria=True if self.type.get() == 3 else False,
                                  area=True if self.type.get() == 4 else False)
        print(result_trac, traction_instance)
        # Actualizar el widget resultadocon el resultado de la función ensayo
        self.resultado1.configure(
            text=f"{result_trac if result_trac != None else 'Error'} ")

    # Toma los datos de los inputs del ensayo del péndulo de Charpy los actualiza en la clase, los calcula y los muestra
    def calcular_ensayo_c(self):
        # Verificar si los CTkEntry están vacíos y asignar None si es el caso sino, asignarlos a una variable

        self.altura1 = float((self.entrada_datos_1.get()).replace(
            ",", ".")) if self.entrada_datos_1.get() else None
        self.altura2 = float((self.entrada_datos_2.get()).replace(
            ",", ".")) if self.entrada_datos_2.get() else None
        self.alfa = float((self.entrada_datos_3.get()).replace(
            ",", ".")) if self.entrada_datos_3.get() else None
        self.beta = float((self.entrada_datos_4.get()).replace(
            ",", ".")) if self.entrada_datos_4.get() else None
        self.energia1 = float((self.entrada_datos_5.get()).replace(
            ",", ".")) if self.entrada_datos_5.get() else None
        self.energia2 = float((self.entrada_datos_6.get()).replace(
            ",", ".")) if self.entrada_datos_6.get() else None
        self.var_energia = float((self.entrada_datos_7.get()).replace(
            ",", ".")) if self.entrada_datos_7.get() else None
        self.resultado = float((self.entrada_datos_8.get()).replace(
            ",", ".")) if self.entrada_datos_8.get() else None
        self.area = float((self.entrada_datos_9.get()).replace(
            ",", ".")) if self.entrada_datos_9.get() else None
        self.lado = float((self.entrada_datos_10.get()).replace(
            ",", ".")) if self.entrada_datos_10.get() else None
        self.entalla = float((self.entrada_datos_11.get()).replace(
            ",", ".")) if self.entrada_datos_11.get() else None
        self.masa = float((self.entrada_datos_12.get()).replace(
            ",", ".")) if self.entrada_datos_12.get() else None
        self.longitud = float((self.entrada_datos_13.get()).replace(
            ",", ".")) if self.entrada_datos_13.get() else None

        # Función que pasa los valores de las variables declaradas anteriormente a la instancia
        valores(charpy_instance, altura_inicial=self.altura1,
                altura_final=self.altura2, longitud=self.longitud, angulo_alpha=self.alfa, angulo_beta=self.beta, energia_potencial1=self.energia1, energia_potencial2=self.energia2, var_energia_potencial=self.var_energia, area=self.area, masa=self.masa, lado=self.lado, entalla=self.entalla, resultado=self.resultado)

        # Calculo del ensayo
        charpy_ensayo(charpy_instance)

        # Muestra los resultados del ensayo en las etiquetas de texto destinadas a ello
        self.resultado1.configure(text=f"{charpy_instance.altura_inicial} m")
        self.resultado2.configure(text=f"{charpy_instance.altura_final} m")
        self.resultado3.configure(
            text=f"{charpy_instance.energia_potencial1} J ")
        self.resultado4.configure(
            text=f"{charpy_instance.energia_potencial2} J ")
        self.resultado5.configure(
            text=f"{charpy_instance.var_energia_potencial} J ")
        self.resultado6.configure(text=f"{charpy_instance.lado} mm")
        self.resultado7.configure(text=f"{charpy_instance.entalla} mm")
        self.resultado8.configure(
            text=f"{charpy_instance.area} mm^2 ")
        self.resultado9.configure(
            text=f"{charpy_instance.masa} kg ")
        self.resultado10.configure(
            text=f"{charpy_instance.resultado} J/mm^2 ")

    # En el ensayo de tracción cambiar el color de los inputs que se deben rellenar para obtener ese dato
    def color_change(self):
        # Mediante un bucle restaura el color de los inputs
        entry_list = [self.entrada_datos_1, self.entrada_datos_2, self.entrada_datos_3,
                      self.entrada_datos_4, self.entrada_datos_5, self.entrada_datos_6, self.entrada_datos_7]
        for i in entry_list:
            i.configure(fg_color=(
                "#D7D7D7", "#555555"))

        # Revisa que dato se está tratando de recibir y cambia el color a los inputs necesarios para indicárselo al usuario
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

# Cambia el tema de la aplicación de claro a oscuro


def cambiar_apariencia():
    global tema_interfaz
    set_appearance_mode("light" if tema_interfaz else "dark")
    tema_interfaz = not tema_interfaz

# Función que pasa los diferentes valores asignados a las clases para poder calcular los ensayos


def valores(self, **kwargs):
    if ensayo:
        for key, value in kwargs.items():
            if value is not None:
                if key == 'diametro2' and kwargs['diametro2'] is not None:
                    # Si se dan dos valores para el diámetro, se calcula la media
                    self.diametro = (
                        (kwargs['diametro1']) + kwargs['diametro2']) / 2
                elif key == 'diametro1':
                    # Si solo se da un valor para el diámetro, se asigna directamente
                    self.diametro = kwargs['diametro1']
                else:
                    setattr(self, key, value)


app = MainApp()
app.mostrar_principal()
set_appearance_mode("light")
print("Por Juan Carlos Alonso")
app.mainloop()

# Por Juan Carlos Alonso
