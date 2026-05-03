import streamlit as st
import pandas as pd
import numpy as np
import libreria_funciones_proyecto1 as lf
import libreria_clases_proyecto1 as lc



# Menú de selección de página
menu = st.sidebar.selectbox(
    "Navegación",
    ["🏠 Home", "💰 Ejercicio 1", "📊 Ejercicio 2", "⚙️ Ejercicio 3", "🧩 Ejercicio 4"]
)

st.title("🚀 DMC - Especialización en Python for Analytics 🚀")

# --- Interfaz Streamlit ---
if menu == "🏠 Home":
    
    st.markdown("""
    <h1 style="background: linear-gradient(to right, #ff7e5f, #feb47b); 
    color: white; text-align: center; padding: 30px;">
    Mi primer proyecto de Python
    </h1>
    """, unsafe_allow_html=True)
    
    st.subheader("🏠 Bienvenido, te saluda Gustavo Garufi 👋")
    st.markdown("""
    Respecto a mi, soy Ingeniero de Sistemas, y trabajo cono Engineer Support.
    Es la primera vez que estoy estudiando Python, me parece una herramienta sumamente importante en la actualidad.
    """)

    st.write("""
        **Breve descripción del proyecto** 🛠️
        
        Esta aplicación interactiva fue desarrollada con **Streamlit** como parte del módulo de Python Fundamentals. 
        El proyecto integra conceptos claves como estructuras de datos, funciones, programación orientada a objetos 
        y desarrollo de interfaces interactivas.
        
        - Flujo de caja
        - Registro de productos
        - Uso de funciones
        - Uso de clases (CRUD)
    """)

    st.write("""
        **Tecnologías utilizadas** 🛠️
        
        - Python
        - Streamlit
        - Pandas
        - NumPy
        - Github
        - Streamlit Cloud
        - CRUD
        - POO
    """)

# EJERCICIO 1
elif menu == "💰 Ejercicio 1":
    st.markdown("""
    <h1 style="background: linear-gradient(to right, #52c234, #061700); 
    color: white; text-align: center; padding: 20px;">
    💰 Ejercicio 1 - Flujo de Caja
    </h1>
    """, unsafe_allow_html=True)
    
    st.markdown("Registra tus ingresos y gastos para calcular tu saldo.")
    if "movimientos" not in st.session_state:
        st.session_state.movimientos = []

    # Ingresar Inputs
    concepto = st.text_input("Concepto")
    tipo = st.selectbox("Tipo de movimiento", ["Ingreso", "Gasto"])
    valor = st.number_input("Valor", min_value=0.0, step=1.0)
    
    #Boton
    if st.button("Agregar Movimiento"):
        st.session_state.movimientos.append({
            "Concepto": concepto,
            "Tipo": tipo,
            "Valor": valor
        })
        st.success("Movimiento agregado correctamente")
    
    #Mostrar Tabla
    if st.session_state.movimientos:
        df = pd.DataFrame(st.session_state.movimientos)
        st.dataframe(df)
    
    #Calculos
    ingresos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Ingreso")
    gastos = sum(m["Valor"] for m in st.session_state.movimientos if m["Tipo"] == "Gasto")
    saldo = ingresos - gastos

    #Resultados
    st.write("Ingresos:", ingresos)
    st.write("Gastos:", gastos)
    st.write("Saldo:", saldo)

    #Flujo
    if saldo > 0:
        st.success("✔ Flujo de caja positivo")
    elif saldo < 0:
        st.error("✖ Flujo de caja negativo")
    else:
        st.info("➖ Flujo equilibrado")




#EJERCICIO 2
elif menu == "📊 Ejercicio 2":
    st.markdown("""
    <h1 style="background: linear-gradient(to right, 52c234, #061700); 
    color: white; text-align: center; padding: 20px;">
    📊 Ejercicio 2
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("📦 Registro de venta de productos en bodega.")
    if "productos" not in st.session_state:
        st.session_state.productos = []

    #Inputs
    nombre = st.text_input("Nombre del producto")
    categoria = st.text_input("Categoría")
    precio = st.number_input("Precio", min_value=0.0)
    cantidad = st.number_input("Cantidad", min_value=1)

    #Boton
    if st.button("Agregar producto"):
        total = precio * cantidad
        registro = np.array([nombre, categoria, precio, cantidad, total])
        st.session_state.productos.append(registro)

    #Tabla
    if st.session_state.productos:
        datos = np.array(st.session_state.productos)        
        df = pd.DataFrame(
            datos,
            columns=["Producto", "Categoría", "Precio", "Cantidad", "Total"]
        )
        st.dataframe(df)


elif menu == "⚙️ Ejercicio 3":
    st.markdown("""
    <h1 style="background: linear-gradient(to right, 52c234, #061700); 
    color: white; text-align: center; padding: 20px;">
    ⚙️ Ejercicio 3
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("Sección de calculos respecto a Tecnología e Informática")

    tabs = st.tabs(["📊 Calcular Métricas", "🛠️ Disponibilidad del Sistema", "🕒 Tiempo transferencia de Archivo"])

    with tabs[0]:
        st.header("📊 Calcular Métricas")
    
        if "historial_metricas" not in st.session_state:
            st.session_state.historial_metricas = []
        
        tp = st.number_input("True Positives (TP)", min_value=0)
        fp = st.number_input("False Positives (FP)", min_value=0)
        fn = st.number_input("False Negatives (FN)", min_value=0)

        if st.button("Calcular métricas"):        
            resultado = lf.calcular_metricas_clasificacion(tp, fp, fn)
            st.write("Resultados:")
            st.write(resultado)
            # Guardar en historial
            st.session_state.historial_metricas.append({
                "TP": tp,
                "FP": fp,
                "FN": fn,
                "Precisión": resultado["precision"],
                "Recall": resultado["recall"],
                "F1 Score": resultado["f1_score"]
            })
            
        if st.session_state.historial_metricas:
        
            df_historial = pd.DataFrame(st.session_state.historial_metricas)
            st.subheader("Historial")
            st.dataframe(df_historial)
    
    with tabs[1]:
        st.header("🛠️ Disponibilidad del Sistema")

        if "historial_disponibilidad" not in st.session_state:
            st.session_state.historial_disponibilidad = []
        
        tt = st.number_input("Tiempo total (horas)", min_value=1.0)
        tc = st.slider("Tiempo de caída (horas)", min_value=0.0, max_value= 24.0)

        if st.button("Calcular disponibilidad"):
            resultado = lf.calcular_disponibilidad_sistema(tt, tc)
            st.write("Resultado:")
            st.write(resultado)
            # Guardar en historial
            st.session_state.historial_disponibilidad.append({
                "Tiempo total": tt,
                "Tiempo caída": tc,
                "Disponibilidad (%)": resultado["disponibilidad_pct"]
            })

        if st.session_state.historial_disponibilidad:
            df = pd.DataFrame(st.session_state.historial_disponibilidad)
            st.subheader("Historial")
            st.dataframe(df)

    
    with tabs[2]:
        st.header("🕒 Tiempo transferencia de Archivo")

        if "historial_transferencia" not in st.session_state:
            st.session_state.historial_transferencia = []

        tamano = st.number_input("Tamaño del archivo (MB)", min_value=1.0)
        velocidad = st.number_input("Velocidad de red (Mbps)", min_value=1.0)
        
        if st.button("Calcular tiempo"):    
            resultado = lf.calcular_tiempo_transferencia_archivo(tamano, velocidad)
            st.write("Resultado:")
            st.write(resultado)
            # Guardar en historial
            st.session_state.historial_transferencia.append({
                "Tamaño (MB)": tamano,
                "Velocidad (Mbps)": velocidad,
                "Tiempo (segundos)": resultado["tiempo_segundos"],
                "Tiempo (minutos)": resultado["tiempo_minutos"]
            })

        if st.session_state.historial_transferencia:    
            df = pd.DataFrame(st.session_state.historial_transferencia)
            st.subheader("Historial")
            st.dataframe(df)

        


elif menu == "🧩 Ejercicio 4":
    st.markdown("""
    <h1 style="background: linear-gradient(to right, 52c234, #061700); 
    color: white; text-align: center; padding: 20px;">
    🧩 Ejercicio 4
    </h1>
    """, unsafe_allow_html=True)

    st.markdown("Operación CRUD de Servidores de Informática")

    if "servidores" not in st.session_state:
        st.session_state.servidores = []
    
    tabs = st.tabs(["➕ Agregar Servidor", "📋 Listar Servidores", "🔄 Actualizar Servidores", "🗑️ Eliminar Servidores"])

    with tabs[0]:
        st.header("➕ Agregar Servidor")
    
        nombre = st.text_input("Nombre del servidor")
        tiempo_total = st.number_input("Tiempo total (horas)", min_value=1.0)
        tiempo_caida = st.number_input("Tiempo de caída (horas)", min_value=0.0)
        alm_total = st.number_input("Almacenamiento total (GB)", min_value=1.0)
        alm_usado = st.number_input("Almacenamiento usado (GB)", min_value=0.0)

        #Crear
        if st.button("Crear servidor"):    
            servidor = lc.Servidor(
                nombre,
                tiempo_total,
                tiempo_caida,
                alm_total,
                alm_usado
            )
            st.session_state.servidores.append(servidor)
            st.success("Servidor creado")
    
    with tabs[1]:
        st.header("📋 Listar Servidores")
        #Ver
        if st.session_state.servidores:    
            datos = []
            for act in st.session_state.servidores:
                datos.append(act.resumen())
            df = pd.DataFrame(datos)
            st.dataframe(df)

    with tabs[2]:
        st.header("🔄 Actualizar Servidores")

        if st.session_state.servidores:

            opciones = list(range(len(st.session_state.servidores)))
            seleccion = st.selectbox("Selecciona índice", opciones)

            update = st.number_input("Nuevo almacenamiento total (GB)", min_value=1.0)

            if st.button("Actualizar"):
                servidor = st.session_state.servidores[seleccion]
                servidor.almacenamiento_total_gb = update
                st.success("Servidor actualizado")

        else:
            st.info("No hay servidores para actualizar.")
    

    with tabs[3]:
        st.header("🗑️ Eliminar Servidores")

        #Eliminar
        nombres = [a.nombre for a in st.session_state.servidores]
        if nombres:
            seleccion = st.selectbox("Selecciona un servidor para eliminar", nombres)
            if st.button("Eliminar"):
                st.session_state.servidores = [a for a in st.session_state.servidores if a.nombre != seleccion]
                st.success("Servidor eliminada correctamente.")
        else:
            st.info("No hay actividades para eliminar.")