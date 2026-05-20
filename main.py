from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.utils import get_color_from_hex
from kivy.core.window import Window

DATA_SOLUCIONES = [
    {"codigo": "1.1", "aplicacion": "Bajo Cubierta (Chapa)", "sistema": "Celulosa Proyectada", "espesor": "30 mm", "precio_m2": 13500},
    {"codigo": "1.2", "aplicacion": "Sobre cielorraso", "sistema": "Celulosa Soplada", "espesor": "100 mm", "precio_m2": 18000},
    {"codigo": "1.3", "aplicacion": "Tabiques Drywall", "sistema": "Celulosa Proyectada", "espesor": "70 mm", "precio_m2": 18000},
    {"codigo": "1.4", "aplicacion": "Tabiques Drywall", "sistema": "Celulosa Proyectada", "espesor": "35 mm", "precio_m2": 13500},
    {"codigo": "1.5", "aplicacion": "Tabiques Drywall", "sistema": "Celulosa Proyectada", "espesor": "100 mm", "precio_m2": 20000},
    {"codigo": "1.6", "aplicacion": "Tabiques Steel Frame", "sistema": "Celulosa Proyectada", "espesor": "100 mm", "precio_m2": 20000},
    {"codigo": "1.7", "aplicacion": "Aislación exterior", "sistema": "EIFS", "espesor": "40 mm", "precio_m2": 52000}
]

OPCIONES_DESCUENTOS = {
    "Sin Descuento": 0.0,
    "Descuento Cliente (5%)": 0.05,
    "Descuento Empresa (10%)": 0.10
}

class PresupuestadorScreen(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = [30, 40, 30, 40]
        self.spacing = 15
        
        # Color de fondo Dark Industrial
        Window.clearcolor = get_color_from_hex('#0f172a')
        
        # Encabezado
        self.add_widget(Label(text="STEELMAT", font_size='28sp', bold=True, color=get_color_from_hex('#2dd4bf'), size_hint_y=None, height=40))
        self.add_widget(Label(text="SISTEMAS DE AISLACIÓN INTELIGENTE", font_size='11sp', color=get_color_from_hex('#94a3b8'), size_hint_y=None, height=20))
        
        # 1. Selector Aplicación
        self.add_widget(Label(text="1. Aplicación Recomendada:", font_size='14sp', bold=True, color=get_color_from_hex('#f1f5f9'), halign='left', size_hint_y=None, height=25))
        apps_unicas = sorted(list(set(item["aplicacion"] for item in DATA_SOLUCIONES)))
        self.spinner_app = Spinner(text="Seleccione Aplicación...", values=apps_unicas, background_color=get_color_from_hex('#1e293b'), color=get_color_from_hex('#ffffff'), size_hint_y=None, height=50)
        self.spinner_app.bind(text=self.actualizar_espesores)
        self.add_widget(self.spinner_app)
        
        # 2. Selector Espesor
        self.add_widget(Label(text="2. Sistema y Espesor:", font_size='14sp', bold=True, color=get_color_from_hex('#f1f5f9'), halign='left', size_hint_y=None, height=25))
        self.spinner_esp = Spinner(text="Primero elija aplicación...", values=[], disabled=True, background_color=get_color_from_hex('#1e293b'), color=get_color_from_hex('#ffffff'), size_hint_y=None, height=50)
        self.spinner_esp.bind(text=self.guardar_seleccion)
        self.add_widget(self.spinner_esp)
        
        # 3. Selector Descuento
        self.add_widget(Label(text="3. Beneficio / Descuento:", font_size='14sp', bold=True, color=get_color_from_hex('#f1f5f9'), halign='left', size_hint_y=None, height=25))
        self.spinner_desc = Spinner(text="Sin Descuento", values=list(OPCIONES_DESCUENTOS.keys()), background_color=get_color_from_hex('#1e293b'), color=get_color_from_hex('#ffffff'), size_hint_y=None, height=50)
        self.add_widget(self.spinner_desc)
        
        # 4. Entrada M2
        self.add_widget(Label(text="4. Superficie (m²):", font_size='14sp', bold=True, color=get_color_from_hex('#f1f5f9'), halign='left', size_hint_y=None, height=25))
        self.input_m2 = TextInput(hint_text="Ej: 150", input_type='number', input_filter='float', multiline=False, background_color=get_color_from_hex('#1e293b'), foreground_color=get_color_from_hex('#ffffff'), size_hint_y=None, height=50, padding=[15, 12, 15, 12])
        self.add_widget(self.input_m2)
        
        # Botón Calcular
        self.btn_calcular = Button(text="CALCULAR PRESUPUESTO", font_size='16sp', bold=True, background_color=get_color_from_hex('#14b8a6'), background_normal='', color=get_color_from_hex('#ffffff'), size_hint_y=None, height=55)
        self.btn_calcular.bind(on_press=self.calcular)
        self.add_widget(self.btn_calcular)
        
        # Cuadro de Resultados
        self.lbl_resultado = Label(text="Complete los datos superiores...", font_size='14sp', color=get_color_from_hex('#cbd5e1'), halign='center', valign='middle')
        self.add_widget(self.lbl_resultado)
        
        self.items_filtrados = []
        self.item_seleccionado = None

    def actualizar_espesores(self, spinner, text):
        self.items_filtrados = [item for item in DATA_SOLUCIONES if item["aplicacion"] == text]
        self.spinner_esp.values = [f"{i['sistema']} ({i['espesor']})" for i in self.items_filtrados]
        self.spinner_esp.disabled = False
        self.spinner_esp.text = "Seleccionar espesor..."
        self.item_seleccionado = None

    def guardar_seleccion(self, spinner, text):
        for item in self.items_filtrados:
            if f"{item['sistema']} ({item['espesor']})" == text:
                self.item_seleccionado = item
                break

    def calcular(self, instance):
        if not self.item_seleccionado:
            self.lbl_resultado.text = "Error: Seleccione Aplicación y Espesor."
            return
        try:
            m2 = float(self.input_m2.text.replace(",", "."))
            if m2 <= 0: raise ValueError
        except ValueError:
            self.lbl_resultado.text = "Error: Ingrese un número m² válido."
            return

        desc = OPCIONES_DESCUENTOS[self.spinner_desc.text]
        subtotal = m2 * self.item_seleccionado["precio_m2"]
        monto_desc = subtotal * desc
        total = subtotal - monto_desc
        
        self.lbl_resultado.text = (
            f"Configuración: {self.item_seleccionado['aplicacion']}\n"
            f"Solución: {self.item_seleccionado['sistema']} ({self.item_seleccionado['espesor']})\n"
            f"Rendimiento: {m2:,.2f} m² | Base: ${self.item_seleccionado['precio_m2']:,}/m²\n"
            f"Subtotal: ${subtotal:,.2f}\n"
            f"Descuento: -${monto_desc:,.2f}\n"
            f"-----------------------------------------\n"
            f"TOTAL ESTIMADO: ${total:,.2f} ARS"
        )

class SteelmatApp(App):
    def build(self):
        return PresupuestadorScreen()

if __name__ == '__main__':
    SteelmatApp().run()