import streamlit as st

# Configuración compacta para pantalla de celular
st.set_page_config(page_title="STEELMAT Presupuestador", page_icon="🏗️", layout="centered")

# Estilo visual Dark Tech / Premium de Steelmat
st.markdown("""
    <style>
        .main { background-color: #0f172a; color: #f8fafc; }
        h1 { color: #2dd4bf; text-align: center; font-family: 'Segoe UI', sans-serif; margin-bottom: 0px; }
        .subtitle { color: #94a3b8; text-align: center; font-size: 11px; font-weight: bold; margin-bottom: 25px; letter-spacing: 1px; }
        div.stButton > button:first-child {
            background-color: #14b8a6; color: white; width: 100%; 
            font-weight: bold; border-radius: 8px; border: none; height: 48px; font-size: 16px;
        }
        div.stButton > button:first-child:hover { background-color: #0d9488; color: white; }
        .res-box { 
            background-color: #1e293b; padding: 18px; border-radius: 10px; 
            border: 1px solid #334155; font-family: monospace; color: #e2e8f0; font-size: 14px;
        }
    </style>
""", unsafe_allow_html=True)

# Base de datos original
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

st.markdown("<h1>STEELMAT</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtitle'>SISTEMAS DE AISLACIÓN INTELIGENTE</p>", unsafe_allow_html=True)

# 1. Selección de Aplicación
apps_unicas = sorted(list(set(item["aplicacion"] for item in DATA_SOLUCIONES)))
app_sel = st.selectbox("1. Aplicación Recomendada:", ["Seleccione..."] + apps_unicas)

# 2. Selección de Sistema y Espesor
if app_sel != "Seleccione...":
    items_filtrados = [item for item in DATA_SOLUCIONES if item["aplicacion"] == app_sel]
    opciones_esp = [f"{i['sistema']} ({i['espesor']})" for i in items_filtrados]
    esp_sel = st.selectbox("2. Sistema y Espesor disponible:", opciones_esp)
    item_seleccionado = next(i for i in items_filtrados if f"{i['sistema']} ({i['espesor']})" == esp_sel)
    st.caption(f"Código: {item_seleccionado['codigo']}  |  Precio: ${item_seleccionado['precio_m2']:,} / m²")
else:
    st.selectbox("2. Sistema y Espesor disponible:", ["Primero elija aplicación..."], disabled=True)
    item_seleccionado = None

# 3 y 4. Inputs en paralelo
col1, col2 = st.columns(2)
with col1:
    desc_sel = st.selectbox("3. Beneficio / Desc:", list(OPCIONES_DESCUENTOS.keys()))
with col2:
    m2_input = st.text_input("4. Superficie (m²):", placeholder="Ej: 150")

st.markdown("<br>", unsafe_allow_html=True)

if st.button("CALCULAR PRESUPUESTO"):
    if not item_seleccionado:
        st.error("Falta seleccionar la aplicación y espesor técnica.")
    elif not m2_input:
        st.error("Ingrese los metros cuadrados.")
    else:
        try:
            m2 = float(m2_input.replace(",", "."))
            if m2 <= 0: raise ValueError
            
            subtotal = m2 * item_seleccionado["precio_m2"]
            descuento_monto = subtotal * OPCIONES_DESCUENTOS[desc_sel]
            total = subtotal - descuento_monto
            
            st.markdown("**RESUMEN COMERCIAL**")
            resumen = (
                f"Configuración:   {item_seleccionado['aplicacion']}\n"
                f"Solución Técnica:{item_seleccionado['sistema']} ({item_seleccionado['espesor']})\n"
                f"Código Único:    [{item_seleccionado['codigo']}]\n"
                f"-----------------------------------------\n"
                f"Rendimiento:     {m2:,.2f} m²\n"
                f"Precio Base:     ${item_seleccionado['precio_m2']:,} / m²\n"
                f"Subtotal Neto:   ${subtotal:,.2f}\n"
                f"Beneficio Aplic.:-${descuento_monto:,.2f} ({desc_sel})\n"
                f"-----------------------------------------\n"
                f"TOTAL ESTIMADO:  ${total:,.2f} ARS"
            )
            st.markdown(f"<pre class='res-box'>{resumen}</pre>", unsafe_allow_html=True)
        except ValueError:
            st.error("Ingrese una superficie válida mayor a 0.")
